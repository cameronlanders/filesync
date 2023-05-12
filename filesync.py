import subprocess
import sys
import os
import time
import datetime
import shutil

# --------------------------------------------------------------
# filesync
# --------------------------------------------------------------
# Recursively copies files between source and destination 
# folder sets specified in the parametwra.
# --------------------------------------------------------------
# Developed using Python 3.7.1
# --------------------------------------------------------------
# Author: Cameron Landers
# --------------------------------------------------------------
# Cameron's LinkedIN profile: 
# https://www.linkedin.com/in/cameronlandersexperience/
# 
# Cameron's Web Site:
# https://conversiondynamics.com
# --------------------------------------------------------------
# LICENSE: Free and Open Source with the following restrictions. 
# --------------------------------------------------------------
# All files within this distribution, hereinafter referenced as 
# "the program" are free to use, modify and include in your own 
# programs, whether for personal or commercial use. The only 
# restrictions are as follows: 
# - Everything above and including this license section must be 
#   included in every copy you distribute that contains the 
#   program in whole or in part, even if you modify the 
#   accompanying code. 
# - Any such modification must be accompanied by a statement 
#   indicating it has been modified from this original version. 
# --------------------------------------------------------------
# Usage Example:
# --------------------------------------------------------------
# filesync sourcepath destinationpath
# 
# Where: 
# sourcepath is the source directory from which copies will be 
# made. Files in the source path will not be changed.
# destinationpath is the destination directory to which want to 
# synchronize the file structure. 
# 
# --------------------------------------------------------------
# Important Note:
# --------------------------------------------------------------
# This app does not look at file dates or sizes. It just does 
# a recursive copy of the source directory structure.
#  
# All subfolders and files found under the source directory will 
# be copied to the destination. Any files by the same name that 
# already exist in the destination will be overwritten.
#
# It is therefore assumed the source path you specify contains 
# the master copy of the files that you want to back up.
# --------------------------------------------------------------
# Global variables
# --------------------------------------------------------------
src = sys.argv[1]
dest = sys.argv[2]
apptitle = "filesync"
logdir = os.getcwd()
logpath = logdir + "\\log.exe"
logdrive = logdir[0:2]
totalfiles = 0
totalfolders = 0
dirlist = []
processedlist = []

# --------------------------------------------------------------
# Start a log entry.
# --------------------------------------------------------------
subprocess.call([logpath, "=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=", apptitle])
subprocess.call([logpath, "                 FILESYNC                      ", apptitle])
subprocess.call([logpath, "=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=", apptitle])
subprocess.call([logpath, "         Developed in Python 3.7.1             ", apptitle])
subprocess.call([logpath, "            By: Cameron Landers                ", apptitle])
subprocess.call([logpath, "=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=", apptitle])
subprocess.call([logpath, "                BEGIN RUN...                   ", apptitle])
subprocess.call([logpath, "-----------------------------------------------", apptitle])

msg="[inf] Processing source: " + src + " to destination: " + dest
subprocess.call([logpath, "-----------------------------------------------", apptitle])
msg="[inf] Processing source: " + src + " to destination: " + dest
subprocess.call([logpath, "-----------------------------------------------", apptitle])
subprocess.call([logpath, msg, apptitle])

def get_modified_time(path):
	ti_m = os.path.getmtime(path)
	return time.ctime(ti_m)

def get_file_size(path):
	return os.path.getsize(path)


def syncfile(srcfile, dest):
	try:
		status = shutil.copy2(srcfile, dest)
		msg="[copied]: " + status
		subprocess.call([logpath, msg, apptitle])
		subprocess.call([logpath, "-----------------------------------------------", apptitle])
	except Exception as inst:
		# Log exceptions
		msg="[Exception] (syncfile): " + str(type(inst))
	

def processDir(src, dest):
	try:

		# ---------------------------------------------------------- 
		# Iterates through the files in the specified directory and 
		# calls syncfile to copy each file to the destination. 
		# ---------------------------------------------------------- 
		global totalfiles
		global totalfolders
		# ----------------------------------------------------------
		# Log each directory processed
		# ----------------------------------------------------------
		msg="[processing] " + src
		subprocess.call([logpath, msg, apptitle])

		# ----------------------------------------------------------
		# Create the root of the src in the destination if it 
		# doesn't already exist.
		# ----------------------------------------------------------
		if not os.path.exists(dest):
			os.mkdir(dest)

		for filename in os.listdir(src):
			f = os.path.join(src, filename)
			# ------------------------------------------------------
			# Check if it is a file
			# ------------------------------------------------------
			if os.path.isfile(f):
				# --------------------------------------------------
				# Increment the file counter.
				# --------------------------------------------------
				totalfiles += 1
				# --------------------------------------------------
				# Process the file.
				# --------------------------------------------------
				targetfile = os.path.join(dest, filename)

				if os.path.exists(targetfile):
					msg="[info]: Target file exists: " + targetfile + ". Checking skip criteria."
					subprocess.call([logpath, msg, apptitle])
					# Check for skip criteria
					targettime = get_modified_time(targetfile) 
					sourcetime = get_modified_time(f)

					msg="[criteria]: Target File Time: " + targettime
					subprocess.call([logpath, msg, apptitle])
					msg="[criteria]: Source File Time: " + sourcetime
					subprocess.call([logpath, msg, apptitle])

					targetsize = get_file_size(targetfile) 
					sourcesize = get_file_size(f)

					msg="[criteria]: Target File Size: " + str(targetsize) + " bytes."
					subprocess.call([logpath, msg, apptitle])
					msg="[criteria]: Source File Size: " + str(sourcesize) + " bytes."
					subprocess.call([logpath, msg, apptitle])
					# ------------------------------------------
					# If source and target timestamp and size 
					# are equal, we skip. 
					# If target is newer, we skip.
					# If source is newer, we overwrite target.
					# ------------------------------------------
					# We assume that if size is different, 
					# timestamp will also be different, in which 
					# case the above criteria prevails.
					# ------------------------------------------
					if sourcetime == targettime and sourcesize == targetsize:
						msg="[info]: Source and target are unchanged. Skipping."
						subprocess.call([logpath, msg, apptitle])
						# --------------------------------------
						# Timestamp and size are equal. Skip.
						# --------------------------------------
						continue
					elif sourcetime > targettime: 
						# --------------------------------------
						# Source is newer. Overwrite target.
						# --------------------------------------
						msg="[info]: Source is newer. Overwriting target."
						subprocess.call([logpath, msg, apptitle])
					elif sourcetime < targettime: 
						# --------------------------------------
						# Target is newer. Skip.
						# --------------------------------------
						msg="[info]: Target is newer. Skipping."
						subprocess.call([logpath, msg, apptitle])
						continue
					else:
						# --------------------------------------
						# Both times and sizes are different. 
						# Source wins. Overwrite target. 
						# --------------------------------------
						msg="[info]: Source and target size differs. Overwriting target."
						subprocess.call([logpath, msg, apptitle])
				syncfile(f, dest)
			else:
				# ----------------------------------------------
				# Increment the directory counter.
				# ----------------------------------------------
				totalfolders += 1
				# Add directory to list
				dirlist.append(f)

	except Exception as inst:
		# Log exceptions
		msg="[ERROR] (processDir):" + str(type(inst))
		subprocess.call([logpath, msg, apptitle])

def recursiveprocess():
	# ---------------------------------------------------------- 
	# Moves through the file system recursively, starting at
	# the destination path passed in the calling parameter.
	#
	# Processes all subdirectories and files to synchronize the 
	# destination with the source. 
	# 
	# IMPORTANT: Any files that already exist are overwritten. 
	# ---------------------------------------------------------- 
	try:
		if len(dirlist) > 0:
			for dir in dirlist:
				# ----------------------------------------------
				# Build the path for each new directory in 
				# the destination. 
				# ----------------------------------------------
				newdir = dir.replace(src, dest)
				# ----------------------------------------------
				# Skip folders already processed.
				# ----------------------------------------------
				if newdir in processedlist:
					continue

				# ----------------------------------------------
				# Create each folder in the destination
				# ----------------------------------------------
				if not os.path.exists(newdir):
					os.mkdir(newdir)
				# ----------------------------------------------
				# Process any files it may contain
				# ----------------------------------------------
				processDir(dir, newdir)
				# ----------------------------------------------
				# Add the new folder to the processed list
				# ----------------------------------------------
				processedlist.append(newdir)
				recursiveprocess()
	
	except Exception as inst:
		# ------------------------------------------------------
		# Log exceptions
		msg="[ERROR] (recursion):" + str(type(inst))
		subprocess.call([logpath, msg, apptitle])
		subprocess.call([logpath, "-----------------------------------------------", apptitle])
		print("ERROR in recursion: " + str(type(inst)))
		return

try:
	processDir(src, dest)
	recursiveprocess()
	# --------------------------------------------------------------
	# Close out the log.
	# --------------------------------------------------------------
	msg="Total Processed: " + str(totalfiles) + " files in " + str(totalfolders) + " folders."
	subprocess.call([logpath, msg, apptitle])
	print(msg)

except Exception as inst:
	# Log exceptions
	msg="[Exception] " + str(type(inst))
	subprocess.call([logpath, msg, apptitle])
	subprocess.call([logpath, "-----------------------------------------------", apptitle])
	print("ERROR in recursion: " + str(type(inst)))

