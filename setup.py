from setuptools import setup

if __name__ == '__main__':
    try:
        long_desc = open('README.md').read()
    except FileNotFoundError:
        long_desc = None

    setup(
        name='gpu-batch',
        description='Batch bsub launcher',
        long_description=long_desc,
        author='Maxim Kochurov <maxim.v.kochurov@gmail.com>',
        python_requires='>=3.5',
        scripts=['gpu-batch.sub'],
    )
