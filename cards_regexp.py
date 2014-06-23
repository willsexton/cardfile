import re

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

regex_date_fmt1 = re.compile("(?P<entry_date>(\d{4}, (Jan|Feb|Mar(|ch)|Apr|May|Jun|Jul(|y)|Aug|Sep(|t)|Oct|Nov|Dec).*([\d]{1,2}))) (?P<location>.*)")
regex_date_fmt2 = re.compile("(\d{1,2}-\d{1,2}-\d{2,4})")
regex_date_fmt3 = re.compile("(?P<entry_date>(\d{4}\. (January|February|March|April|May|June|July|August|September|October|November|December) ([\d]{1,2})))\. (?P<location>.*)")

regex_collection = re.compile("(?P<collection>.+ MSS\.)")

