#!/usr/bin/env python3
import os

def generateStudy(src_root, outstudies_path, study):
    generateFullHtml(src_root, outstudies_path, study, True)
    # Option when index has no header
    # generateFullHtml(src_root, outstudies_path, study, study.name != "0_index")
            

def generateFullHtml(src_root, outstudies_path, study, is_write_header):
	join = os.path.join

	studies_folder = join(src_root, "studies")
	header_file = open(join(studies_folder,  "header.html"), "r")
	footer_file = open(join(studies_folder,  "footer.html"), "r")
	study_filename = study.name + ".html"
	study_file = open(join(studies_folder, "english", study_filename))

	header = header_file.read()
	footer = footer_file.read()
	body = study_file.read()
	out_file = open(outstudies_path + "/" + study.name + ".html", "w")
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
