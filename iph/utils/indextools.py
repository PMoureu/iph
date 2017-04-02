import clr
import gc


# todo add a number index to break 

MAX_DEEP = 15

def create_index(ref_base, fullpath):
    ''' create a search index for autocompletion
    '''
    index = {}
    template = get_template(ref_base)
    if template:
        index.update(template(0, ref_base, fullpath))

    return index

def get_template(ref):
    ''' define a members template to choose recursivity or not
        next step : look in class members 
    '''
    res = None
    if type(ref).__name__ == 'namespace#':
        res = get_members_recurs

    elif type(ref).__name__ == 'module':
        res = get_members_recurs

    #elif isinstance(ref, type):
    #    clrtype = clr.GetClrType(ref)

    #    if clrtype.IsEnum:
    #        res = get_members
            
    #    elif clrtype.IsClass:
    #        res = get_members

    return res

def get_members(_, ref_base, fullpath):
    ''' no recursive function...
    '''
    members = {}
    for member in dir(ref_base):
        members[member+'@'+ fullpath] = {
            'title': member,
            'refpath': fullpath
            }
    return members

def get_members_recurs(level, ref_base, fullpath):
    ''' hard recursive function...
    '''
    level +=1
    members = {}
    for member in dir(ref_base):
        members[member+'@'+ fullpath] = {
            'title': member,
            'refpath': fullpath
            }

        try:
            membref = getattr(ref_base, member)
            template = get_template(membref)

            if level < MAX_DEEP and template:
                members.update(template(
                    level, 
                    membref, 
                    fullpath +'.'+ member))

        except Exception as error:
            print(error)

    return members




