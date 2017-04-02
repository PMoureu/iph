import sys
import clr
import gc
from System.Collections.ObjectModel import ObservableCollection
from iph import logger
from config import img_tree
from iph.ana.details import *
from iph.ana.members import *
from iph.core.basemodel import ModelObject
from iph.core import BaseNotifier


#                               #
#           TABS VIEW
#                               #

class TabViewItem(BaseNotifier):
    ''' represents a tab in the tabcontrol (main info + grid)
         holds the referenced model object
        
    '''
    def __init__(self, model):
        ''' init with a modelbase class
            (given by treenode or created with ModelObject(ref, name))
        '''
        super(TabViewItem, self).__init__()
        self.model = model
        self.maindoc = ''
        self.datagrid = []
        self.backup = []
        self.options_templates = []
        self.update_details()
        self.progress = 100
        
    
    def refresh(self, new_model):
        ''' called by modelview to update the current tab
        '''
        self.model = new_model
        self.update_details()
        self.NotifyPropertyChanged("model")

    def update_details(self):
        ''' use model details to fill main infos, 
            default filter option and datagrid
        '''
        ref = self.model.ref
        self.maindoc = self.model.name 
        self.maindoc += ' (Type : {} - Mem Size: {})'.format(
                        self.model.type, 
                        sys.getsizeof(ref))
        self.maindoc += '\nGetType() : ' + str(clr.GetClrType(type(ref)))
        self.maindoc += '\n'*2 + self.model.templ_value(ref)
        self.maindoc += '\n'*2 + str(self.model.templ_doc(ref))
        

        self.options_templates = [
            GridFilter('Template light', self.model.templ_members),
            GridFilter('All Members', get_members_no_filter)
            ]

        self.update_grid()
        self.NotifyPropertyChanged("maindoc")
        self.NotifyPropertyChanged("options_templates")

    def update_grid(self):
        ''' refresh grid rows from new model/new template filters
        '''
        self.datagrid = []
        gc.collect()
        try:
            for model in self.model.get_members():
                try:
                    self.datagrid.append(ModelGridRow(model))
                except Exception as error:
                    logger.error('update_grid row error : ' + str(error))

        except Exception as error:
            logger.error('update_grid template error : ' + str(error))

        self.backup = self.datagrid[:]
        self.NotifyPropertyChanged("datagrid")

    def filter_by_name(self, txtfilter=None):
        ''' creates a new filtered list for datagrid,
            restore the original when text is erased
        '''
        if not txtfilter:
            self.datagrid = self.backup
        else:
            self.datagrid = [row for row in self.backup 
                if row.model.name.upper().startswith(txtfilter.upper())]

        self.NotifyPropertyChanged("datagrid")

    def change_templ_memb(self, new_template):
        ''' replace template and refresh the grid
            arg: new template provided by combobox (bind options_templates)
        '''
        self.model.templ_members = new_template
        self.update_grid()

    def __repr__(self):
        if self.model:
            id = self.model.name + ' - '+ self.model.type
        return 'TabViewItem '+ id


#                               #
#         GRIDROW VIEW
#                               #

class ModelGridRow(BaseNotifier):
    ''' base subview item for the datagrid 
        holds the value and doc given by model
        and binds the model datas
    '''
    def __init__(self, model):
        super(ModelGridRow, self).__init__()
        self.model = model
        self.value = self.model.get_value()
        self.short_value = self.value[0:100]
        self.doc = ''
        self._row_selected = False
        self._doc_filled = False
        self.is_visible = True

    def set_doc(self):
        self.doc = self.model.get_doc()
        self.NotifyPropertyChanged("doc")


#                               #
#    DATAGRID OPTIONS FILTERS
#                               #

class GridFilter(object):
    ''' simple class to allow binding with option
    '''
    def __init__(self, name, filterfunc):
        self.name = name
        self.filter_funct = filterfunc