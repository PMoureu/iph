import time
from functools import wraps

#                               #
#       WELCOME PLACEHOLDER
#                               #
class Welcome:
    """
    Explore some API or your own code.

    Click on the below tips to display some help

    """
    def tip_00_General_usage(self):
        """
        - Select a node in the tree to display details.
        - click on a gridrow to see details
        - click on a gridrow icon to open a new tab
        - sort the colums or filter the names to find what you want
        - open options dock to add new API or new python module
         (living in the current scope or tries import from folder)
        """

    def tip_01_Do_Not(self):
        """
        - Don't press * on the tree !!

        """

    def tip_02_Normal_mode(self):
        """
        Just launch the app to explore api, get details of classes etc..
        Right-Click on the launcher to use the ironpython console
          or
        import iph
        iph.go()
        """

    def tip_03_Snapshot_tool(self):
        """
        This mode allows you to track some variables in your code

        - first import the module iph and init the mode with a first call:
          import iph
          iph.snap(your_object)
          ... code ...

          iph.snap(your_object_after_work)

        - finally add this line at the end to launch the app
          iph.go()
        """

    def tip_04_Add_new_api(self):
        """
        You can try to add other API located in the same folder
        or living in the scope, reachable through clr.References.

        - Open the options dock and change the hook path

        - You can create an index to enable autocompletion (be carefull,
          You should remove it after use to release memory )
        """

    def __repr__(self):
        return 'Welcome Class'


#                               #
#        TIMER FUNCTIONS
#                               #
def dbg_timercheck(function):
    """ only print if time > 0.005
    """
    @wraps(function)
    def function_timer(*args, **kwargs):
        
        t0 = time.time()
        result = function(*args, **kwargs)
        t1 = time.time()
        if t1-t0 > 0.005:
            print ("Timer Warning !! %s: %s s." %
                   (function.func_name, str(t1-t0)))
            
        return result
    return function_timer


def dbg_timer(function):
    @wraps(function)
    def function_timer(*args, **kwargs):
        
        t0 = time.time()
        result = function(*args, **kwargs)
        t1 = time.time()
        print ("Test Total %s: %s seconds" %
                (function.func_name, str(t1-t0)) + repr(args))
            
        return result
    return function_timer
