import time
from functools import wraps
 
def dbg_timercheck(function):
    ''' only print if time > 0.005
    '''
    @wraps(function)
    def function_timer(*args, **kwargs):
        
        t0 = time.time()
        result = function(*args, **kwargs)
        t1 = time.time()
        if t1-t0 > 0.005:
            print ("Total %s: %s seconds" %
                   (function.func_name, str(t1-t0))
                   + repr(args))
            
        return result
    return function_timer


def dbg_timertest(function):
    @wraps(function)
    def function_timer(*args, **kwargs):
        
        t0 = time.time()
        result = function(*args, **kwargs)
        t1 = time.time()
        print ("Test Total %s: %s seconds" %
                (function.func_name, str(t1-t0))
                + repr(args))
            
        return result
    return function_timer
