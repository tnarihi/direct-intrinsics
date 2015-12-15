from __future__ import print_function

from glob import glob
from os.path import join, dirname, isdir
from os import makedirs
from six.moves import range
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--dir_sintel', default='.')
parser.add_argument('--dir_mit', default='../MIT-intrinsic')
parser.add_argument('--dir_target', default='./sources_18_barron_mit2_sintel_balance')
parser.add_argument('--balance', action='store_true')
args = parser.parse_args()

dir_src_sintel = join(args.dir_sintel, 'sources_18_mask')
dir_src_mit = join(args.dir_mit, 'sources_barron')
if not isdir(args.dir_target):
    makedirs(args.dir_target)

corres = [
    ('clean_{}', '{}', 'clean_{}'),
    ('RS_{}', '{}', 'RS_{}'),
    ('albedo_{}', '{}_r', 'albedo_{}'),
    ('shading_{}', '{}_sg', 'shading_{}'),
    ('albedo_defect_mask_{}', '{}_m', 'albedo_defect_mask_{}'),
    ('albedo_defect_mask_{}', '{}_m', 'albedo_defect_mask_s_{}'),  # mask_s
    ]

for s, m, t in corres:
    for v in ('train', 'test'):
        ss = 'source_{}.txt'.format(s.format(v))
        mm = 'source_{}.txt'.format(m.format(v))
        tt = 'source_{}.txt'.format(t.format(v))
        ss
        print(ss, mm, '-->', tt)
        with open(join(args.dir_target, tt), 'w') as fd:
            print(open(join(dir_src_sintel, ss)).read(), end='', file=fd)
            for i in range(4):
                print(open(join(dir_src_mit, mm)).read(), end='', file=fd)            
