""" Main module for object analysis,
    provides infos or templates depending on the type
    all these functions are used in the main types table (anatable.py)
    
"""
import clr
from iph import logger


def get_member_name(refobject):
    """ return the best readable name
    """
    try:
        member_name = refobject.__name__

    except AttributeError:
        member_name = type(refobject).__name__

    except Exception as error:
        logger.debug('get_member_name :'+str(error))
        member_name = str(refobject)
    
    return member_name

def get_revit_parameter_name(refobject):
    try:
        member_name = 'Param : ' + refobject.Definition.Name
    except Exception as error:
        logger.debug('get_revit_parameter_name :' + str(error))
        member_name = str(refobject)

    # add value in name
    try:
        member_name += ' ({})'.format(refobject.AsValueString())
    except:
        pass
    return member_name

#                               #
#          DOC TEMPLATES
#                               #

# todo doc in revit index
def get_event_doc(refobject):
    """ BoundEvent
    """
    return refobject.Event.__doc__


def get_rout_event_doc(refobject):
    """
    """
    try:
        doc = refobject.Name
        doc += '\nHandler Type: ' + str(refobject.HandlerType)
        doc += '\nOwner Type: ' + str(refobject.OwnerType)
        doc += '\nRouting Strategy : ' + str(refobject.RoutingStrategy)
    except Exception as error:
        logger.debug('function get_rout_event_doc :'+str(error))
        doc = get_doc(refobject)
    return doc


def get_indexer_doc(refobject):
    """ indexer  getset_descriptor
    """
    doc = get_doc(refobject)
    doc += '\n' + str(refobject.PropertyType.__doc__)
    return doc


def get_std_doc(refobject):
    """ str, bool int float ...
    """
    return 'Builtin : ' + str(type(refobject).__name__)


def get_class_doc(refobject):
    doc = str(refobject.__doc__)
    try:
        doc += '\n' + str(refobject.__mro__)
    except Exception as error:
        logger.debug('function get_class_doc :'+str(error))
        pass
    return doc


def get_doc(refobject):
    """ try to access the __doc__ attribute
    """
    try:
        doc = refobject.__doc__
        if not doc:
            doc = 'n/a'

    except Exception as error:
        doc = 'Error :' + str(error)
        logger.debug('function get_doc :'+str(error))

    return doc


#                               #
#        VALUES TEMPLATES
#                               #

def get_list_val(refobject):
    """ list type format
    """
    return '\n'.join(list(map(str, refobject)))


def get_dict_val(refobject):
    """ dict type format
    """
    values = [str(k) + ': ' + repr(val) for k, val in refobject.items()]
    return '\n'.join(values) 


def get_event_val(refobject):
    """ BoundEvent
    """
    handler = refobject.Event.Info.EventHandlerType.ToString()
    value = 'Event arg :' + handler.split('.')[:-1].pop()
    return value


def get_value_enum(enumobject):
    """ clrtype enumeration
    """
    try:
        lst_enum = enumobject.GetEnumNames()
    except:
        lst_enum = clr.GetClrType(enumobject).GetEnumNames()

    return '\n'.join(lst_enum)


def get_value_subenum(enumobject):
    """ clrtype enumeration
    """
    try:
        lst_enum = type(enumobject).GetEnumNames()
    except:
        lst_enum = clr.GetClrType(type(enumobject)).GetEnumNames()

    return '\n'.join(lst_enum)


def get_std_value(refobject):
    """ basic str/repr
    """
    try:
        value = str(refobject)
    except:
        value = repr(refobject)

    return value


def get_revit_parameter_value(refobject):
    try:
        value = refobject.AsValueString()
    except:
        value = repr(refobject)

    return value

