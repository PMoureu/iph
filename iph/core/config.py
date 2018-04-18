import os
import json
from System import Uri
from System.Windows.Media.Imaging import BitmapImage
from iph import DIR_PATH, logger
from iph.utils.dialogs import *


# cannot load as window resources in xaml ? wrong path
def load_img(ipath): 
    return BitmapImage(Uri(os.path.join(DIR_PATH, ipath)))


img_tree = dict()
img_tree['class'] = load_img('img\constru.png')
img_tree['default'] = load_img('img\default.png')
img_tree['dict'] = load_img('img\dict.png')
img_tree['function'] = load_img('img\xfunc.png')
img_tree['interface'] = load_img('img\interface.png')
img_tree['list'] = load_img('img\list.png')
img_tree['modulec'] = load_img('img\modulc.png')
img_tree['module'] = load_img('img\modul.png')
img_tree['newcoll'] = load_img('img\collec.png')
img_tree['prop'] = load_img('img\prope.png')
img_tree['unknown'] = load_img('img\unknown.png')

DEFAULT_SETTINGS = dict()
DEFAULT_SETTINGS['window'] = {'Left': 10, 'Top': 10, 'Width': 800, 'Height': 600}

DEFAULT_SETTINGS['api_set'] = [
    {'name': 'Revit', 'path': 'Autodesk.Revit', 'enabled': False},
    {'name': 'main', 'path': '__main__', 'enabled': False},
    {'name': 'sys modules', 'path': 'sys.modules', 'enabled': False},
    {'name': 'System .Net', 'path': 'System', 'enabled': False},
    {'name': 'IronPython', 'path': 'IronPython', 'enabled': True}
]


def load_settings_from_file(file_path):
    """try to read settings from file in directory
        else return the defaults
        arg : path as string
    """
    try:
        with open(file_path, 'r') as jfile:
            settings = json.load(jfile)
                
    except Exception as error:
        settings = DEFAULT_SETTINGS
        if ok_or_not('Something wrong in the file, restore defaults settings ?'):
            save_settings_to_file(DEFAULT_SETTINGS, file_path)

        logger.error('load_settings_from_file failed :\n' 
                     + str(error))

    return settings


def save_settings_to_file(settings, file_path):
    """try to save settings to file
        arg : settings as dict, path as string
    """
    try:
        for opt in settings['api_set']:
            opt['enabled'] = bool(opt['enabled'])  # revit saves with uppercase bool ?
        with open(file_path, 'w') as jfile:
            json.dump(settings, jfile, indent=4, sort_keys=True)

    except Exception as error:
        logger.error('save_settings_to_file failed :\n' + str(error))


def replace_key_in_json(str_key, new_val, file_path):
    """ arg : str_key as string, new_val, path as string
    """
    try:
        saved_settings = load_settings_from_file(file_path)
        saved_settings[str_key] = new_val
        with open(file_path, 'w') as jfile:
            json.dump(saved_settings, jfile, indent=4, sort_keys=True)

    except Exception as error:
        logger.error('save_key_to_json failed :\n' + str(error))


# in progress...

def load_json_index():
    """ 1st attempt to use index for autocompletion and additional doc
    """
    try:
        with open(os.path.join(DIR_PATH, 'index_revit.json'), 'r') as jfile:
            index = json.load(jfile)
                
    except Exception as error:
        
        logger.error('load_json index :\n' + str(error))

    return index


def check_api_option(dict_api):
    """
    """
    is_valid = False
    if isinstance(dict_api['name'], str) and isinstance(dict_api['path'], str):
        is_valid = True

    return is_valid


def check_windows_settings():
    import ctypes
    user32 = ctypes.windll.user32
    screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
