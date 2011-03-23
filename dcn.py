#!/usr/bin/env python
from desktopcouch.records.server import CouchDatabase
from desktopcouch.records.record import Record
import os
import sys

dbname = 'dcn_'+str(os.getuid())
try:
	db = CouchDatabase(str(dbname), create=True)
except Exception:
	raise
'''else:
	print 'Database created.'''

def func(param, param2):
	record_type = 'http://example.com/fetch-record-type.html'
	if param == '-i':
		if param2 != '':
			new_row = Record({'row':str(param2)}, record_type)
			try:
				db.put_record(new_row)
			except Exception:
				raise
			else:
				print 'New row created.'
		else:
			row = raw_input('Insert text here:  ')
			new_row = Record({'row':str(row)}, record_type)
			try:
				db.put_record(new_row)
			except Exception:
				raise
			else:
				print 'New row created.'

	elif param == '-d':
		print 'brisanje'

	elif param == '-l':
		results = db.get_records(record_type = record_type, create_view = True)
		for records in results:
			record = records.value
			print record

if __name__ == '__main__':
	if len(sys.argv) == 1:
		print 'usage: '+sys.argv[0]+' [OPTION]'
		print '    -i: insert new row'
		print '    -l: list rows'
		print '    -d: delete row\n'
	else:
		if sys.argv[1] == '-i':
			if len(sys.argv) == 3:
				func(str(sys.argv[1]),str(sys.argv[2]))
			elif len(sys.argv) == 2:
				func(str(sys.argv[1]),'')
			else:
				print '-i option accepts either no parameters or a single parameter.\n'
		elif sys.argv[1] == '-d':
			func(str(sys.argv[1]),str(sys.argv[2]))
		elif sys.argv[1] == '-l':
			func(str(sys.argv[1]),'')
		else:
			os.system('./dcn.py')
