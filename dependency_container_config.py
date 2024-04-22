import inject

from interfaces.i_git_service import IGitService
from interfaces.i_git_checker import IGitChecker
from interfaces.i_package_service import IPackageService
from interfaces.i_url_validator import IURLValidator
from interfaces.i_get_repo_name import IGetRepoName

from services.git_service import GitService
from services.git_checker import GitChecker
from services.get_repo_name import GetRepoName
from services.package_service import PackageService

from validators.url_validator import URLValidator

def config(binder):
    binder.bind(IGitService, GitService())
    binder.bind(IGitChecker, GitChecker())
    binder.bind(IGetRepoName, GetRepoName())
    binder.bind(IURLValidator, URLValidator())
    binder.bind(IPackageService, PackageService())  

inject.configure_once(config)
