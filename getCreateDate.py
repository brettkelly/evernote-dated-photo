import EXIF
import sys
import os.path

def formatDate(date):
    "YYYY:MM:DD HH:MM:SS"
    d = date.split(' ')[0]
    y,m,d = d.split(':')
    return '%s/%s/%s' % (m,d,y[2:])

if sys.argv[1] and os.path.exists(sys.argv[1]):
    fd = open(sys.argv[1].strip(),'rb')
    tags = EXIF.process_file(fd)
    fd.close()
    if tags.has_key('EXIF DateTimeOriginal'):
        d = str(tags['EXIF DateTimeOriginal'])
        sys.stdout.write(formatDate(d))
