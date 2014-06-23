import glob
from lxml import etree

NSMAP = {
    'duke' : 'http://library.duke.edu/metadata/terms',
    'atom' : 'http://www.w3.org/2005/Atom',
}


filecount = 0
for folder in glob.glob('/Users/will/Data/cardfile/autograph/file_*'):
    fileglob = '{0}/*.txt'.format(folder)
    filecount += len(glob.glob(fileglob))
    

print filecount
entrycount = 0

for file in glob.glob('/Users/will/Data/cardfile/xml/autograph/*.xml'):
    root = etree.parse(file)
    entries = root.xpath('/atom:entry/atom:cardEntry', namespaces = NSMAP)
    entrycount += len(entries)
    print '{0}: {1}'.format(file, len(entries))
    
print entrycount
