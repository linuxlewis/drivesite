from drivesite.drive import DriveAgent

import os

# virtual sites
sites = [{'folder_id':'', 'name':'thetaxigs.org'}]

# get build
build = DriveAgent.get_build()


for site in sites:
	print 'Syncing %s...' % site['name'] 
	# get folder
	folder = build.files().get(fileId=site['folder_id']).execute()




def drive_walk(file, path):
	# check if path exists
	if not os.path.exists(path):
		# if not create folder
		os.mkdirs(path)

	# if file is folder
	#if file[]

		# return map drive_walk children, path + foldername

	# else

		# write file
