import clr
from iph import logger
from details import *
from anatable import *


def get_model_details(refobject):
    ''' main funnel to choose the best model representation
        based on object's type
    '''
    typename = type(refobject).__name__

    if TYPES_TABLE.has_key(typename):

        details = TYPES_TABLE[typename]

    elif isinstance(refobject, type):
        clrtype = clr.GetClrType(refobject)

        if clrtype.IsEnum:
            details = TYPES_TABLE['enumtype']
            
        elif clrtype.IsClass:
            if clrtype.FullName.startswith('Autodesk.Revit.DB'):
                details = TYPES_TABLE['revitclass']
            else:
                details = TYPES_TABLE['classtype']

        elif clrtype.IsInterface:
            details = TYPES_TABLE['interface']

        elif clrtype.FullName in SYS_TYPES:
            details = TYPES_TABLE['systype']

        elif clrtype.FullName in WIN_TYPES:
            details = TYPES_TABLE['wintype']

        else:
            details = TYPES_TABLE['unknown']
            logger.debug('TODO get_model_details for CLR/type: {}  ({})'.format(
                typename, refobject))

    elif is_iterable(refobject): # match all collection types
        details = TYPES_TABLE['listtype']

    elif clr.GetClrType(type(refobject)).IsEnum: # match sub enum types
        details = TYPES_TABLE['subenumtype']

    elif clr.GetClrType(type(refobject)).IsClass: # match sub class types
        if clr.GetClrType(type(refobject)).FullName.startswith('Autodesk.Revit.DB'):
            details = TYPES_TABLE['revitclass']
        else:
            details = TYPES_TABLE['subclasstype']

    elif clr.GetClrType(type(refobject)).IsInterface:
        details = TYPES_TABLE['interface']

    elif clr.GetClrType(type(refobject)).FullName in SYS_TYPES:
        details = TYPES_TABLE['systype']

    elif clr.GetClrType(type(refobject)).FullName in WIN_TYPES:
        details = TYPES_TABLE['wintype']

    else:
        details = TYPES_TABLE['unknown']
        logger.debug('TODO get_model_details for : {}  ({})'.format(
            typename, refobject))

    return details

def is_iterable(refobject):
    ''' test more efficient than checking dir(object) with huge class
    '''
    is_iter = False
    #try:
    #    len(refobject) #refobject.__iter__
    #    is_iter = True
    #except:
    #    pass
    try:
        for e in refobject: 
            is_iter = True
            break
    except:
        pass

    return is_iter


