import os

def converter(filename, input_format, output_format, directory):
	try:
		path = ('{}/{}').format(directory, filename)
		input_file = ('\'{}.{}\'').format(path, input_format)
		output_file = ('\'{}.{}\'').format(path, output_format)
		command = ("ffmpeg -loglevel panic -i {} {}").format(input_file, output_file)
		os.popen(command)
		print('Το βίντεο μετατράπηκε με επιτυχία σε mp3. Τερματισμός προγράμματος.')
		return
	except:
		print('Κάτι πήγε στραβά στην μετατροπή σε mp3. Ξανατρέξτε το πρόγραμμα.')
		exit()
	

if __name__ == "__main__":
	converter()