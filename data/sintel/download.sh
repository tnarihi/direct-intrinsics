#! /bin/bash
set -eu
fail=0
[ -d images ] || fail=1 && echo << EOF
So far MPI does not provide a public link to Sintel intrinsic dataset.
Please email us for MPI Sintel dataset.
Once you get dataset, expand files such that you have a folder structure like:

images--- albedo --- alley_1
       |          |
       |          |- alley_2
       |          |
       |          |- ambush_2
       |          |
       |          |- ...
       |
       |- shading --- ...
       |
       |- clean --- ...

Then, run this script again. It will create files that you need for training.
EOF
exit $fail

