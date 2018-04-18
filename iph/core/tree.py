import gc
from System.Collections.ObjectModel import ObservableCollection
from iph import logger
from iph.core import BaseNotifier
from iph.ana.details import get_member_name
from iph.ana.syshook import try_resolve_path
from iph.utils.dialogs import *
from basemodel import ModelObject
from treeoption import OptionBaseRoot


#                               #
#      TREE CONTENT MANAGER
#                               #

class TreeViewManager(BaseNotifier):
    """
        Holds the treeview collection and the list of options given by 
        settings (represented by the dock collapsed on left)
        
       - display enabled nodes in the tree in basic mode
       - or display only target(s) provided by the call 

    """
    def __init__(self, settings):
        super(TreeViewManager, self).__init__()

        self.settings = settings
        self.list_options = ObservableCollection[OptionBaseRoot]()
        self.list_roots = ObservableCollection[NodeBase]()

        for api in settings:
            option_api = OptionBaseRoot(
                api['name'], api['path'], api['enabled'], self)
            self.list_options.Add(option_api)

    def init_target(self, target):
        """
            arg :target, object to inspect, given by an external call
        """
        target_name = get_member_name(target)
        node = self.create_root_node(target, target_name)

    def init_options_api(self):
        """
            creates a rootnode for all enabled api in options
        """
        for option_api in self.list_options:
            if option_api.enabled:
                # holds the ref to node to disable it later
                option_api.rootnode = self.create_root_from_path(
                    option_api.name, option_api.path)

    def create_root_from_path(self, nameapi, path):
        """
            resolves the path from sys.modules
        """
        hookref = try_resolve_path(path)
        if not hookref:
            ok_help('Sorry, cannot load this module :\n' + str(path))
        else:
            return self.create_root_node(hookref, nameapi)

    def create_root_node(self, ref_object, name=''):
        """ add a new root to the tree
            args : ref_object, reference
                  name, optional, string
        """
        if not name:
            name = get_member_name(ref_object)
        try:
            rootnode = NodeBase(ModelObject(ref_object, name), None)
            rootnode.expand_node()

        except Exception as error:
            rootnode = NodeBase(ModelObject(None, str(error)), None)
            logger.error('Error create_root_node :' + str(error))

        self.list_roots.Add(rootnode)

        return rootnode

    def focus_node_from_path(self, fullpath, api_target):
        """ split path, find/create root with the first part,
            and calls expands_to_node to finish the job
            args : fullpath, string with dot (iph.core.tree)
        """
        
        for api_option in self.list_options:
            if api_option is api_target:
                api_option.rootnode.IsExpanded = True

            elif api_option.rootnode:
                api_option.rootnode.IsExpanded = False
        try:
            nodepath = fullpath.split(api_target.path)[1]
            nodeslist = [node for node in nodepath.split('.') if node][::-1]
            parent = api_target.rootnode

            while nodeslist:
                next_node = nodeslist.pop()
                for node in parent.members:
                    if node.model.name == next_node:
                        node.IsExpanded = True  # triggers members creation
                        parent = node
                        break
            if node:
                node.IsSelected = True

        except Exception as error:
            logger.error('Error focus_node_from_path :' + str(error))

    def select_node_startswith(self, basenode, letter):
        """ shortcut to focus nodes by name in the tree
        """
        for node in basenode.members:
            if node.model.name.upper().startswith(letter.upper()):
                node.IsSelected = True
                break

    def remove_root_node(self, ref_node):
        """ delete rootnode from the tree
        """
        try:
            ref_node.members.Clear()
            self.list_roots.Remove(ref_node)
        except Exception as error:
            logger.error('Error remove_root_node' + str(error))

    def release_option(self, optionitem):
        """ todo plug in UI
        """
        try:
            self.list_options.Remove(optionitem)
        except Exception as error:
            logger.error('Error release_option' + str(error))

    def add_empty(self):
        """ adds a new option
        """
        self.list_options.Add(OptionBaseRoot('Name', 'Full.Path', False, self))

    def expand_nodes_from_name(self, searchname):
        """ todo
            search in members of module, class, enum
            limit by level
        """
        pass


#                               #
#         TREENODE BASE
#                               #

class NodeBase(BaseNotifier):
    """ Treenode class
        holds a modelbase with : name, ref, type, category, icon
        members are separated from model to allow differents templates
        in the tree and the gridrow
    """
    def __init__(self, model, parent):
        """ init with a model and the parent node
            (or None for the root)
        """
        super(NodeBase, self).__init__()
        self.model = model
        self.parent = parent
        self.is_filled = False
        self.is_selected = False
        self.is_expanded = False
        self.members = ObservableCollection[NodeBase]()

        if self.model.templ_members:
            dum = ModelObject(None, 'empty')
            self.members.Add(NodeBase(dum, self))
    
    def expand_node(self):
        """ only expand if a template_members is provided on the node
            triggered by xaml, treeitem property IsExpanded
        """
        self.is_filled = True
        self.members.Clear()
        gc.collect()
        for newmodel in self.model.get_members():
            try:
                node = NodeBase(newmodel, self)
            except Exception as error:
                node = NodeBase(ModelObject(None, 'Error...'), self)
                logger.debug('expand_node for : {} {} - {}'.format(
                    self.model.name, self.model.type, error))

            self.members.Add(node)

    # get/set for expand control
    def get_expand(self):
        return self.is_expanded

    def set_expand(self, isexpand):
        if isexpand:
            if not self.is_filled:
                self.is_filled = True
                self.expand_node()
            self.is_expanded = True
        else:
            self.is_expanded = False
        self.NotifyPropertyChanged('IsExpanded')
    IsExpanded = property(get_expand, set_expand)

    # get/set for selection control
    def get_selected(self):
        return self.is_selected

    def set_selected(self, selected):
        if selected:
            self.is_selected = True
        else:
            self.is_selected = False
        self.NotifyPropertyChanged('IsSelected')
    IsSelected = property(get_selected, set_selected)

    def __repr__(self):
        name = self.model.name if self.model else '/ no model'
        return 'NodeBase ' + name
