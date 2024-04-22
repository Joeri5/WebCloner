from typing import Protocol

class IGitChecker(Protocol):
    def is_git_installed(self) -> bool: ...
