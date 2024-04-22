import json
import os
from typing import Dict, Optional

from interfaces.i_package_service import IPackageService

class PackageService(IPackageService):
    def read_package_json(self, repo_path: str) -> Optional[Dict]:
        package_path = os.path.join(repo_path, 'package.json')
        try:
            with open(package_path, 'r') as file:
                package_data = json.load(file)
                build_command = package_data.get('scripts', {}).get('build')
                return build_command
        except FileNotFoundError:
            print(f"package.json not found in {repo_path}.")
        except json.JSONDecodeError:
            print("Failed to decode package.json.")
        return None
