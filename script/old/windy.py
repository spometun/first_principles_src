#!/usr/bin/env python3
"""
  windy - what is not done yet
"""

import os

ROOT = ".."

def listdir_html(dirname):
    return set([f for f in os.listdir(dirname) if f.endswith(".html")])

old_www_files = listdir_html(os.path.join(ROOT, "old_www"))
www_files = listdir_html(os.path.join(ROOT, "www/studies/english"))

for f in old_www_files - www_files:
    print(f)
