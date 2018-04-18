import clr
import gc
from System.Collections.ObjectModel import ObservableCollection
from iph.utils.dialogs import *
from iph.utils.tools import Welcome
from iph import logger
from iph.ana.details import *
from tree import TreeViewManager
from tabs import TabViewItem
from iph.core.basemodel import ModelObject
from iph.core import BaseNotifier


#                               #
#        MAIN MODEL VIEW
#                               #

class ModelView(BaseNotifier):
    """ Central Model view, relays all events notified by subviews
        - holds the tabs list
        - delegates the tree logic to treemanager (datacontext is set in xaml)
        - manage autocompletion list (groups all enabled indexes)

    """

    def __init__(self, manager):
        super(ModelView, self).__init__()
        self.ready = False
        self.manager = manager
        self.log_errors = []
        self.treemanager = TreeViewManager(manager.settings['api_set'])
        self.tabs_list = ObservableCollection[TabViewItem]()
        self.autocompl = ObservableCollection[OptionCompletion]()
        self.ready = True

    def init(self, target):
        """ init tree with target if provided else enables api options
        """
        if target:
            self.treemanager.init_target(target)
            self.add_new_tab(ModelObject(target))
        else:
            self.treemanager.init_options_api()
            self.tabs_list.Add(TabViewItem(ModelObject(Welcome(), 'Welcome')))

    def close_tab(self, item):
        """ close selected tab unless it's the last
        """
        try:
            if len(self.tabs_list) > 1:
                self.tabs_list.Remove(item)
                item.datagrid = None
                item = None
                gc.collect()

        except Exception as error:
            logger.error('Error close_tab : ' + str(error))

    def add_new_tab(self, newmodel):
        """ display a new tab
            arg: newmodel , model of the gridrow item given by ui event
            (works with treeitem too)
        """
        try:
            new_tab = TabViewItem(newmodel)
            self.tabs_list.Add(new_tab)
            self.manager.main_form.ui_tabs_control.SelectedIndex = len(self.tabs_list)-1

        except Exception as error:
            logger.error('add_new_tab for : '+ str(error))
    
    def update_current_tab(self, sel_tab, sel_node):
        """ replace details in selected tabview
            called by ui code-behind (on_node_select event)
        """
        try:
            if not len(self.tabs_list):
                self.tabs_list.Add(TabViewItem(sel_node.model))
            else:
                sel_tab.refresh(sel_node.model)
        except Exception as error:
            logger.error('update_current_tab for : {} - {}/ {}'.format(
                sel_tab, sel_node, error))

    def restore_autocompl(self):
        """ Cleans suggestions list on the left dock
        """
        self.autocompl.Clear()
        gc.collect()

    def update_autocompl(self, text):
        """ refresh list with the new string to found
        """
        self.autocompl.Clear()
        gc.collect()
        for base_api in self.treemanager.list_options:
            if isinstance(base_api.index_module, dict):
                for key, dictoption in base_api.index_module.items():
                    if dictoption['title'].upper().startswith(text.upper()):
                        self.autocompl.Add(OptionCompletion(
                            dictoption['title'], 
                            dictoption['refpath'],
                            base_api))
                
        return len(self.autocompl)

    def debug(self, element):
        """ most convenient method when working on the project:
            linked to F10 key
            adds a node in the tree to inspect properties, 
            or what's going wrong
        """
        self.treemanager.create_root_node(element)

    def refresh_logger(self):
        """ refresh the combobox on debug mode
            (last errors first)
        """
        self.log_errors = logger.errors[::-1]
        self.NotifyPropertyChanged("log_errors")


#                               #
#         AUTOCOMPLETION
#                               #

class OptionCompletion(object):
    """
        small class to wrap suggestions option
    """
    def __init__(self, title, refpath, api):
        self.title = title
        self.refpath = refpath
        self.base_api = api
