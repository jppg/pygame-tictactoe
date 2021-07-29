from setuptools import setup, find_packages

setup(
    name='tictactoe',
    version='0.1.0',
    packages=find_packages(include=['code', 'code.*']),
    install_requires=[
        'configparser',
        'pygame',
        'pygame-menu'
        'scikit-learn', 
        'scipy',
        'matplotlib'
    ]
)