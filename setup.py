from setuptools import setup,find_packages

# find_packages = it is used for finding all the packages present in the entire machine learning application
with open('requirements.txt') as f:
    requirements = f.read().splitlines()
setup(
    name = " Student Performance Analysis",
    version = '0.1',
    author = 'Chandan Kumar Nayak',
    author_email = 'chandankunayak2003@gmail.com',
    packages = find_packages(),
    install_requires = requirements
)