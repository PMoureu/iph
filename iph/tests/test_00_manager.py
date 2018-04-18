""" test module for manager functions
"""


def test_instance_manager():
    """ test init and settings
    """
    from iph.main import Manager

    res = Manager()
    assert isinstance(res, Manager)


def test_manager_settings():
    """ test init and settings
    """
    from iph.main import Manager
    res = Manager()
    assert isinstance(res.settings, dict)
    assert 'window' in res.settings
    assert 'api_set' in res.settings


def test_manager_is_revit_host_true():
    from iph.main import Manager
    import iph
    iph.main.hostname = 'Autodesk'
    res = Manager()
    assert res.is_revit_host is True


def test_manager_is_revit_host_false():
    from iph.main import Manager
    import iph
    iph.main.hostname = 'IronPython'
    res = Manager()
    assert res.is_revit_host is False


def test_instance_modelview():
    from iph.main import Manager
    from iph.core import modelview
    res = modelview.ModelView(Manager())
    assert isinstance(res, modelview.ModelView)
    assert res.ready is True


def test_instance_view():
    from iph.main import Manager
    from iph.core import modelview
    from iph.core import ui
    man = Manager()
    man.modelview = modelview.ModelView(man)
    res = ui.MainForm(man)
    assert isinstance(res, ui.MainForm)
    assert res.ready is True
