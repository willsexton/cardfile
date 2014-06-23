#!/usr/bin/python
import sys, re, os, glob
from lxml import etree

FILE_PATH = "/Volumes/Vol1/Data/Metadata/cards/file_001_a_albq_0001.txt"

#if not os.path.exists(FILE_PATH):
#    print "please mount the 'Vol1' drive."
#    sys.exit(2)
    
regex_author = re.compile("^(|(.+RAPH|.+raph|.+G[A-Z]APH|.+g[a-z]aph|AUTOGRAP[\"]*) [\"0-9A-z: ]*[\r\n]*)(?P<author_name>([\"'^&*.0-9A-Za-z\[\]-]+,?)( [\"'^&*.0-9A-Za-z\[\]-]+,?){1,})( \(.+[\)]*)*[ \n\r]*(Petition )*(To|to) (?P<recipient_name>.*)[\n\r]")
regex_author_fmt2 = re.compile("^(|(.+RAPH|.+raph) [\"0-9A-z: ]*[\r\n]*)(?P<author_name>([\"'^&*.0-9A-Za-z\[\]-]+,?)([\"'^&*.0-9A-Za-z\[\]-]+,?){1,})( \(.+[\)]*)*[ \n\r]*(Petition )*(To|to) (?P<recipient_name>.*)[\n\r]")
regex_author_fmt3 = re.compile("^([A-z0-9,.'\"]+\s[\n\r]?)+[\n\r]{2,}To (.*)")
regex_fmt2 = re.compile("^(|(.+TOGRAPH|.+tograph) [0-9A-z: ]*[\r\n]*)(?P<author_name>[\"'^&*.\d\w\[\]\(\)-]+,?]+)[\n\r]+(Petition )?(To|to) (?P<recipient_name>.*)[\n\r]")
regex_author_2 = re.compile("^(?P<author_name>([\"'^&*.0-9A-Za-z\[\]-]+)([,]* [\"'^&*.0-9A-Za-z\[\]-]+){1,}) (WORKS|works|Works)")
regex_fmt3 = re.compile("^(?P<author_name>([\"'^&*.0-9A-Za-z\[\]-]+)([,]* [\"'^&*.0-9A-Za-z\[\]-]+){1,})[ \n\r]*(Statement|STATEMENT|Note|NOTE|Receipt|RECEIPT|Report|REPORT)")
regex_author_works_2 = re.compile("^(WORKS|Works|works|MICROFILM|Microfilm)\s*(?P<author_name>([\"'^&*.0-9A-Za-z\[\]-]+)(,{0,1} [ \"'^&*.0-9A-Za-z\[\]-]+){1,})( \(.+\))*")
regex_author_seealso = re.compile("^(?P<author_name>([\"'^&*.0-9A-Za-z\[\]-]+)([,]* [\"'^&*.0-9A-Za-z\[\]-]+){1,})[ \n\r]+(See(| Also| also)) (?P<see_also_name>.*)")
regex_end = re.compile("^[\d]{1,2}-[\d]{1,2}-[\d]{1,2}.*$")
regex_mss = re.compile("^.+(MSS).*")

regex_date_fmt1 = re.compile("(?P<entry_date>(\d{4}, (Jan|Feb|Mar(|ch)|Apr|May|Jun|Jul(|y)|Aug|Sep(|t)|Oct|Nov|Dec).*([\d]{1,2})) (?P<location>.*))")
regex_date_fmt2 = re.compile("(\d{1,2}-\d{1,2}-\d{2,4})")
regex_date_fmt3 = re.compile("(?P<entry_date>(\d{4}\. (January|February|March|April|May|June|July|August|September|October|November|December) ([\d]{1,2}))\. (?P<location>.*))")

start_of_card = False
end_of_card = False

file_count = 0
matches = 0
not_matched = []
card_records = []

for folder in glob.glob('/Users/will/Data/cardfile/autograph/file_*'):
    folderid = folder[folder.rfind('/')+1:]
    fileglob = '{0}/*.txt'.format(folder)
    for dirent in glob.glob(fileglob):
        file_count += 1
        fh = open(dirent, 'r')
        slug, fname = os.path.split(dirent)
        
        fileContents = file(dirent).read()
        match = regex_author.match(fileContents)
        match_author_fmt2 = regex_author_fmt2.match(fileContents)
        match_author_fmt3 = regex_author_fmt3.match(fileContents)
        match_fmt2 = regex_fmt2.match(fileContents)
        match_fmt3 = regex_fmt3.match(fileContents)
        match2 = regex_author_2.match(fileContents)
        match_seealso = regex_author_seealso.match(fileContents)
        match_works2 = regex_author_works_2.match(fileContents)
        
        card_record = {}
        card_matched = False
        for m in [match, match_author_fmt2, match_author_fmt3, match2, match_fmt3, match_seealso, match_works2]:
            if m:
                card_matched = True
                matches += 1
                #sys.stdout.write(fname + ": ")
                try:
                    #sys.stdout.write(" %s" % m.group('author_name'))
                    card_record['author_name'] = m.group('author_name').rstrip('\n\r')
                except:
                    pass
                    
                try:
                    #sys.stdout.write("  %s" % m.group('recipient_name'))
                    card_record['recipient_name'] = m.group('recipient_name').rstrip('\n\r')
                except:
                    pass
                    
                #sys.stdout.write("\n")
                break
                
        if card_matched:
            pathslug, afilename = os.path.split(dirent)
            card_record['filename'] = afilename
            card_record['dates'] = []
            for line in fh:
                date_match_fmt1 = regex_date_fmt1.match(line)
                date_match_fmt2 = regex_date_fmt2.match(line)
                date_match_fmt3 = regex_date_fmt3.match(line)
                if date_match_fmt1 or date_match_fmt2 or date_match_fmt3:
                    #sys.stdout.write("Date Matched: ")
                    for m in [date_match_fmt1, date_match_fmt3]:
                        if m:
                            entry_date = m.group('entry_date').rstrip('\r\n')
                            location = m.group('location').rstrip('\r\n')
                            date_match_rec = {'entry_date': entry_date, 'location': location}
                            card_record['dates'].append(date_match_rec)
                            #print m.group(0)
                            break
                            
            card_records.append(card_record)
        else:
            not_matched.append(dirent)
                
        #print ""
        
        fh.close()
            
        start_of_card = False
        end_of_card = False
        
    # print not_matched to screen
    #for n in not_matched:
    #    print n
        
    # print card_records to screen    
    #for c in card_records:
    #    print c
    
    DMR_NSMAP = {
        'rdf' : 'http://www.w3.org/1999/02/22-rdf-syntax-ns#',
        'dcterms' : 'http://purl.org/dc/terms',
        'duke' : 'http://library.duke.edu/metadata/terms',
    }
    NSMAP1 = {
        'duke' : 'http://library.duke.edu/metadata/terms',
        '' : 'http://www.w3.org/2005/Atom',
    }
    entry = etree.Element('entry', nsmap={'duke':DMR_NSMAP['duke']})
    entry.set('xmlns','http://www.w3.org/2005/Atom')
    for c in card_records:
        card_entry = etree.SubElement(entry, 'cardEntry', filename=c['filename'])
        author = etree.SubElement(card_entry, "author")
        try:
            author.text = c["author_name"]
        except:
            pass
        
        recipient = etree.SubElement(card_entry, "recipient")
        try:
            recipient.text = c["recipient_name"]
        except:
            pass
            
        if len(c['dates']):
            dateEntries = etree.SubElement(card_entry, 'dateEntries')
            for d in c['dates']:
                try:
                    dateEntry = etree.SubElement(dateEntries, 'date')
                    dateEntry.text = d['entry_date'].rstrip('\r\n\f').encode('utf-8')
                except UnicodeDecodeError:
                    print "'  %s  '" % d['entry_date']
                    
                try:
                    locationEntry = etree.SubElement(dateEntries, 'location')
                    locationEntry.text = d['location'].rstrip('\r\n\f').decode('utf-8')
                except:
                    pass
        
    out = open('/Users/will/Data/cardfile/xml/autograph/{0}.xml'.format(folderid), 'w')
    out.write(etree.tostring(entry, pretty_print=True))
    out.close()

        
