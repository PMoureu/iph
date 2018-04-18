""" basic functions to resolve a reference from sys.modules or clr import
    
"""
import importlib
import sys
import clr
from iph import logger


def try_resolve_path(path_to_ref):
    """ arg path_to_ref : string, ex: System.Windows.Controls
    """

    if path_to_ref in sys.modules:
        refobject = sys.modules[path_to_ref]

    else:
        try:
            mods = [mod for mod in path_to_ref.split('.') if mod][::-1]
            base_module = mods.pop()
            if base_module in sys.modules:
                refobject = sys.modules[base_module]
                while mods:
                    mod = mods.pop()
                    refobject = getattr(refobject, mod)
            else:
                refobject = try_import_python_path(path_to_ref)
                
        except Exception as error:
            logger.debug('try_resolve_path failed {}- {}'.format(path_to_ref, error))
            refobject = try_import_python_path(path_to_ref)

    return refobject


def try_import_python_path(path_to_ref):
    """ arg path_to_ref : string, ex: iph.core.ui
    """
    
    try:
        refobject = importlib.import_module(path_to_ref)
        if not refobject:
            refobject = try_import_clr_path(path_to_ref)

    except Exception as error:
        logger.debug('try_import_python_path Backup import failed {} - {}'.format(path_to_ref, error))
        refobject = try_import_clr_path(path_to_ref)

    return refobject


def try_import_clr_path(path_to_ref):
    """ try add clr reference
        arg path_to_ref : string
    """
    try:

        mods = [mod for mod in path_to_ref.split('.') if mod][::-1]
        entry_module = mods.pop()
        clr.AddReferenceByPartialName(entry_module)

        if entry_module in sys.modules:
            refobject = sys.modules[entry_module]
            while mods:
                mod = mods.pop()
                refobject = getattr(refobject, mod)
        else:
            for ref in clr.References:
                if ref.FullName.startswith(path_to_ref):
                    refobject = ref
                    break
            else:
                refobject = clr.References

    except Exception as error:
        refobject = None
        logger.debug('try_import_clr_path Backup import failed {} - {}'.format(path_to_ref, error))

    finally:
        return refobject
