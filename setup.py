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
        long_desc = open('README.md').read()
    except FileNotFoundError:
        long_desc = None

    setup(
        name='gpu-batch',
        description='Batch bsub launcher',
        long_description=long_desc,
        version=get_version(),
        author='Maxim Kochurov <maxim.v.kochurov@gmail.com>',
        python_requires='>=3.5',
        scripts=['gpu-batch.sub'],
    )
