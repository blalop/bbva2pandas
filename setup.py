from setuptools import setup, find_packages
import re

with open('requirements.txt') as req:
    requirements = req.read().splitlines()

with open('README.md', encoding='utf-8') as f:
    readme = f.read()

with open('CHANGELOG.md', encoding='utf-8') as f:
    version = re.findall(r'\[(\d*.\d*.\d*)\]', f.read())[0]


setup(name='bbva2pandas',
      version=version,
      description='Parse BBVA monthly reports directly to a Dataframe',
      long_description=readme,
      long_description_content_type='text/markdown',
      install_requires=requirements,
      scripts=[
          'bin/bbva2pandas',
      ],
      url='https://github.com/blalop/bbva2pandas',
      author='Alejandro Blanco López',
      author_email='alexbl1996@gmail.com',
      license='GPLv3+',
      packages=find_packages(exclude=['grafana', 'tests']),
      keywords='bbva pdf bank regex',
      classifiers=[
          'Development Status :: 4 - Beta',
          'Intended Audience :: Developers',
          'Intended Audience :: Financial and Insurance Industry',
          'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
          'Programming Language :: Python',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 3.8',
          'Programming Language :: Python :: 3.9',
          'Topic :: Database',
          'Topic :: Office/Business :: Financial',
          'Topic :: Office/Business :: Financial :: Accounting',
          'Typing :: Typed'
      ]
      )
