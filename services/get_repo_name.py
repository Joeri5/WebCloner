from interfaces.i_get_repo_name import IGetRepoName

import re

class GetRepoName(IGetRepoName):
    def get_repo_name(self, url) -> str:
        pattern = r'https?://github\.com/[\w-]+/(?P<repo>[\w-]+)'
        match = re.search(pattern, url)
        if match:
            return match.group('repo')
        else:
            raise ValueError("Invalid GitHub URL or repository name not found.")