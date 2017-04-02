import clr
from iph import logger
from excluds import *

#                               #
#     DEFAULT FILTER TEMPLATE
#                               #

def get_members_default(refobject):
    ''' default template filter
        display all members except builtins and magic
    '''
    dir_obj = sorted(set(dir(refobject)) - SET_BUILT)
    
    for member in dir_obj:
        try:
            ref_member = getattr(refobject, member)
            
        except Exception as error:
            ref_member = None
            member += ' ! no access !'
            
            logger.debug('get_members_default : '+ member + str(error))

        finally:
            yield (member, ref_member)

#                               #
#        FILTERS TEMPLATES
#                               #


def get_members_filt_revit(refobject):
    ''' display all members except inherited from Element
        
    '''
    dir_obj = sorted(set(dir(refobject)) - SET_REVIT)
    
    for member in dir_obj:
        try:
            ref_member = getattr(refobject, member)
            
        except Exception as error:
            ref_member = None
            member += ' ! no access !'
            
            logger.debug('method get_members_filt_revit :'+ member + str(error))

        finally:
            yield (member, ref_member)

#                               #
#        MEMBERS TEMPLATES
#                               #


def get_members_no_filter(refobject):
    ''' default no filtered template using dir()
    '''
    for member in dir(refobject):
        try:
            ref_member = getattr(refobject, member)
            
        except Exception as error:
            ref_member = None
            member += ' ! no access !'
            
            logger.debug('get_members_no_filter :'+ member + str(error))

        finally:
            yield (member, ref_member)

def get_members_enum(enumobject):
    ''' template for enum types
    '''
    try:
        lst_enum = enumobject.GetEnumNames()
    except:
        lst_enum = clr.GetClrType(enumobject).GetEnumNames()

    for nameoption in lst_enum:
        yield (nameoption, None)

def get_members_subenum(enumobject):
    ''' template for enum types
    '''
    try:
        lst_enum = type(enumobject).GetEnumNames()
    except:
        lst_enum = clr.GetClrType(type(enumobject)).GetEnumNames()

    for nameoption in lst_enum:
        yield (nameoption, None)

def get_list_members(refobject):
    ''' readable and indexed template for list type
        Limited to the 200 first items
    '''
    
    for ind, item in enumerate(refobject):
        if ind > 200:
            break
        yield (str(ind) +': '+ str(item), item)


def get_dict_members(refobject):
    '''readable and indexed template for dict type
        Limited to the 200 first items
    '''
    ind = 0
    for key, val in refobject.items():
        ind += 1
        if ind > 200:
            break
        yield (str(key), val)



