from setuptools import setup
from pathlib import Path


here = Path(__file__).parent
long_desc = (here / 'README.md').read_text()

setup(
	name='college-scorecard',
	description='A python library for collegescorecard.ed.gov',
	author='Ahadu Kebede',
	version='1.3',
	author_email='ahadukebede@gmail.com',
	url='https://github.com/ahoodatheguy/scorecard',
	packages=['scorecard'],
	long_description=long_desc,
	long_description_content_type='text/markdown',
)
