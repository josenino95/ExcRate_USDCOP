from setuptools import setup, find_packages

setup(
    author = "Jose David Nino Muriel",
    description= "App for predicting USD/COP exchange rate for the next day and the next week.",
    name="usdcop-app",
    version="0.1.0",
    packages=find_packages(include=['src', 'src.*']),
    install_requires = [
        'pandas>=1.0',
        'suds>=1.1.2'

    ],
    python_requires = '>=3, !=3.11.*'
)