from typing import Protocol

class IURLValidator(Protocol):
    def is_valid_github_url(self, url: str) -> bool: ...
