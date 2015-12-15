#! /bin/bash
set -eu
./download.sh
python create_albedo_mask.py
python generate_sintel_rs.py
python generate_sintel_rgs.py
mkdir images_mit_sintel
python create_fusion.py
