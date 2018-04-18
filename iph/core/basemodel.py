"""
    This file contains the base model class used in tree, tabs and datagrid.

    Special note : 
    search of __doc__ can be very slow with many members or some types,
    so display is delayed and triggered by a row selection in the datagrid

    value and doc are only used by tabs and gridrow so the model holds a template
    to avoid overloading the tree with potential huge values.

"""

from iph import logger
from iph.ana.details import get_member_name
from iph.ana.analysis import get_model_details
from config import img_tree


#                               #
#           MAIN MODEL
#                               #

class ModelObject(object):
    """ represents an ironpython object
        model for node element, tab, and gridrow

        init with a ref and a name if possible (given by dir() )
    """
    def __init__(self, ref_object, name=''):
        """ args:
            ref_object : direct reference
            name: str
        """
        super(ModelObject, self).__init__()

        self.ref = ref_object
        self.type = type(self.ref).__name__
        self.name = name if name else get_member_name(self.ref)

        details = get_model_details(self.ref)

        self.icon = img_tree[details['icon']]
        self.category = details['category']
        self.templ_members = details['members']
        self.templ_value = details['value']
        self.templ_doc = details['doc']

    def get_members(self):
        if self.templ_members:
            try:
                for name, ref in self.templ_members(self.ref):
                    yield ModelObject(ref, name)
            except Exception as error:
                logger.error(error)

    def get_doc(self):
        doc = self.templ_doc(self.ref)
        if not doc:
            doc = 'n/a'
        return doc

    def get_value(self):
        val = self.templ_value(self.ref)
        if not val:
            val = 'n/a'
        return val
