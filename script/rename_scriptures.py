#!/usr/bin/env python3
import os
import shutil

SCRIPTURES_DIR = "../old_www/scriptures"
SCRIPTURES_OUT_DIR = "../www/studies/english/scriptures"

for filename in os.listdir(SCRIPTURES_DIR):
    old_name = os.path.join(SCRIPTURES_DIR, filename)
    new_filename = filename.replace("-", "_")
    new_name = os.path.join(SCRIPTURES_OUT_DIR, new_filename)
    shutil.copyfile(old_name, new_name)
