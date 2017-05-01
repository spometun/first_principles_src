
def generateStudy(src_root, outstudies_path, study_name, study_title):
    generateFullHtml(src_root, outstudies_path, study_name, study_title, True)

def generateIndex(src_root, outstudies_path):
    generateFullHtml(src_root, outstudies_path, "index", "", False)

def generateFullHtml(src_root, outstudies_path, study_name, study_title, is_write_header):
	
	header_file = open(src_root + "/header.html", "r") 
	footer_file = open(src_root + "/footer.html", "r")
	study_file = open(src_root + "/studies/english/" + study_name + ".html")

	header = header_file.read()
	footer = footer_file.read()
	study = study_file.read()

	out_file = open(outstudies_path + "/" + study_name + ".html", "w")
	if is_write_header:
            header = header.replace("study_title", "_(\"" + study_title + "\")")
            header = header.replace("study_header", "_(\"" + study_title + "\")")
            out_file.write(header)
	out_file.write(study)
	out_file.write(footer)

	header_file.close()
	footer_file.close()
	study_file.close()
	out_file.close()
