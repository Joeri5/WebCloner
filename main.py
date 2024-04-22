import logging
import inject

from interfaces.i_git_checker import IGitChecker
from interfaces.i_git_service import IGitService
from interfaces.i_get_repo_name import IGetRepoName
from interfaces.i_package_service import IPackageService
from interfaces.i_url_validator import IURLValidator

import dependency_container_config

def main(repo_url: str):
    git_checker = inject.instance(IGitChecker)

    if not git_checker.is_git_installed():
        logging.error("Git is required for this script to run.")
        return
    
    git_service = inject.instance(IGitService)
    url_validator = inject.instance(IURLValidator)
    get_repo_name = inject.instance(IGetRepoName)
    package_service = inject.instance(IPackageService)

    if url_validator.is_valid_github_url(repo_url):
        repo_name = get_repo_name.get_repo_name(repo_url)
        cloned = git_service.clone_repo(repo_url, repo_name)

        if cloned:
            logging.info(f"Repository {repo_name} cloned successfully.")
            package_info = package_service.read_package_json('dist/' + repo_name)
            if package_info:
                print("Package.json contents:", package_info)
            else:
                print("Failed to read package.json.")
        else:
            print("Repository cloning failed.")
    else:
        logging.error("Invalid GitHub URL provided.")

if __name__ == "__main__":
    repo_url = input("Enter a github repository url: ")

    logging.basicConfig(level=logging.INFO)

    main(repo_url)
