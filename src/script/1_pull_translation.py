import requests
import json
import os
import shutil
import errno
from   requests import get

po_request = {'api_token' : '65bfe24ddca299ea8b490a5f96a89187', 
			   'id'        : '104375',
			   'language'  : 'uk',
			   'type'      : 'po'}

src_root 	 = "/home/dima/church-it/first_principles/0_template/"
dst_root 	 = "/home/dima/church-it/first_principles/1_template_with_translation/"


def download_from_poeditor(request):
	poeditor_export = requests.post('https://api.poeditor.com/v2/projects/export', request)
	url = poeditor_export.json()['result']['url']
	response = get(url)
	#print(response.content)
	return response.content

def copyFolder(src_root, dst_root):
	if os.path.exists(dst_root):
		shutil.rmtree(dst_root)
	shutil.copytree(src_root, dst_root)

copyFolder(src_root, dst_root)

os.mkdir(dst_root + "lang/ru/")
os.mkdir(dst_root + "lang/ru/LC_MESSAGES")

translation_po = download_from_poeditor(po_request)

po_file = open(dst_root + "lang/ru/LC_MESSAGES/text.po", "wb")
po_file.write(translation_po)
