wget http://people.csail.mit.edu/rgrosse/intrinsic/intrinsic-data.tar.gz
tar xvf intrinsic-data.tar.gz
mv MIT-intrinsic/data .
rmdir MIT-intrinsic
rm intrinsic-data.tar.gz
python create_dataset.py
python create_shading.py
python create_wrapped_images.py
python create_barron_split.py
