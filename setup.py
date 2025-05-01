import os, sys
setup_dir = os.path.dirname(__file__)
sys.path.insert(0, os.path.join(setup_dir, "xstatic"))
from pkg import pygments as xs

# The README.txt file should be written in reST so that PyPI can use
# it to generate your project's PyPI page. 
with open('README.txt') as f:
    long_description = f.read()

from setuptools import setup, find_namespace_packages

setup(
    name=xs.PACKAGE_NAME,
    version=xs.PACKAGE_VERSION,
    description=xs.DESCRIPTION,
    long_description=long_description,
    classifiers=xs.CLASSIFIERS,
    keywords=xs.KEYWORDS,
    maintainer=xs.MAINTAINER,
    maintainer_email=xs.MAINTAINER_EMAIL,
    license=xs.LICENSE,
    url=xs.HOMEPAGE,
    platforms=xs.PLATFORMS,
    packages=find_namespace_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=['XStatic >= 2.0.0, < 3.0.0'],
)
