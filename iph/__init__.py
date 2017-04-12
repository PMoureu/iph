import os
import sys

SESSION = None

DIR_PATH = os.path.dirname(__file__)
sys.path.append(DIR_PATH)
sys.path.append(os.path.dirname(DIR_PATH))

from iph.utils.logger import logger # thanks rpw!

def get_hostname():
    import clr
    clr.AddReference('System.Windows.Forms')
    import System.Windows.Forms as forms
    return forms.Application.ProductName

hostname = get_hostname()
 
# wake up manager
from iph.main import Manager

def go(target=None):
    ''' launch app directly with(out) target
    '''
    global SESSION
    if SESSION:
        if target and SESSION.modelview and SESSION.modelview.ready:
            SESSION.modelview.init(target)
        SESSION.start_app()
    else:
        SESSION = Manager()
        SESSION.init_components(target)
        SESSION.start_app()

def start(target=None):
    ''' init component to accept snapshots
    '''
    global SESSION

    if not SESSION:
        SESSION = Manager()
        SESSION.init_components(target)

def snap(target=None):
    ''' add a new snapshot of a target in the model
    '''
    global SESSION
    if (SESSION and target and 
        SESSION.modelview and SESSION.modelview.ready):
        SESSION.modelview.init(target)

    elif not SESSION:
        start(target)

def debug(target=None):
    ''' launch debug mode (verbose log + debug controls)
    '''
    logger.verbose(True)
    man = Manager()
    man.mode_dbg = True
    man.init_components(target)
    man.start_app()
    

