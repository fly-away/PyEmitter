from setuptools import setup

setup(
    name='PyEmitter',
    version='1.2.0',
    url='http://github.com/fuzeman/PyEmitter/',

    author='Dean Gardiner',
    author_email='me@dgardiner.net',

    packages=find_packages(exclude=['tests']),
    platforms='any',

    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python'
    ],
)
