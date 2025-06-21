from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as readme:
    data=readme.read()

setup(
    name='port_scanner_rq',
    version='1.1.1',
    author='xRangeroQ',
    author_email='xRangeroQ@email.com',
    description='A high-speed threaded TCP port scanner.',
    long_description=data,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    python_requires='>=3.6',
    license="MIT"
)
