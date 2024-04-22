import os
import sys
import subprocess
import unittest

from unittest.mock import patch
from services.git_checker import GitChecker

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

class TestGitChecker(unittest.TestCase):
    def test_is_git_installed_when_git_is_missing(self):
        # Setup the mock to simulate subprocess.run raising a CalledProcessError
        with patch('subprocess.run', side_effect=subprocess.CalledProcessError(1, ['git', '--version'])):
            checker = GitChecker()
            result = checker.is_git_installed()
            self.assertFalse(result)  # Expect False because git is "not installed"

    def test_is_git_installed_when_git_is_available(self):
        # Setup the mock to simulate successful subprocess.run
        with patch('subprocess.run') as mocked_run:
            mocked_run.return_value = subprocess.CompletedProcess(args=['git', '--version'], returncode=0, stdout='git version 2.29.2')
            checker = GitChecker()
            result = checker.is_git_installed()
            self.assertTrue(result)  # Expect True because git is "installed"

if __name__ == '__main__':
    unittest.main()
