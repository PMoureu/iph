""" unittest what ??
    at beginning i created a simple context manager to wrap basics tests
    with 3 or 4 constants more, and the file discover, it's really easy to
    add news tests
"""
import sys
import importlib
from iph import logger
from iph.utils.tools import dbg_timercheck

def discover_and_run(verbose=False):
    """ loads all 'test_*' files and performs all 'test_*' functions
        
    """
    if verbose:
        logger.verbose(True)
    logger.title('Test all components')

    NB_TESTS = 0
    NB_FAILS = 0
    NB_CRASH = 0
    NB_PASSED = 0
    TODO = set()

    import glob, os
    os.chdir(os.path.dirname(__file__))
    modules_tests = glob.glob('test*.py')
    NB_MODS = len(modules_tests)
    checkmod = 0
    for file in modules_tests:
        name_mod = file.split('.')[0]

        test_cases = []
        try:
            tmodule = importlib.import_module(
                '.'+ name_mod, 'iph.tests')

            test_cases = [case for case in dir(tmodule) 
                          if case.startswith('test_')]

            if not test_cases:
                continue

            logger.title('\n   *   *  MODULE : '+ name_mod)
            nb_cases = len(test_cases)
            NB_TESTS += nb_cases
            crashs = NB_CRASH
            fails = NB_FAILS
            passed = NB_PASSED

            for case in test_cases:
                
                msg = 'Test : '+ case + '.' * (50-len(case)) 
                try:
                    dbg_timercheck(getattr(tmodule, case))()
                    msg += 'OK'
                    NB_PASSED += 1

                except AssertionError as error:

                    msg += 'FAILED {}'.format(error)
                    NB_FAILS += 1
                    TODO.add(case)
                except:
                    logger.error(msg)
                    TODO.add(case)
                    NB_CRASH += 1
                    msg += 'CRASHED '
                    if verbose:
                        import traceback
                        traceback.print_exc()

                finally:
                    logger.info(msg)

            logger.title('\tEnd ===> {} fails - {} crashed ({} errors raised) - {}/{}\n'.format(
                NB_FAILS - fails,  NB_CRASH - crashs, 
                len(logger.errors), 
                NB_PASSED - passed, nb_cases))
            checkmod += 1

        except Exception as error:
            break
            logger.error(name_mod +' crashed !!!!! : {}'.format(error))
            import traceback
            traceback.print_exc()

    logger.title('\n\t\tTESTS END : {} modules test - {}/{} PASSED -  {} fails / {} crashed'.format(
            NB_MODS, NB_PASSED, NB_TESTS, NB_FAILS, NB_CRASH))

    logger.info('guilty functions :\n' + '\n'.join(TODO))

    if not checkmod == NB_MODS:
        logger.info('tests CRASHED !!')
    
