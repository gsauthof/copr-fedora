#!/bin/bash

set -eux

name=img2pdf
version=0.2.4
filename=$name-$version.tar.gz
url=https://files.pythonhosted.org/packages/source/i/$name/$filename
checksum=140b70fa3a3bfb54e92947818cee01483a4f1492b5d1d02b0f649257f5ffc9ae

. ../build.sh
