import glob

CARDS_BASE_DIR = '/Users/will/Data/cardfile/text'

filelist = []
last_filelist_len = len(filelist)
for folder in glob.glob('/Users/will/Data/cardfile/autograph/file_*'):
    folderid = folder[folder.rfind('/')+1:]
    filelist.extend(glob.glob('{0}/*.txt'.format(folder)))
    print len(filelist) - last_filelist_len
    last_filelist_len = len(filelist)

for f in filelist:
    fh = open(f)
    t = fh.read()
    fh.close()
    print t[:10]
