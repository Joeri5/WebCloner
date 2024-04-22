from interfaces.i_git_service import IGitService

import subprocess
import os

class GitService(IGitService):
    def clone_repo(self, repo_url: str, repo_name: str):
        try:
            path = 'dist/' + repo_name

            if os.path.exists(path):
                print(f"Repository {repo_name} already exists.")
                print(f"Would you like to delete it and clone again? (y/n)")
                response = input()
                if response.lower() == 'y':
                    subprocess.run(["rm", "-rf", path], check=True)
                else:
                    return False

            subprocess.run(["git", "clone", repo_url, path], check=True)
            return True
        except subprocess.CalledProcessError as e:
            print(f"Error cloning repository: {e}")
            return False