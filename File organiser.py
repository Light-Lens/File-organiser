# File organizer
# These imports will be used for this project
import sys
import os

# Initilazing File organizer
os.system('title File organizer')
os.chdir(sys.argv[1])

Content = os.listdir() # Listing all the content exist in the current folder.

# This function will organize all the files.
def Organizer(files, extention, dir_name):
	if files.endswith(extention):
		List = os.path.isdir(dir_name)
		if List == True:
			os.system(f'move \"{files}\" {dir_name}\\\"{files}\"')

		else:
			os.system(f'mkdir {dir_name}')
			os.system(f'move \"{files}\" {dir_name}\\\"{files}\"')

# Organizing the files.
for File in Content:
	Organizer(File, ".mp3", "Music") # This will Organize all Music files
	Organizer(File, ".mp4", "Videos") # This will Organize all Video files

	# This will Organize all Documents
	Organizer(File, ".txt", "Docs")
	Organizer(File, ".pdf", "Docs")
	Organizer(File, ".docx", "Docs")
	Organizer(File, ".xlsx", "Docs")

	# This will Organize all Pictures
	Organizer(File, ".png", "Photos")
	Organizer(File, ".jpg", "Photos")

sys.exit() # Exiting the program successfully
