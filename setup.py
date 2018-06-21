from setuptools import setup

if __name__ == '__main__':
    setup(
        name='gpu-batch',
        author='Maxim Kochurov <maxim.v.kochurov@gmail.com>',
        python_requires='>=3.5',
        scripts=['gpu-batch.sub'],
    )
