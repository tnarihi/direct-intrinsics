from __future__ import print_function

from glob import glob
from os.path import join, dirname, isdir
from os import makedirs

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--dir_data', default='.')

args = parser.parse_args()

train_objs = ['apple', 'box', 'cup1', 'dinosaur', 'frog1', 'panther', 'paper1', 'phone', 'squirrel', 'teabag2']
test_objs = ['cup2', 'deer', 'frog2', 'paper2', 'pear', 'potato', 'raccoon', 'sun', 'teabag1', 'turtle']

sources = sorted(glob(join(args.dir_data, 'source_full*.txt')))

if not isdir(join(args.dir_data, 'sources_barron')):
    makedirs(join(args.dir_data, 'sources_barron'))

for source in sources:
    source_train = source.replace('source_full', 'sources_barron/source_train')
    source_test = source.replace('source_full', 'sources_barron/source_test')
    print(source, '-->', source_train, source_test)
    paths = map(lambda x: x.strip(), open(source, 'r'))
    with open(source_train, 'w') as ftr, open(source_test, 'w') as fte:
        for p in paths:
            obj = dirname(p)
            if obj in train_objs:
                print(p, file=ftr)
            elif obj in test_objs:
                print(p, file=fte)
