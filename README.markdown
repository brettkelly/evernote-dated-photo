## Overview

For a long time, I've wanted to add photos taken with my digital camera to Evernote and have the Created date of the note match the date the photo was taken. This application, when a file or folder is dropped onto it, will read the EXIF data of the image, create a new note in Evernote containing the image and if present, set the created date on the note to the date read from the image's EXIF data.

This simple application consists of an AppleScript droplet and a Python script (which depends on EXIF.py, a third-party Python library used to retrieve EXIF data from digital camera image files.

### Requirements

* Python 2.6 or later

### Installation

Grab all of the files in this repo and save them somewhere, then drag EvernoteDatedPhoto.app to your Dock (thereby creating an alias that can receive dropped files)

**Note**: By default, this application will add any dragged images to your _default_ notebook in Evernote. If you'd like to be prompted to choose the notebook where your images will be added, you'll need to modify the useDefaultNotebook property at the top of the AppleScript document to be true instead of false.

### Usage

Drag any number of image files or a folder of image files onto the droplet and they will be added to your Evernote account. If the image's EXIF data contains the "EXIF DateTimeOriginal" value, this value will be used as the Evernote note's created date.

### Misc.

* Tags are not currently supported

I'd like to add these things, but I seriously doubt it will happen anytime soon. So, if you want to hack on this, fork away and send me a pull request for any cool stuff you do.
