# -*- coding: utf-8 -*-
"""
This module contains the tool of collective.recipe.i18noverrides
"""
import os
from setuptools import setup, find_packages


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

version = '1.3.dev0'

long_description = (
    read('README.txt')
    + '\n' +
    'Detailed Documentation\n'
    '======================\n'
    + '\n' +
    read('collective', 'recipe', 'i18noverrides', 'README.txt')
    + '\n' +
    'Contributors\n'
    '============\n'
    + '\n' +
    read('CONTRIBUTORS.txt')
    + '\n' +
    'Change history\n'
    '==============\n'
    + '\n' +
    read('CHANGES.rst')
    + '\n' +
    'Download\n'
    '========\n'
    )
entry_point = 'collective.recipe.i18noverrides:Recipe'
entry_points = {"zc.buildout": ["default = %s" % entry_point]}

tests_require = ['zope.testing', 'zc.buildout']

setup(name='collective.recipe.i18noverrides',
      version=version,
      description=("Override translations by putting some .po files in the "
                   "i18n directory of the zope 2 instance"),
      long_description=long_description,
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
          'Framework :: Buildout',
          'Framework :: Plone',
          'Framework :: Plone :: 3.3',
          'Intended Audience :: Developers',
          'Topic :: Software Development :: Build Tools',
          'Topic :: Software Development :: Libraries :: Python Modules',
          'License :: OSI Approved :: GNU General Public License (GPL)',
          ],
      keywords='i18n',
      author='Maurits van Rees',
      author_email='m.van.rees@zestsoftware.nl',
      url='https://github.com/collective/collective.recipe.i18noverrides',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['collective', 'collective.recipe'],
      include_package_data=True,
      zip_safe=False,
      install_requires=['setuptools',
                        'zc.buildout'
                        # -*- Extra requirements: -*-
                        ],
      tests_require=tests_require,
      extras_require=dict(tests=tests_require),
      test_suite='collective.recipe.i18noverrides.tests.test_docs.test_suite',
      entry_points=entry_points,
      )
