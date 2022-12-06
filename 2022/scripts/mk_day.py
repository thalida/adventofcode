import shutil
import pathlib
import os
import sys

source_dir = pathlib.Path(os.path.dirname(sys.argv[0]), './templates/day')
dest_dir = pathlib.Path(os.path.dirname(sys.argv[0]), f'../day-{sys.argv[1]}')
shutil.copytree(source_dir, dest_dir)
