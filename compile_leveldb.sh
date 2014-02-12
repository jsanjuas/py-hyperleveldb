#!/bin/sh

set -e;

(
	svn checkout http://snappy.googlecode.com/svn/trunk/ snappy-read-only;
	cd snappy-read-only;
	./autogen.sh;
	./configure --enable-shared=no --enable-static=yes;
	make clean;
	make CXXFLAGS='-g -O2 -fPIC';
)

(
	git clone https://github.com/rescrv/HyperLevelDB.git || (
		cd HyperLevelDB; git checkout master; git pull
	);
	cd HyperLevelDB;
	git checkout tags/releases/1.0.1;
	autoreconf -i; ./configure; make
	make .libs/libhyperleveldb.a LDFLAGS='-L../snappy-read-only/.libs/ -Bstatic -lsnappy' OPT='-fPIC -O2 -DNDEBUG -DSNAPPY -I../snappy-read-only' SNAPPY_CFLAGS=''
)
