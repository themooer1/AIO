from setuptools import setup

setup(
    name='AIOwiki',
    version='1.3',
    packages=['AIO'],
    install_requires=[
        'requests'
    ],
    url='https://github.com/themooer1/AIO',
    license='MIT',
    author='David Smith',
    author_email='fluffy1781@gmail.com',
    description='A Python API for accessing information about episodes on AIOwiki.com'
)
