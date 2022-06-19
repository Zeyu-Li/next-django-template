import logging

def Logger():
    ''' logger singleton '''
    return logging.getLogger('app')
