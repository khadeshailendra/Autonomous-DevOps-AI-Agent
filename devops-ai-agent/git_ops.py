import os

def clone_repo(repo_url):
    os.system(f"git clone {repo_url}")
    return {"status": "repo cloned", "repo": repo_url}
