import logging

def Logger():
    ''' 
    logger singleton
    
    Returns
    -------
    logger singleton
    '''
    return logging.getLogger('app')
