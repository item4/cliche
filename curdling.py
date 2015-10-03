import subprocess
import sys
import tempfile

from requrements import (install_requires, deploy_requires, docs_require,
                         tests_require)

args = sys.argv

requirements = install_requires

if 'tests' in args:
    requirements += tests_require

if 'docs' in args:
    requirements += docs_require

if 'deploy' in args:
    requirements += deploy_requires

with tempfile.NamedTemporaryFile() as f:
    for requirement in requirements:
        f.write(requirement.encode('u8') + b'\n')
    subprocess.Popen(['pip', 'install', 'curdling']).communicate()
    subprocess.Popen(['curd', 'install', '-r', f.name]).communicate()
