from setuptools import setup,find_packages
from typing import List

setup(
    name='Credit_card_fault_detrction',
    author='aravind',
    author_email='aravindkavati83@gmail.com',
    version='0.0.1',
    install_requirements=['pandas','sklearn','seaborn'],
    packages=find_packages()
)