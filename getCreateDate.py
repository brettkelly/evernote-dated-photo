import sys
import os.path

def getDateStringFromFileName(fname):
    fname = os.path.split(fname)[1]
    fname = fname.replace("liked_","")
    try:
        p = fname.split('_') # remove trailing ID
        if p[0]:
            y,m,d = p[0].split('-')
            return '%s/%s/%s' % (m,d,y[2:]) # format and return date
    except Exception, e:
        # something went wrong; abort mission
        return str(e)

if sys.argv[1] and os.path.exists(sys.argv[1]):
    datestr = getDateStringFromFileName(sys.argv[1])
    sys.stdout.write(datestr)