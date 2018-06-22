from setuptools import setup
import re


def get_version():
    lines = open('gpu-batch.sub', 'rt').readlines()
    version_regex = r"^__version__ = ['\"]([^'\"]*)['\"]"
    for line in lines:
        mo = re.search(version_regex, line, re.M)
        if mo:
            return mo.group(1)
    raise RuntimeError('Unable to find version in %s.' % ('gpu-batch.sub',))


if __name__ == '__main__':
    try:
        LONG_DESC = open('README.rst').read()
    except FileNotFoundError:
        LONG_DESC = None

    setup(
        name='gpu-batch-sub',
        description='Batch bsub launcher',
        url='https://github.com/ferrine/gpu-batch.sub',
        long_description=LONG_DESC,
        version=get_version(),
        author='Maxim Kochurov',
        author_email='maxim.v.kochurov@gmail.com',
        python_requires='>=3.5',
        scripts=['gpu-batch.sub'],
        license="Apache License, Version 2.0",
        classifiers=[
            'Programming Language :: Python :: 3',
            'License :: OSI Approved :: Apache Software License',
            'Topic :: Scientific/Engineering',
            'Operating System :: OS Independent'
        ]
    )
