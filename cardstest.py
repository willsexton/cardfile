#!/usr/bin/python
import sys, re, os, glob, csv, copy
from cards_regexp import *    

def get_card_records():

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
                    collection_match = regex_collection.match(line)
                    if collection_match:
                        card_record['collection'] = collection_match.group('collection').rstrip('\r\n')
                card_records.append(card_record)
            else:
                not_matched.append(fileContents)
                    
            #print ""
            
            fh.close()
                
            start_of_card = False
            end_of_card = False
    return (card_records, not_matched)


def write_data(card_records):

    out = open('cardrecords.csv', 'wb')
    csvwriter = csv.writer(out)
    csvwriter.writerow(['Author', 'Recipient', 'Collection', 'Filename', 'Date', 'Location'])
    
    for card in card_records:
        head = []
        for name in ['author_name','recipient_name', 'collection','filename']:
            if name in card:
                head.append(card[name])
            else:
                head.append('')
    
        for entry in card['dates']:
            row = copy.copy(head)
            for name in ['entry_date','location']:
                if name in entry:
                    row.append(entry[name])
                else:
                    row.append('')
            csvwriter.writerow(row)
    out.close()
    
if __name__ == '__main__':
    (card_records, unmatched) = get_card_records()
    for t in unmatched:
        print t[:10]
