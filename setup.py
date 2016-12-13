"""Setup for ubcpi XBlock."""

import os
from setuptools import setup


def package_data(pkg, roots):
    """Generic function to find package_data.

    All of the files under each of the `roots` will be declared as package
    data for package `pkg`.

    """
    data = []
    for root in roots:
        for dirname, _, files in os.walk(os.path.join(pkg, root)):
            for fname in files:
                data.append(os.path.relpath(os.path.join(dirname, fname), pkg))

    return {pkg: data}


def readme():
    if os.path.exists('README.rst'):
        with open('README.rst') as f:
            return f.read()
    else:
        # fallback to a default description
        return 'UBC Peer Rationale Reflection Tool'


setup(
    name='ubcpien-xblock',
    version='0.6.0',
    description='UBC Peer Rationale Reflection XBlock',
    long_description=readme(),
    license='Affero GNU General Public License v3 (GPLv3)',
    author="UBC CTLT",
    author_email="pan.luo@ubc.ca",
    packages=['ubcpien'],
    install_requires=[
        'XBlock',
    ],
    entry_points={
        'xblock.v1': [
            'ubcpien = ubcpien.ubcpien:ubcpienXBlock',
        ]
    },
    package_data=package_data("ubcpien", ["static", "public", "translations"]),
    keywords=['edx', 'peer rationale reflection', 'ubc'],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Plugins",
        "Framework :: Django",
        "Intended Audience :: Education",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: JavaScript",
        "Topic :: Education",
    ],
)
