# import os
# import re
from setuptools import setup, find_packages

DESCRIPTION = """\
nabbit: Nose integration with Gabbi\
"""

# ld = []
# ldf = open(os.path.join(os.path.dirname(__file__), 'tests', 'about.rst'))
# copy = True
# for line in ldf:
#     if copy:
#         if line.startswith('.. fixt') or line.startswith('.. contents'):
#             continue
#         if line.startswith('Examples'):
#             copy = False
#     elif line.startswith('.. _'):
#         ld.append(line)
#     if copy:
#         ld.append(line)
# LONG_DESCRIPTION = ''.join(ld)
LONG_DESCRIPTION = 'cookies'

CLASSIFIERS = [
    "Development Status :: 3 - Alpha",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Topic :: Software Development :: Testing"
    ]

setup(
    name='nabbit',
    version='0.1.0',
    author='Jason Myers',
    author_email='jason@jasonamyers.com',
    packages=find_packages(),
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    classifiers=CLASSIFIERS,
    url="http://www.github.com/jasonamyers/nose-gabbi",
    include_package_data = True,
    license="MIT License",
    entry_points = {
            'nose.plugins.0.10': [
                'nabbit = nabbit:Nabbit'
                ]
            },
    install_requires=['nose>=0.10.1', 'docutils>=0.5'],
    tests_require=['simplejson>=1.7.1,<2', 'Paste', 'lxml>=2.0'],
    extras_require={'xml': ['lxml>=2.0'],
                    'sphinx': ['Sphinx>=1.0']}
    )
