#!/usr/bin/env python3
import os
import re
import json
import urllib.request
import urllib.error
import subprocess
import shutil
import datetime

# --- CONFIGURATION ---
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
COLLECTIONS_DIR = os.path.join(os.path.dirname(SCRIPT_DIR), "collections")
REGISTRY_PATH = os.path.join(COLLECTIONS_DIR, "registry.json")
GLOBAL_INDEX_PATH = os.path.join(COLLECTIONS_DIR, "global_registry.md")
SOURCES_PATH = os.path.join(SCRIPT_DIR, "sources.txt")

os.makedirs(COLLECTIONS_DIR, exist_ok=True)

def load_registry():
    if os.path.exists(REGISTRY_PATH):
        try:
            with open(REGISTRY_PATH, "r") as f:
                return json.load(f)
        except Exception:
            pass
    return {}

def save_registry(registry):
    with open(REGISTRY_PATH, "w") as f:
        json.dump(registry, f, indent=2)

def generate_keywords(path, content=""):
    words = re.findall(r'[a-zA-Z0-9]+', path.lower())
    stopwords = {'md', 'txt', 'skills', 'prompts', 'src', 'main', 'master', 'tree', 'py', 'json', 'github', 'com', 'commands', 'agents', 'rules', 'docs', 'tools', 'plugin'}
    keywords = [f"#{w}" for w in set(words) if w not in stopwords and len(w) > 2]
    return " ".join(keywords)

def extract_description(content):
    # Try to find specific descriptive headers
    match = re.search(r'#+\s*(?:When to Use|When to reach for it|What it does|Description|Overview|About|Summary)\s*(.*?)(?=\n#|\Z)', content, re.IGNORECASE | re.DOTALL)
    if match:
        desc = match.group(1).strip()
        if len(desc) > 10:
            return desc.split('\n\n')[0].replace('\n', ' ')
    
    # Try YAML frontmatter
    match = re.search(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
    if match:
        yaml_content = match.group(1)
        desc_match = re.search(r'description:\s*["\']?(.*?)["\']?$', yaml_content, re.IGNORECASE | re.MULTILINE)
        if desc_match and len(desc_match.group(1).strip()) > 5:
            return desc_match.group(1).strip()
            
    # Fallback to first non-empty paragraph that has some substance
    lines = content.split('\n')
    for i, line in enumerate(lines):
        line = line.strip()
        # Skip headers, images, html tags, and very short lines like "**Quickstart:**"
        if line and not line.startswith('#') and not line.startswith('![') and not line.startswith('<') and len(re.sub(r'[^a-zA-Z]', '', line)) > 15:
            # Clean up bolding/italics for the preview
            clean_line = line.replace('**', '').replace('__', '')
            return clean_line[:200] + "..." if len(clean_line) > 200 else clean_line
            
    return "No description available."

def extract_json_description(content):
    try:
        data = json.loads(content)
        if isinstance(data, dict):
            desc = data.get('description') or data.get('name') or "Configuration file."
            return str(desc)[:200]
    except:
        pass
    return "JSON Configuration."

def process_repo(repo_url, registry):
    match = re.search(r'github\.com/([^/]+)/([^/]+)', repo_url)
    if not match:
        print(f"Invalid GitHub URL: {repo_url}")
        return
    owner, repo = match.groups()
    repo = repo.replace('.git', '')
    
    print(f"Processing {owner}/{repo}...")
    
    # 1. Fetch repo data
    try:
        req = urllib.request.Request(f"https://api.github.com/repos/{owner}/{repo}", headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            repo_data = json.loads(response.read().decode())
            default_branch = repo_data.get('default_branch', 'main')
            description = repo_data.get('description', 'No description provided.')
            stars = repo_data.get('stargazers_count', 0)
    except Exception as e:
        print(f"  Error fetching repo data: {e}")
        return

    # 2. Fetch latest commit hash
    try:
        req = urllib.request.Request(f"https://api.github.com/repos/{owner}/{repo}/commits/{default_branch}", headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            commit_data = json.loads(response.read().decode())
            latest_commit = commit_data.get('sha', '')
    except Exception as e:
        print(f"  Error fetching commit data: {e}")
        return
        
    repo_key = f"{owner}/{repo}"
    repo_entry = registry.get(repo_key, {})
    
    if repo_entry.get("commit_hash") == latest_commit:
        print(f"  -> No changes detected (Commit: {latest_commit[:7]}). Updating stars only.")
        repo_entry["stars"] = stars
        registry[repo_key] = repo_entry
        return
        
    print(f"  -> Changes detected. Cloning repository...")
    tmp_dir = os.path.join(SCRIPT_DIR, f"tmp_spider_{repo}_{latest_commit[:7]}")
    
    # Clone
    if os.path.exists(tmp_dir):
        shutil.rmtree(tmp_dir)
    try:
        subprocess.run(["git", "clone", "--depth", "1", "-b", default_branch, f"https://github.com/{owner}/{repo}", tmp_dir], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except subprocess.CalledProcessError:
        print(f"  -> Failed to clone repository.")
        return
        
    # Walk tree and parse
    items = []
    for root, dirs, files in os.walk(tmp_dir):
        # Ignore .git
        if '.git' in dirs:
            dirs.remove('.git')
            
        for file in files:
            # Ignore hidden files, Mac OS X AppleDouble files, etc.
            if file.startswith('.'):
                continue
                
            path = os.path.join(root, file)
            rel_path = os.path.relpath(path, tmp_dir)
            name_lower = file.lower()
            
            if name_lower.endswith('.md') or name_lower in ['plugin.json', 'marketplace.json']:
                if name_lower in ['readme.md', 'contributing.md', 'license.md'] and '/' not in rel_path:
                    continue
                    
                with open(path, "r", encoding="utf-8", errors="ignore") as f:
                    content = f.read()
                    
                if name_lower.endswith('.md'):
                    item_desc = extract_description(content)
                else:
                    item_desc = extract_json_description(content)
                    
                raw_url = f"https://raw.githubusercontent.com/{owner}/{repo}/{default_branch}/{rel_path}"
                keywords = generate_keywords(rel_path, content)
                
                is_mcp = 'mcp' in repo_key.lower() or 'mcp' in name_lower or 'server' in name_lower
                category = "MCP Servers" if is_mcp else "Agentic Skills"
                
                items.append({
                    "name": file,
                    "rel_path": rel_path,
                    "raw_url": raw_url,
                    "description": item_desc,
                    "keywords": keywords,
                    "category": category
                })
                
    # Update registry
    registry[repo_key] = {
        "description": description,
        "stars": stars,
        "commit_hash": latest_commit,
        "url": f"https://github.com/{owner}/{repo}",
        "updated_at": datetime.datetime.now().isoformat(),
        "items": items
    }
    
    # Cleanup
    shutil.rmtree(tmp_dir)
    print(f"  -> Processed {len(items)} items.")

def build_global_registry(registry):
    print("Building Global Registry...")
    categories = {}
    
    for repo_key, repo_data in registry.items():
        repo_stars = repo_data.get("stars", 0)
        repo_url = repo_data.get("url", "")
        
        for item in repo_data.get("items", []):
            cat = item["category"]
            if cat not in categories:
                categories[cat] = []
            
            item_copy = item.copy()
            item_copy["repo_key"] = repo_key
            item_copy["repo_stars"] = repo_stars
            item_copy["repo_url"] = repo_url
            categories[cat].append(item_copy)
            
    out_lines = []
    out_lines.append("# 🌐 Global Agentic Registry")
    out_lines.append(f"**Ultimo Aggiornamento Globale**: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    out_lines.append("> Il database centralizzato per MCP Servers e Agentic Skills, generato da Spider Indexer 3.0.\n")
    
    for cat, items in sorted(categories.items()):
        out_lines.append(f"## 🛠️ {cat}")
        out_lines.append("*(Ordinati per Popolarità / Stelle GitHub del repository di origine)*\n")
        
        # Sort items by repo_stars descending
        items.sort(key=lambda x: x["repo_stars"], reverse=True)
        
        for item in items:
            out_lines.append(f"### {item['name']}")
            out_lines.append(f"**Sorgente**: [Link RAW GitHub]({item['raw_url']}) (Path: `{item['rel_path']}`)")
            out_lines.append(f"**Repo Origine**: [{item['repo_key']}]({item['repo_url']}) (⭐ {item['repo_stars']})")
            out_lines.append(f"**Descrizione/When to Use**: {item['description']}")
            out_lines.append(f"**Keywords**: {item['keywords']}\n")
            
    with open(GLOBAL_INDEX_PATH, "w") as f:
        f.write("\n".join(out_lines))
    print(f"Global Registry written to {GLOBAL_INDEX_PATH}")

def main():
    if not os.path.exists(SOURCES_PATH):
        print(f"Sources file not found at {SOURCES_PATH}")
        return
        
    with open(SOURCES_PATH, "r") as f:
        urls = [line.strip() for line in f if line.strip() and not line.startswith('#')]
        
    registry = load_registry()
    
    for url in urls:
        process_repo(url, registry)
        # Save incrementally
        save_registry(registry)
        
    build_global_registry(registry)

if __name__ == "__main__":
    main()
