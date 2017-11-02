# Setup.py

from setuptools import setup, find_packages
import imgflat

with open('requirements.txt') as f:
    required = f.read().splitlines()

with open('README.md') as f:
    long_description = f.read()


setup(
    name='imgflat',
    version=imgflat.__version__,
    long_description=long_description,
    packages=find_packages(),
    url='https://arlgitgisp01.ecorp.cat.com/PUG/imgflat',
    license='MIT',
    author='walkews',
    author_email='walker_waylon_s@cat.com',
    description='a python library for quickly creating interactive charts',
    install_requires=required,
    test_suite='tests',
    include_package_data=True,
    package_data={'imgflat/templates':['*']},
    zip_safe=False,
    entry_points={'console_scripts':['imgflat=imgflat.inline_img:inline']}

)
