def generateFullHtml(src_root, dst_root, study_name, is_write_header = True):
	
	header_file = open(src_root + "/header.html", "r") 
	footer_file = open(src_root + "/footer.html", "r")
	study_file = open(src_root + "/studies/" + study_name + ".html")

	header = header_file.read()
	footer = footer_file.read()
	study = study_file.read()

	out_file = open(dst_root + "/studies/" + study_name + ".html", "w")
	if is_write_header:
		out_file.write(header)
	out_file.write(study)
	out_file.write(footer)

	header_file.close()
	footer_file.close()
	study_file.close()
	out_file.close()
