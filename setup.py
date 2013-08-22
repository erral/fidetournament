from setuptools import setup, find_packages
import os

version = '0.1'

setup(name='fidetournament',
      version=version,
      description="FIDE Tournament Report File (Krause format) parser and creator",
      long_description=open("README.rst").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='chess fide parser',
      author='Mikel Larreategi',
      author_email='larreategi@eibar.org',
      url='https://github.com/erral/fidetournament',
      license='GPL',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
