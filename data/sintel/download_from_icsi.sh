#! /bin/bash
set -eu
scp login.icsi.berkeley.edu:/u/vis/x1/narihira/data/di-sintel/albedo.tar.xz .
scp login.icsi.berkeley.edu:/u/vis/x1/narihira/data/di-sintel/clean.tar.xz .
scp login.icsi.berkeley.edu:/u/vis/x1/narihira/data/di-sintel/shading.tar.xz .
mkdir images
mv *.tar.xz images
(cd images; for p in *.tar.xz ; do tar xvf $p; done)
rm images/*.tar.xz
