import subprocess
from interfaces.i_git_checker import IGitChecker

class GitChecker(IGitChecker):
    def is_git_installed(self) -> bool:
        return self.check_git_version()

    def check_git_version(self):
        try:
            subprocess.run(["git", "--version"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            return True
        except subprocess.CalledProcessError:
            return False
