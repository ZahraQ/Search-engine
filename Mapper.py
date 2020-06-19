#Extract words and where they appear

#!/usr/bin/python2.6
import json
import sys
import re

pattern = re.compile("[A-Za-z][0-9A-Za-z]*")
for line in sys.stdin:
	
	recordline = json.loads(line)

	document_id = recordline[0]
	text = recordline[1]

	for word in pattern.findall(line):

		print word.lower(),"\t", document_id
	
