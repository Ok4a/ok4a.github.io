from distutils.dir_util import copy_tree
src = 'CSV'
dst = 'copy of data'

copy_tree(src, dst)

print('\nData copyed\n')