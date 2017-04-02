import clr
import gc
from System.Collections.ObjectModel import ObservableCollection
from iph.utils.dialogs import *
from iph import logger
from iph import DIR_PATH, hostname
from iph.ana.details import *
from tree import TreeViewManager
from tabs import TabViewItem
from iph.core.basemodel import ModelObject
from iph.core import BaseNotifier

#                               #
#        MAIN MODEL VIEW
#                               #

class ModelView(BaseNotifier):
    ''' Central Model view, holds the tabs list and delegates
    the tree logic to treemanager (datacontext is set in xaml)
    also relays events notified by all subviews
    
        interface:
        - settings/api targets
        - autocompletion

    '''

    def __init__(self, manager):
        super(ModelView, self).__init__()
        self.ready = False
        self.manager = manager
        self.log_errors = []
        self.treemanager = TreeViewManager(manager.settings['api_set'])
        self.tabs_list = ObservableCollection[TabViewItem]()
        self.autocompl = ObservableCollection[OptionCompletion]()
        self.tabs_list.Add(TabViewItem(ModelObject(Welcome(),'Welcome')))

        self.ready = True

    def init(self, target):
        ''' init tree with target if provided else enables api options
        '''
        if target:
            self.treemanager.init_target(target)
            self.add_new_tab(ModelObject(target))
        else:
            self.treemanager.init_options_api()

    def close_tab(self, item):
        ''' close selected tab unless it's the last
        '''
        try:
            if len(self.tabs_list) > 1:
                self.tabs_list.Remove(item)
                item.datagrid = None
                item = None
                gc.collect()

        except Exception as error:
            logger.error('Error close_tab : ' + str(error))

    def add_new_tab(self, newmodel):
        ''' display a new tab
            arg: newmodel , model of the gridrow item given by ui event
            (works with treeitem too)
        '''
        try:
            new_tab = TabViewItem(newmodel)
            self.tabs_list.Add(new_tab)
            self.manager.main_form.ui_tabs_control.SelectedIndex = (len(self.tabs_list)-1)

        except Exception as error:
            logger.error('add_new_tab for : '+ str(error))
    
    def update_current_tab(self, sel_tab, sel_node):
        ''' replace details in selected tabview
            called by ui code-behind (on_node_select event)
        '''
        try:
            sel_tab.refresh(sel_node.model)
        except Exception as error:
            logger.error('update_current_tab for : {} - {}/ {}'.format(
                sel_tab, sel_node, error))

    def restore_autocompl(self):
        ''' Cleans suggestions list on the left dock
        '''
        self.autocompl.Clear()
        gc.collect()

    def update_autocompl(self, text):
        ''' refresh list with the new string to found
        '''
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
        ''' most convenient method when working on the project:
            linked to F10 key
            adds a node in the tree to inspect properties, 
            or what's going wrong
        '''
        self.treemanager.create_root_node(element)

    def refresh_logger(self):
        ''' refresh the combobox on debug mode
            (last errors first)
        '''
        self.log_errors = logger.errors[::-1]
        self.NotifyPropertyChanged("log_errors")


#                               #
#         AUTOCOMPLETION
#                               #

class OptionCompletion(object):
    ''' small class to wrap a suggestions option 
        
    '''
    def __init__(self, title, refpath, api):
        self.title = title
        self.refpath = refpath
        self.base_api = api


#                               #
#       WELCOME PLACEHOLDER
#                               #

class Welcome(object):
    ''' Explore some API or your own code.

        - Select a node in the tree to display details.
        - click on a gridrow to see details 
        - click on a gridrow icon to open a new tab
        - sort the colums or filter the names to find what you want
        - open options dock to add new API or new python module
         (living in the current scope or tries import from folder)
        - Don't press * on the tree !!
    '''
    def __init__(self):
        self.text = 'Welcome, this is just a placeholder.'

    def tip_01_normal_mode(self):
        ''' Just launch the app to explore api, get details of classes etc..
              Right-Click on the launcher to use the ironpython console
          or 
              import iph
              iph.go()
        '''
    def tip_02_snapshot_tool(self):
        ''' This mode allows you to track some variables in your code

            - first import the module iph and init the mode with a first call:
              import iph
              iph.snap(your_object)
              ... code ...

              iph.snap(your_object_after_work)

            - finally add this line at the end to launch the app
              iph.go()
        '''
    def tip_03_add_new_api(self):
        ''' You can try to add other API located in the same folder
            or living in the scope with clr.References.

            - Open the options dock and change the hook path

            - You can create an index to enable autocompletion (be carefull,
              You should remove it after use to release memory )

        '''
    def __repr__(self):
        return 'Welcome Class'

