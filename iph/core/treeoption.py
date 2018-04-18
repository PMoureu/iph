import gc
from iph.core import BaseNotifier
from iph.utils.indextools import create_index
from iph.utils.dialogs import ok, ok_error


#                               #
#       TREE ROOTS OPTIONS 
#                               #
class OptionBaseRoot(BaseNotifier):
    """ represents an API saved in the settings
        (or any reference added by user)
        associated to a root node in the tree
    """
    def __init__(self, title, lpath, enab, parent):
        super(OptionBaseRoot, self).__init__()
        self.parent = parent
        self._enabled = enab
        self.name = title
        self.path = lpath
        self.rootnode = None
        self.index_module = None

    def create_module_index(self):
        """ creates an index to enable autocompletion
        """
        if self.path and self.rootnode and self.rootnode.model:
            self.index_module = create_index(
                self.rootnode.model.ref, self.path)

            if not self.index_module:
                ok_error('Sorry, no index found for ' + self.name)

            else:
                ok('Index is ready for {} ({} entries)'.format(
                        self.name, len(self.index_module)))

    def delete_index(self):
        """ removes index and force memory cleanup
        """
        if self.index_module:
            self.index_module = None
            gc.collect()

    # get/set to control enabled state
    def get_enabled(self):
        return self._enabled

    def set_enabled(self, val):
        if val:
            self.rootnode = self.parent.create_root_from_path(
                            self.name, self.path)
            
            if self.rootnode:
                self._enabled = True
            else:
                self._enabled = False
        else:
            self._enabled = False
            if self.rootnode:
                self.parent.remove_root_node(self.rootnode)
                self.rootnode = None

    enabled = property(get_enabled, set_enabled)

    # get/set to control index creation
    def get_ind_enabled(self):
        return self.index_module is not None

    def set_ind_enabled(self, val):
        if val:
            self.create_module_index()
        else:
            self.delete_index()
    index_enabled = property(get_ind_enabled, set_ind_enabled)

    def get_json(self):
        """ called by the manager when closing app
        """
        return {'name': self.name, 
                'path': self.path, 
                'enabled': self.enabled}
