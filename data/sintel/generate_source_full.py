from __future__ import print_function
from os.path import join, isfile, exists
import subprocess
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('dir_source')
args = parser.parse_args()

elems = ['albedo_defect_mask_s', 'albedo_defect_mask', 'albedo', 'clean', 'shading', 'RS', 'gray_shading', 'RGS']
for elem in elems:
    src_tr = join(args.dir_source, 'source_{}_{}.txt'.format(elem, 'train'))
    src_te = join(args.dir_source, 'source_{}_{}.txt'.format(elem, 'test'))
    src_fu = join(args.dir_source, 'source_{}_{}.txt'.format(elem, 'full'))
    if not isfile(src_tr):
        print(src_tr, "doesn't exist.")
        continue
    elif not isfile(src_te):
        print(src_te, "doesn't exist.")
        continue
    elif exists(src_fu):
        print(src_fu, "already exists.")
        continue
    print(src_tr, src_te, '-->', src_fu)
    subprocess.call('cat {} {} >> {}'.format(src_tr, src_te, src_fu), shell=True)
