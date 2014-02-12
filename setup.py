#!/usr/bin/python

# Copyright (c) Arni Mar Jonsson.
# See LICENSE for details.

import sys

try:
	from setuptools import setup, Extension
except ImportError:
	from distutils.core import setup, Extension

extra_compile_args = ['-I./HyperLevelDB', '-fPIC', '-Wall', '-g2', '-D_GNU_SOURCE', '-O2', '-DNDEBUG']
extra_link_args = ['-L./HyperLevelDB/.libs', '-Bstatic', '-lhyperleveldb', '-L./snappy-read-only/.libs/', '-Bstatic', '-lsnappy']

setup(
	name = 'hyperleveldb',
	version = '0.1',
	maintainer = 'Josep Sanjuas',
	maintainer_email = 'jsanjuas@gmail.com',
	#url = 'http://code.google.com/p/py-leveldb/',

	classifiers = [
		'Development Status :: 4 - Beta',
		'Environment :: Other Environment',
		'Intended Audience :: Developers',
		'License :: OSI Approved :: BSD License',
		'Operating System :: POSIX',
		'Programming Language :: C++',
		'Programming Language :: Python',
		'Programming Language :: Python :: 2.4',
		'Programming Language :: Python :: 2.5',
		'Programming Language :: Python :: 2.6',
		'Programming Language :: Python :: 2.7',
		'Programming Language :: Python :: 3.0',
		'Programming Language :: Python :: 3.1',
		'Programming Language :: Python :: 3.2',
		'Programming Language :: Python :: 3.3',
		'Topic :: Database',
		'Topic :: Software Development :: Libraries'
	],

	description = 'Python bindings for hyperleveldb database library',

	packages = ['hyperleveldb'],
	package_dir = {'hyperleveldb': ''},

	ext_modules = [
		Extension('hyperleveldb',
			sources = [
				# python stuff
				'leveldb_ext.cc',
				'leveldb_object.cc',
			],
			libraries = ['stdc++'],

			extra_compile_args = extra_compile_args,
			extra_link_args = extra_link_args
		)
	]
)
