import os
import sys
from iph.utils.logger import logger  # from rpw, thanks @ https://github.com/gtalarico !


SESSION = None
DIR_PATH = os.path.dirname(__file__)
sys.path.append(DIR_PATH)
sys.path.append(os.path.dirname(DIR_PATH))

# wake up manager
from iph.main import Manager


def go(target=None):
    """ launch app directly with(out) target
    """
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
    """ init Manager component to accept snapshots
        do not use manually
    """
    global SESSION

    if not SESSION:
        SESSION = Manager()
        SESSION.init_components(target)


def snap(target=None):
    """ add a new snapshot of a target in the model
    """
    global SESSION
    logger.debug('snap : {}'.format(target))
    if (SESSION and target and SESSION.modelview and SESSION.modelview.ready):
            SESSION.modelview.init(target)

    elif not SESSION:
        start(target)


def debug(target=None):
    """ launch dev mode (verbose log + debug controls)
    """
    logger.verbose(True)
    man = Manager()
    man.mode_dbg = True
    man.init_components(target)
    man.start_app()
