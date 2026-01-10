# from distutils.dir_util import copy_tree
from shutil import copytree
src = 'CSV'
dst = 'copy of data'


copytree(src, dst, dirs_exist_ok=True)

print('\nData copied\n')