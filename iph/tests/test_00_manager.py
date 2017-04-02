''' test module for manager functions
'''

def test_instance_manager():
    ''' test init and settings
    '''
    from iph.main import Manager

    res = Manager()
    assert isinstance(res, Manager)


def test_manager_settings():
    ''' test init and settings
    '''
    from iph.main import Manager
    res = Manager()
    assert isinstance(res.settings, dict)
    assert res.settings.has_key('window')
    assert res.settings.has_key('api_set')

def test_manager_is_revit_host_True():
    from iph.main import Manager
    import iph
    iph.main.hostname = 'Autodesk'
    res = Manager()
    assert res.is_revit_host == True


def test_manager_is_revit_host_False():
    from iph.main import Manager
    import iph
    iph.main.hostname = 'IronPython'
    res = Manager()
    assert res.is_revit_host == False


def test_instance_modelview():
    from iph.main import Manager
    from iph.core import modelview
    res = modelview.ModelView(Manager())
    assert isinstance(res, modelview.ModelView)
    assert res.ready == True


def test_instance_view():
    from iph.main import Manager
    from iph.core import modelview
    from iph.core import ui
    man = Manager()
    man.modelview = modelview.ModelView(man)
    res = ui.MainForm(man)
    assert isinstance(res, ui.MainForm)
    assert res.ready == True



