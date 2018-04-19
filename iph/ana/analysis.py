import clr
from iph import logger
from details import *
from anatable import *


def get_model_details(refobject):
    """ main funnel to choose the best model representation
        based on object's type
    """
    typename = type(refobject).__name__

    if typename in TYPES_TABLE:

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

    # match all list/collection types
    elif is_iterable(refobject):
        details = TYPES_TABLE['listtype']

    # match sub enum types
    elif clr.GetClrType(type(refobject)).IsEnum:
        details = TYPES_TABLE['subenumtype']

    # match sub class types
    elif clr.GetClrType(type(refobject)).IsClass:

        if clr.GetClrType(type(refobject)).FullName == 'Autodesk.Revit.DB.Parameter':
            details = TYPES_TABLE['revitparameter']

        elif clr.GetClrType(type(refobject)).FullName.startswith('Autodesk.Revit.DB'):
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
    """ test more efficient than checking dir(object) with huge class
    """
    is_iter = False
    try:
        for e in refobject: 
            break
        is_iter = True
    except:
        pass

    return is_iter
