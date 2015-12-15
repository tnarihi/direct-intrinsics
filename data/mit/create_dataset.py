from glob import glob
import os, csv
from os.path import join, basename, dirname

import cv2

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--dir_data', default='.')

args = parser.parse_args()

csvs = {}
for t in ['full', 'train', 'test']:
    for k in ['', '_r', '_s', '_m', '_m_s']:
        csvs[t + k] = csv.writer(open(join(args.dir_data, 'source_%s.txt' % (t + k)), 'w'))

def to_label(images, label='reflectance'):
    return map(lambda x: [join(dirname(x[0]), label + '.png')], images)

paths = sorted(glob(join(args.dir_data, 'data/*')))

for i, p in enumerate(paths):
    # create mask0
    pm = join(p, 'mask.png')
    img = cv2.imread(pm)
    img[...] = 0
    cv2.imwrite(join(p, 'mask0.png'), img)

    sub = 'train' if i % 2 else 'test'
    images = sorted(glob(join(p, 'diffuse.png')) + glob(join(p, 'light*.png')))
    images = map(lambda x: [join(basename(p), basename(x))], images)
    shadings = ['mask.png'] + ['mask0.png' for jj in xrange(len(images) - 1)]
    shadings = map(lambda x: [join(basename(p), x)], shadings)
    csvs['full'].writerows(images)
    csvs[sub].writerows(images)
    csvs['full_m_s'].writerows(shadings)
    csvs[sub + '_m_s'].writerows(shadings)
    for k, kk in [('_r', 'reflectance'), ('_s', 'shading'), ('_m', 'mask')]:
        csvs['full' + k].writerows(to_label(images, kk))
        csvs[sub + k].writerows(to_label(images, kk))
