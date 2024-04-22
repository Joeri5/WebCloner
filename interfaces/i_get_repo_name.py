from typing import Protocol

class IGetRepoName(Protocol):
    def get_repo_name(self, url: str) -> str: ...