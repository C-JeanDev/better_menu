from setuptools import setup, find_packages
import os
import codecs
import platform


VERSION = '1.0.13'
DESCRIPTION = 'A simple but cool menu-creation package'

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    LONG_DESCRIPTION = "\n" + fh.read()

install_requires = ['print_color'] if platform.system() == 'Windows' else [
    'print_color', 'getch']


# Setting up
setup(
    name="better_menu",
    version=VERSION,
    url='https://github.com/C-JeanDev/better_menu',
    author="Bilodev, C-JeanDev",
    author_email="bilotta.antonio.biz@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    install_requires=install_requires,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    keywords=['python', 'menu', 'selection menu',
              'menu selection', 'selection', 'cool menu', 'cli'],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
