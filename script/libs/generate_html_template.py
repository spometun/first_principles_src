#!/usr/bin/env python3
import os

ENCODING ="UTF-8"

def generateStudy(src_root, outstudies_path, study, is_build_mobile):
    generateFullHtml(src_root, outstudies_path, study, is_build_mobile, True)
    # Option when index has no header
    # generateFullHtml(src_root, outstudies_path, study, is_build_mobile, study.name != "0_index")
            

def generateFullHtml(src_root, outstudies_path, study, is_build_mobile, is_write_header):
	join = os.path.join

	studies_folder = join(src_root, "studies")
	header_filename = "header_mobile.html" if is_build_mobile else "header_web.html"
	header_file = open(join(studies_folder,  header_filename), "r", encoding=ENCODING)
	footer_file = open(join(studies_folder,  "footer.html"), "r", encoding=ENCODING)
	study_filename = join(studies_folder, "english", study.name + ".html")
	study_file = open(study_filename, "r", encoding=ENCODING)

	header = header_file.read()
	footer = footer_file.read()
	body = study_file.read()
	out_file = open(outstudies_path + "/" + study.name + ".html", "w", encoding=ENCODING)
	if is_write_header:
	    header = header.replace("study_title", "_(\"" + study.title + "\")")
	    header = header.replace("study_header", "_(\"" + study.title + "\")")
	    out_file.write(header)
	out_file.write(body)
	out_file.write(footer)

	header_file.close()
	footer_file.close()
	study_file.close()
	out_file.close()
