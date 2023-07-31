from setuptools import setup, find_packages

setup(
    name='funniest',
    version='1.0.0',
    url='https://github.com/Icy4r/funniest',
    author='Ian Yung',
    author_email='IYung419@gmail.com',
    description='Joke!',
    packages=find_packages(),
    install_requires=['numpy >= 1.11.1', 'matplotlib >= 1.5.1'],
)