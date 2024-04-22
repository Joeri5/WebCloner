from typing import Protocol

class IGitService(Protocol):
    def clone_repo(self) -> bool: ...