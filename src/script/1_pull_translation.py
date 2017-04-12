import requests
import json
import os
import shutil, errno
from   requests import get

json_export = {'api_token' : '65bfe24ddca299ea8b490a5f96a89187', 
			   'id'        : '104375',
			   'language'  : 'uk',
			   'type'      : 'po'}

file_name = r'../../church-it/text.po'

src_root = "/home/dima/church-it/first_principles/0_template"
dst_root = "/home/dima/church-it/first_principles/1_template_with_translation"


def download(url, file_name):
	# open in binary mode
	with open(file_name, "wb") as file:
		# get request
		response = get(url)
		# write to file
		print(response.content)
		file.write(response.content)

def copyAnything(src_root, dst_root):
	if os.path.exists(dst_root):
		shutil.rmtree(dst_root)
	#os.mkdir(dst_root)
	try:
		shutil.copytree(src_root, dst_root)
	except OSError as exc: # python >2.5
		if exc.errno == errno.ENOTDIR:
			shutil.copy(src_root, dst_root)
		else: raise


r_export = requests.post('https://api.poeditor.com/v2/projects/export', data = json_export)
url      = r_export.json()['result']['url']

#download(url, file_name)
copyAnything(src_root, dst_root)