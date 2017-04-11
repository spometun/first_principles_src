def generateFullHtml(study_name):
	header_path = "../data/header.html"
	footer_path = "../data/footer.html"
	study_path = "../data/studies/" + study_name + ".html"
	out_path = "../../0_template/studies/" + study_name + ".html"
	
	header_file = open(header_path, "r") 
	footer_file = open(footer_path, "r")
	study_file = open(study_path)

	header = header_file.read()
	footer = footer_file.read()
	study = study_file.read()

	out_file = open(out_path, "w")
	out_file.write(header)
	out_file.write(study)
	out_file.write(footer)

	header_file.close()
	footer_file.close()
	study_file.close()
	out_file.close()
