import os
import wpf
import System.Windows
from System.Windows import Window, Visibility, Thickness
from System.Windows.Input import FocusManager, Keyboard, Key
from iph import DIR_PATH
from iph.utils.dialogs import *
from config import img_tree

class MainForm(Window):
    ''' Represents the user interface
        - loads xaml
        - handle events and deals with modelview
    '''
    def __init__(self, manager):
        self.ready = False
        self.manager = manager
        self.modelview = manager.modelview
        self.closing = False
        self.debug = self.modelview.debug
        
        try:
            for key, val in img_tree.items():
                self.Resources.Add(key,val)

            self.Resources.Add('mode_dbg', manager.mode_dbg)

            # load xaml and bind context to modelview
            wpf.LoadComponent(self, 
                os.path.join(DIR_PATH, 'core', 'ui.xaml'))
            self.DataContext = self.modelview
            self.ui_tabs_control.SelectedIndex = 0

            param = self.manager.settings['window']
            self.Left = param['Left']
            self.Top = param['Top']
            self.Width = param['Width']
            self.Height = param['Height']
            
            self.ready = True
            
        except Exception as error:
            ok_error('Sorry, cannot load the xaml :'+ str(error))

    #                               #
    #           EVENTS UI
    #                               #

    #def OnClosing(self, event): # makes revit crash
    #    ''' catch the top [X] close event
    #    '''
    #    if not self.closing:
    #        event.Cancel = True
    #        self.closing = True
    #        self.manager.exit_app()

    def on_button_close(self, sender, event):
        ''' main close button event
        '''
        self.closing = True
        self.manager.exit_app()

    def on_click_options(self, sender, event):
        ''' toggle dock options displayed on the left
        '''
        if self.ui_roots_options.Visibility == Visibility.Collapsed:
            self.ui_options_api.BorderThickness = Thickness(1)
            self.ui_roots_options.Visibility = Visibility.Visible

        else:
            self.ui_options_api.BorderThickness = Thickness(0)
            self.ui_roots_options.Visibility = Visibility.Collapsed

    def on_button_index_click(self, sender, event):
        ''' create an index for autocompletion search
            datacontext is an OptionBaseRoot class
        '''
        if sender.DataContext:
            sender.DataContext.create_module_index()

    def on_node_select(self, sender, event):
        ''' click on a treenode refresh the current tab
        '''
        if sender.SelectedItem and self.ui_tabs_control.SelectedItem:
            self.modelview.update_current_tab(
                self.ui_tabs_control.SelectedItem, sender.SelectedItem)
    
    def on_keydown_tree(self, sender, event):
        ''' select the first node starting with the given name
            todo : search in whole word, save keys sequences
        '''
        key = str(event.Key)
        if len(key)==1 and key.isalpha():
            if self.ui_treeview.SelectedItem:
                node = self.ui_treeview.SelectedItem.parent
                if not node:
                    node = self.ui_treeview.SelectedItem
                if not node.IsExpanded:
                    node.IsExpanded = True
                self.modelview.treemanager.select_node_startswith(node, key)

    def on_row_select(self, sender, event):
        ''' handles click on datagridrows (add doc & val)
        '''
        if event.Row.DataContext:
            event.Row.DataContext.set_doc()

    def on_close_tab(self, sender, event):
        ''' tells modelview to remove selected tab
            and focus the last tab
        '''
        tab = sender.Parent.DataContext
        if tab == self.ui_tabs_control.SelectedItem:
            self.modelview.close_tab(tab)
            nbtabs = len(self.modelview.tabs_list)
            self.ui_tabs_control.SelectedIndex = nbtabs-1

    def on_rowicon_click(self, sender, event):
        ''' click on gridrow opens a new tab
            the model of the row is given to new tab
        '''
        if sender.DataContext and 'model' in dir(sender.DataContext):
            self.modelview.add_new_tab(sender.DataContext.model)

    def on_filterbox_textChanged(self, sender, event):
        ''' enable autocompletion dock or clean the list
        '''
        if not len(sender.Text):
           self.ui_search_options.Visibility = Visibility.Collapsed
           self.modelview.restore_autocompl()
           
        if len(sender.Text) > 1:
            names = self.modelview.update_autocompl(sender.Text)
            self.ui_search_options.Visibility = Visibility.Visible
            if not names:
                self.modelview.restore_autocompl()

    def on_suggestion_selected(self, sender, event):
        ''' links a suggestion to a node in the tree
            datacontext is a class OptionCompletion
        '''
        if sender.DataContext:
            dc = sender.DataContext
            fullpath = '.'.join([dc.refpath, dc.title])
            self.modelview.treemanager.focus_node_from_path(fullpath, dc.base_api)

    def on_filter_select(self, sender, event):
        ''' replaces tab item model template for members
        '''
        if not len(event.AddedItems):
            return
        if self.ui_tabs_control.SelectedItem is sender.DataContext:
            sender.DataContext.change_templ_memb(event.AddedItems[0].filter_funct)

    def on_filter_txt_tab(self, sender, event):
        ''' filters row by name
        '''
        if not len(sender.Text) and sender.DataContext:
            sender.DataContext.filter_by_name()

        if len(sender.Text) > 0 and sender.DataContext:
            sender.DataContext.filter_by_name(sender.Text)

    def on_filterbutton_click(self, sender, event):
        ''' todo : another search behavior : 
            filter and  expand relevants treenodes
            def expand_nodes_from_name
        '''
        pass
    #                               #
    #             DEBUG
    #                               #

    def on_debug_click(self, sender, event):
        ''' Adds a refreshed node in the tree to inspect properties at runtime
        '''
        self.debug(self.manager)
        self.debug(self.modelview)
        self.debug(self.modelview.treemanager)
    
    def ui_main_keydown(self, sender, event):
        ''' Second most convenient method when working on this project:
            Press F10 to debug the selected control at runtime
        '''
        if event.SystemKey == Key.F10:
            self.debug(FocusManager.GetFocusedElement(self))
    
    def ui_logger_Selected(self, sender, e):
        ''' refresh logs errors in combobox (debug mode)
        '''
        self.modelview.refresh_logger()
    

    def on_optionapi_path_check(self, sender, event):
        ''' valid the new path input by user with key Enter
        '''
        pass
        # fixme : doesn't refresh binding when press enter...
        #if event.Key == Key.Enter and sender.DataContext:
        #    ctxt = sender.DataContext
        #    if ctxt.enabled: # reset node
        #        ctxt.enabled = False
        #    ctxt.enabled = True




