import sys
import glob
import os
import csv
import six
import numpy as np
from os.path import join, abspath, basename, dirname

from matplotlib.image import imsave, imread

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--dir_data', default='.')

args = parser.parse_args()
dir_source_base = args.dir_data
dir_data_mit = '{}/data'.format(args.dir_data)
dir_data_shading = dir_data_mit

def load_source(p):
    return map(lambda x: x[0], csv.reader(open(p, 'r')))

names = {}
for key in [('', 'c'), ('_r', 'r'), ('_s', 's'), ('_m', 'm')]:
    names[key[1]] = load_source(join(dir_source_base, 'source_full%s.txt' % key[0]))

IM_PER_OBJ = 11

def load_images(dir_data, names, ii):
    img = {}
    for key in ['c', 'r', 's', 'm']:
        img[key] = imread(join(dir_data, names[key][ii]))
        img[key] = img[key].astype('float64')
    img['m'][img['m'] > 0] = 1.0
    img['m'] = np.repeat(img['m'][..., np.newaxis], 3, 2)
    img['s'] = np.repeat(img['s'][..., np.newaxis], 3, 2)
    return img

def create_shading(img, alpha):
    s = img['m'].max(2) * img['c'].mean(2) / np.maximum(alpha * img['r'].mean(2), 1e-8)
    return np.repeat(s[..., np.newaxis], 3, 2)
def create_shading_median(img, alpha):
    s = np.median(img['m'], 2) * np.median(img['c'] / np.maximum(alpha * img['r'], 1e-8), 2)
    return np.repeat(s[..., np.newaxis], 3, 2)
def create_shading_color(img, alpha):
    return img['m'] * img['c'] / np.maximum(alpha * img['r'], 1e-8)

def save_padded_image(fname, s, size=600):
    ss = np.zeros((size, size, 3))
    ss[:s.shape[0], :s.shape[1]] = s
    imsave(fname, ss)

def generate_shading(dir_data, names, dir_target, prefix='gray_', create_shading=create_shading):
    ii = 0
    while ii < len(names['c']):
        obj = dirname(names['c'][ii])
        print obj
        dir_obj = join(dir_target, obj)
        print 'original'
        oimg = load_images(dir_data, names, ii)
        cc = oimg['r'] * oimg['s']
        alpha = (oimg['m'] * cc * oimg['c']).sum() / (oimg['m'] * cc * cc).sum()
        s = create_shading(oimg, alpha)
        s /= s.max()
        imsave(join(dir_obj, prefix + 'shading.png'), s)
        ii += 1
        for i in xrange(IM_PER_OBJ-1):
            print 'light%02d' % (i + 1)
            img = load_images(dir_data, names, ii)
            ii += 1
            ss = create_shading(img, alpha)
            ss /= ss.max()
            imsave(join(dir_obj, prefix + 'shading%02d.png' % (i + 1)), ss)

generate_shading(dir_data_mit, names, dir_data_shading, prefix='gray_', create_shading=create_shading)

# Create source files
srcs = ['%s/source_%s_s.txt' % (args.dir_data, k) for k in ['full', 'train', 'test']]
def convert_shading_source(src, prefix, postfix):
    names = load_source(src)
    i = 0
    while len(names) > i:
        obj = dirname(names[i])
        for j in xrange(IM_PER_OBJ):
            if j == 0:
                names[i] = join(obj, prefix + 'shading.png')
            else:
                names[i] = join(obj, prefix + 'shading%02d.png' % j)
            i += 1
    csv.writer(open(src.replace('_s.txt', postfix), 'w')).writerows(map(lambda x: [x], names))

for src in srcs:
    print src
    convert_shading_source(src, 'gray_', '_sg.txt')
    # convert_shading_source(src, 'color_', '_sc.txt')
    # convert_shading_source(src, 'median_', '_sm.txt')


