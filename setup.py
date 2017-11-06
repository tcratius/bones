try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    ’description’: ’My Project’,
    ’author’: ’Conrad Thiele’,
    ’url’: ’https://github.com/tcratius’,
    ’download_url’: ’Where to download it.’,
    ’author_email’: ’tcratius@gmail.com’,
    ’version’: ’0.1’,
    ’install_requires’: [’pytest’],
    ’packages’: [’mypkg’],
    ’scripts’: [],
    ’name’: ’projectname’

    }


setup(**config)
