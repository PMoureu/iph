import clr

clr.AddReference('IronPython')
clr.AddReference('IronPython.Wpf')
clr.AddReference('System.Windows')
clr.AddReference('PresentationCore')
clr.AddReference("System.Xaml")
clr.AddReference("PresentationFramework")
clr.AddReference('WindowsBase')

from System.Windows import Application

import iph
from core.ui import MainForm
from core.modelview import ModelView
from core.config import *
from iph import logger, DIR_PATH

def get_hostname():
    import clr
    clr.AddReference('System.Windows.Forms')
    import System.Windows.Forms as forms
    return forms.Application.ProductName


hostname = get_hostname()

class Manager(object):
    """ Main control on the app
        init all components and launch the form 
        handle the exit and saves some convenient settings
    """
    def __init__(self):
        super(Manager, self).__init__()
        logger.info('iph starting in {}'.format(hostname))
        self.app = None
        self.mode_dbg = False
        self.is_revit_host = 'Autodesk' in hostname
        self.modelview = None
        self.main_form = None
        self.settings_file = os.path.join(DIR_PATH, 'settings.json')
        self.settings = load_settings_from_file(self.settings_file)

    def init_components(self, target=None):
        """ init modelview and main form
        """
        logger.debug('Loading Modelview...')
        self.modelview = ModelView(self)
        if self.mode_dbg:
            self.modelview.debug(self)

        logger.debug('Loading UI...')
        if self.modelview.ready:
            self.main_form = MainForm(self)
            self.modelview.init(target)
        else:
            ok_error('Sorry, modelview cannot start')

    def start_app(self):
        """ function called from __init__
            display the window
        """
        if self.main_form.ready and self.modelview.ready:
            
            if 'Autodesk' not in hostname:
                # ok in standalone, but makes Revit crash
                self.app = Application()  
                self.app.DispatcherUnhandledException += self.on_run_exception
                self.app.Run(self.main_form)
            else:
                self.main_form.Show()  # ShowDialog
        else:
            ok_error('Sorry, a component cannot start')

    def exit_app(self):
        """ "handle" the exit, TODO some cleanup...
        """
        
        if self.mode_dbg:
            self.log_out()
        # self.Dispatcher.Invoke(lambda *_: self.win.Close())

        if self.save_settings_and_quit():  # else cancel by user

            if not self.is_revit_host:
                logger.debug('app exit (standalone)')
                self.app.DispatcherUnhandledException -= self.on_run_exception
                Application.Current.Shutdown()
                # ok in standalone, but makes Revit crash

            else:
                logger.debug('app exit (revit context)')
                self.main_form.Close()  # crash in standalone

            iph.SESSION = None

    def save_settings_and_quit(self):
        """ check if changes in settings and ask for save or cancel
            window pos is saved anyway
        """
        _exit = True
        try:
            self.settings['window']['Left'] = self.main_form.Left
            self.settings['window']['Top'] = self.main_form.Top
            self.settings['window']['Width'] = self.main_form.Width
            self.settings['window']['Height'] = self.main_form.Height

            new_targets = [api.get_json()
                           for api in self.modelview.treemanager.list_options]
            
            if not new_targets == self.settings['api_set']:
                
                action_user = ok_no_cancel('Save the targets changes ?')
                if action_user:
                    self.settings['api_set'] = new_targets

                elif action_user is None:
                    _exit = False
            if _exit:
                save_settings_to_file(self.settings, self.settings_file)
            
        except Exception as error:
            logger.error('save_settings failed :\n' + str(error))

        finally:
            return _exit

    def log_out(self):
        """ logs the 100 last errors stacked in logger when app is closing
        """
        logs = logger.errors[:100]
        if logs:
            import time
            ldate = time.strftime('%d %b %Y %X')
            with open(os.path.join(DIR_PATH, 'logs', 'session.log'), 'w') as fileout:
                fileout.write(ldate+'\n')
                for er in logs:
                    fileout.write(str(er)+'\n')

    #                               #
    #             EVENTS
    #                               #
    def on_run_exception(self, sender, event):
        """
            catch runtime exception when running alone
        """
        msg = str(event.Exception.Message)
        ok_error(msg)
        logger.error('Runtime exception :\n' + msg)
        event.Handled = True

    def __repr__(self):
        return 'Main App Manager (Debug: {})'.format(self.mode_dbg)
