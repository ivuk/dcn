#!/usr/bin/env python
from desktopcouch.records.server import CouchDatabase
from desktopcouch.records.record import Record
import os
import sys
from uuid import uuid4

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
            new_row = Record({'_id': uuid4().hex,'data':str(param2)}, record_type)
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
        if param2 != '':
            print 'brisanje'
        else:
            func('-l','')
            dvar = raw_input('Which record do you want to delete: ')
            print dvar
    elif param == '-l':
        results = db.get_records(record_type = record_type, create_view = True)
        for records in results:
            record = records.value
            print record

class base:
# base.record_type
    record_type = 'http://example.com/fetch-record-type.html'
# base.insert
    def insert(self, param):
        return True
# base.delete
    def delete(self):
        return True
# base.list
    def list(self, param):
        return True
# konstruktor
def __init__(self):
    self.data = []

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
                        if len(sys.argv) == 3:
                                func(str(sys.argv[1]),str(sys.argv[2]))
                        elif len(sys.argv) == 2:
                                func(str(sys.argv[1]),'')
                        else:  
                                print '-d option accepts either no parameters or a single parameter.\n'
		elif sys.argv[1] == '-l':
			if len(sys.argv) == 2:
				func(str(sys.argv[1]),'')
			else:
				print '-l option accepts no parameters.\n'
		else:
			os.system('./'+sys.argv[0]+'')
