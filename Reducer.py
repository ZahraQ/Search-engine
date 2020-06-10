#Groups the documents ids where words appear

#!/usr/bin/python2.6
from __future__ import print_function
import sys
import re


def main():
	last_word = None
	last_list_id = None
	lists = []
	for line in sys.stdin:
		
		

		word, list_id = line.split('\t')

		if last_word == word and last_list_id != list_id:
			lists.append(last_list_id)
			last_list_id = list_id
			
		else:

			if last_word != word:
				lists.append(last_list_id)
				#print(word,"\t", lists, "\n")
				print(word.strip(),end=':')
				print(",".join((str(elt)).strip() for elt in lists),end="\n")
				del lists[:]
			last_word = word
			last_list_id = list_id
	

if __name__ == '__main__':
	main()
			
