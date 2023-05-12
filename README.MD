# Filesync 
## A program for easy file and folder structure synchronization.

**Developed in Python 3.7.1 by Cameron Landers**

### License:

Free and Open Source. This program is free to use, copy and modify anyway you choose, whether for personal or commercial use, as long as one simple requirement is honored. Please see the license information contained in the code itself for this explicit requirement that allows copying, modification and redistribution. There aren't many restrictions. Please understand and accommodate the few we do have.

**Prerequisites:**

* Python version 3.7.1 or later is required for successful deployment.
* This version of the code is designed to be installed on Windows. However, UNC paths are supported for source and destination folders so you can easily use this tool to synchronize folder sets across other operating systems, such as Unix, Linux or Macos. 
* Synchronizing has been successfully tested between filesets on Windows and several Linux distributions as of this writing. 

## Installation

### Step 1:
* Choose a folder where you want to store the program on your local machine. 

### Step 2:
* Change to the above folder in a command prompt (or Powershell) and execute the following two commands:

* `pyinstaller --onefile filesync.py`
* `pyinstaller --onefile log.py`

**What these commands do:**

* The first command compiles the mian program (filesync.py) to an executable.
* The second command does the same for the logging utility (log.py).

### Step 3:

Change into the `dist` folder that was created during compilation. Copy the two executables (`filesync.exe` and `log.exe`) to the parent directory where you started.

Filesync is now installed. To use it, follow these simple guidelines:

**Syntax:**

`filesync source-path destination-path`

**Where:**

* `source-path` is the directory that contains the files and folders you want to backup.
* `destination` path is the destination directory to which you want the data copied.

**Examples:**

`filesync c:\dev\mystuff \\myserver\backups`

As you can see, UNC paths are fully supported, so for example on Windows, you don't have to map a drive just to do backups. 

The above command  will copy all files and subdirectories contained within `c:\dev\mystuff` to `\\myserver\backups`. The toperation is recursive, so no matter how deep the source directory structure is, all files and subdirectories will be copied exactly as they are, mirroring the directory structure at the destination location.

Note that alternately you might type:

`filesync c:\dev\mystuff \\myserver\backups\mystuff`

This would create the root folder (`mystuff`) in the destination, and everything would be placed under that, just as it is in your source directory structure. It's all up to you!

**Overwrite Criteria:**

When (and _only_ when) a given file already exists in the destination location, the overwrite policy comes into play. The overarching rule is that the file in thre source location generally takes precedence. 

Here's the complete overwrite logic:

1. When the source and target files have the same modified date and timestamp, the file will be skipped.
2. When the source file is newer than the target, the source file will overwrite the target.
3. When the source file is older than the target, the file will be skipped. Newer files will not be overwritten. 

**About File Size Differences:**

The above rules apply regardless of file size. The program assumes that if the file sizes are different, the timestamps must also be different, in which case the timestamnp rules are all that is needed. 

**More Information**

In other words, timestamps take precedence over file size. It is assumed that you cannot have two versions of a file with different sizes if they also have the same modification timestamp. This is because changing the file will always update the timestamp.

* Remember that the first parameter you specify on the command line is the "source" file structure and the second parameter is the target. Files in the source location will "win" when the source timestamp is newer than the target file's timestamp. 
* On the other hand, if the target file's timestamp is newer, the file will be skipped to avoid overwriting the newer file.

You should always specify the location of the file set you consider to be your "master" or "working" file set as the first parameter, so that it will overwrite files in the target, which are the files presumed to be a potentially stale backup.

If you want full, 2-way synchronazation between both filesets, you can modify the script to easily implement that. It is a trivial change, so feel free to do so if that's the behavior you want. Personally, I don't like to change files manually in both the working fileset and the backups. 

My rule of thumb is, make changes in only one working fileset and back that up to the others. That way I always know which location is current and which is potentially stale. It also makes things much easier to automate. I use scheduled tasks to call  this program on a nighly basis.

One reasom you might consider full synchronization is when you work with a group of people who modify different copies of the same files at different locations. This shared use case requires a more advanced synchronization model, so you'll need to decide how to manage potential conflicts in such a model. 

Please consider emailing me from my web site and let me know if you found Filesync useful for your scenario. I would love to hear your comments!

Here's the link:
https://conversiondynamics.com


Cheers,

-=Cameron

