#!/usr/bin/env python3
import sys
import os
import json
import urllib.request
import re

def generate_keywords(path):
    # Extract words from the path to use as keywords
    words = re.findall(r'[a-zA-Z0-9]+', path.lower())
    # filter some generic words
    stopwords = {'md', 'txt', 'skills', 'prompts', 'src', 'main', 'master', 'tree', 'py', 'json', 'github', 'com'}
    keywords = [f"#{w}" for w in set(words) if w not in stopwords and len(w) > 2]
    return " ".join(keywords)

def spider_github(repo_url):
    # Extract owner and repo from url (e.g. https://github.com/sickn33/agentic-awesome-skills)
    match = re.search(r'github\.com/([^/]+)/([^/]+)', repo_url)
    if not match:
        print("Invalid GitHub URL")
        return None
    owner, repo = match.groups()
    repo = repo.replace('.git', '')
    
    # Clean URL of any /tree/main/skills paths
    clean_url = f"https://github.com/{owner}/{repo}"
    
    # Try fetching default branch tree
    # First get repo info to find default branch
    try:
        req = urllib.request.Request(f"https://api.github.com/repos/{owner}/{repo}", headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            repo_data = json.loads(response.read().decode())
            default_branch = repo_data.get('default_branch', 'main')
            description = repo_data.get('description', 'No description provided.')
    except Exception as e:
        print(f"Error fetching repo data: {e}")
        default_branch = 'main'
        description = "External collection."
        
    try:
        # Fetch recursive tree
        req = urllib.request.Request(f"https://api.github.com/repos/{owner}/{repo}/git/trees/{default_branch}?recursive=1", headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            tree_data = json.loads(response.read().decode())
            tree = tree_data.get('tree', [])
    except Exception as e:
        print(f"Error fetching repo tree: {e}")
        return None
        
    import datetime
    out_lines = []
    out_lines.append(f"# {repo}")
    out_lines.append(f"**Repository Originale**: [{clean_url}]({clean_url})")
    out_lines.append(f"**Ultimo Aggiornamento**: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    out_lines.append(f"**Descrizione**: {description}\n")
    out_lines.append(f"## Indice delle Skill e Contenuti")
    
    count = 0
    for item in tree:
        if item['type'] == 'blob':
            path = item['path']
            # We filter for useful files
            if path.endswith('.md') or path.endswith('.py') or path.endswith('.txt') or path.endswith('.json'):
                name_lower = os.path.basename(path).lower()
                if name_lower in ['package.json', 'package-lock.json', 'tsconfig.json', 'tsconfig.node.json']:
                    continue
                # Ignore standard markdown files at root if they are just docs
                if name_lower in ['readme.md', 'contributing.md', 'license.md'] and '/' not in path:
                    continue
                name = os.path.basename(path)
                keywords = generate_keywords(path)
                raw_url = f"https://raw.githubusercontent.com/{owner}/{repo}/{default_branch}/{path}"
                out_lines.append(f"- [**{name}**]({raw_url}): Path -> `{path}`. **Keywords:** {keywords}")
                count += 1
                
    if count == 0:
        out_lines.append("- Nessun file rilevante trovato.")
        
    return "\n".join(out_lines)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 spider_indexer.py <github_url>")
        sys.exit(1)
        
    url = sys.argv[1]
    match = re.search(r'github\.com/([^/]+)/([^/]+)', url)
    if not match:
        print("Invalid GitHub URL")
        sys.exit(1)
    
    owner, repo = match.groups()
    repo = repo.replace('.git', '')
    
    print(f"Spidering {url}...")
    markdown_content = spider_github(url)
    
    if markdown_content:
        out_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "collections")
        os.makedirs(out_dir, exist_ok=True)
        out_path = os.path.join(out_dir, f"{repo}.md")
        with open(out_path, "w") as f:
            f.write(markdown_content)
        print(f"Success! Indice generato in {out_path}")
    else:
        print("Failed to generate index.")
