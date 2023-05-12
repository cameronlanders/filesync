import sys
import os
# --------------------------------------------------------------
# log.py - version 1.0.8 - June 16, 2022
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
# included in every copy you distribute that contains the 
# program in whole or in part, even if you modify the 
# accompanying code. 
# - Any such modification must be accompanied by a statement 
# indicating it has been modified from this original version. 
# --------------------------------------------------------------
# Purpose:
# --------------------------------------------------------------
# This module logs the message specified in argv[1] to a date 
# stamped file in the directory from which it was called. 
# The program will append entries to an existing file if one 
# exists for the current date. If not, one will be created. 
# --------------------------------------------------------------
# Note:
# --------------------------------------------------------------
# The filename will be in the format: [datestamp]-reposync.log
# The script therefore generates a new log for each day that it 
# runs. To change the filename logic, modify the script below.
# --------------------------------------------------------------
# Parameters:
# --------------------------------------------------------------
# 1. msg: A string containing the message to be logged.
# 2. logtitle: A string contianing The title of the application 
# that is logging the message.
# --------------------------------------------------------------
# The logtitle parameter is used as part of the filename for 
# the log. This clarifies which application legged the data.
# --------------------------------------------------------------

msg = sys.argv[1]
msg = msg.replace(".. .",'...')
logtitle = sys.argv[2]

logdir = os.getcwd()
		
from datetime import datetime
datestamp = datetime.today().strftime('%Y-%m-%d')
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
with open('./' + datestamp + "-" + logtitle + '-log.txt', 'a') as f:
	f.write(timestamp + ' ' + msg)
	f.write('\n')
sys.exit(0)
