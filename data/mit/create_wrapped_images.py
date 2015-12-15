import argparse

import glob
import os
import six
import numpy as np
from os.path import join, abspath, basename, dirname

import cv2

parser = argparse.ArgumentParser()
parser.add_argument('--dir_data', default='.')
parser.add_argument('--wrap', default=600, type=int)

args = parser.parse_args()

dir_cover = join(args.dir_data, 'data_cover')
paths = sorted(glob.glob(join(args.dir_data, 'data', '*', '*.png')))

def save_wrapped_image(fname, s, size=600):
    ss = np.zeros((size, size, 3), s.dtype)
    ss[:s.shape[0], :s.shape[1]] = s
    cv2.imwrite(fname, ss)

def get_id(s):
    bn = basename(s)
    dn = basename(dirname(s))
    return join(dn, bn)

for path in paths:
    img = cv2.imread(path)
    fname = join(dir_cover, get_id(path))
    dir_o = dirname(fname)
    try:
        os.makedirs(dir_o)
    except:
        pass
    print(fname)
    save_wrapped_image(fname, img, args.wrap)
