import sys
import glob
import os
from os.path import join, abspath, basename

import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--dir_mit', default='../MIT-intrinsic')
    args = parser.parse_args()
    dir_o = './images_mit_sintel/'
    path_mit = os.path.abspath(join(args.dir_mit, 'data_cover'))
    paths = glob.glob(join(path_mit, '*'))
    for p in paths:
        os.symlink(p, join(dir_o, basename(p)))

    path_sintel_images = './images'
    paths = glob.glob(join(path_sintel_images, '*'))
    for p in paths:
        os.symlink(join('..', p), join(dir_o, basename(p)))

if __name__ == '__main__':
    main()
