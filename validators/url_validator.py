import re
from interfaces.i_url_validator import IURLValidator

class URLValidator(IURLValidator):
    def is_valid_github_url(self, url: str) -> bool:
        pattern = r'^https?://(?:www\.)?github\.com/[\w-]+/[\w-]+/?$'
        return re.match(pattern, url) is not None
