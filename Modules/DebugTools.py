'''
This module provides basic debug tools for top-level modules.
'''

import sys, traceback

def beforeExit():
    print('-'*32)
    print('PRESS ANY KEY TO EXIT...')
    input()
    sys.exit()
    
def traceBug(location='UNKNOWN', print_exc=True):
    TYPE, VALUE, TB = sys.exc_info()
    if print_exc:
        sys.stderr.write('LOCATION: %s' % location)
        traceback.print_tb(TB)
        sys.stderr.write(str(TYPE))
        sys.stderr.write(str(VALUE))
        sys.stderr.write('\n\n')
    return VALUE
