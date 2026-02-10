# setup_dependencies.py

"""
This script manages project dependencies automatically.
"""

import subprocess
import sys

def install(package):
    """Install the package using pip"""
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])

if __name__ == '__main__':
    # List of required packages
    required_packages = [
        'requests',
        'numpy',
        'pandas',
        'scikit-learn'
    ]

    for package in required_packages:
        try:
            __import__(package)
        except ImportError:
            print(f'Installing {package}...')
            install(package)