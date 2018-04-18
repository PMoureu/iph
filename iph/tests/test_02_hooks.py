from iph.ana.syshook import *


def test_try_resolve_path_python_single_path():
    res = try_resolve_path('iph')
    import iph as expect
    assert res == expect


def test_try_resolve_path_python_composed_path():
    res = try_resolve_path('iph.core.basemodel')
    import iph.core.basemodel as expect
    assert res == expect


def test_try_resolve_path_clr_single_path():
    res = try_resolve_path('System')
    import System as expect
    assert res == expect


def test_try_resolve_path_comp_path():
    res = try_resolve_path('System.Windows.Controls')
    import System.Windows.Controls as expect
    assert res == expect


def test_try_resolve_path_creepy_path():
    res = try_resolve_path('creepy path')
    assert res is None


def test_try_resolve_path_creepy_path2():
    res = try_resolve_path('@.Crap..Path.+')
    assert res is None


def test_try_resolve_path_clr_not_loaded():
    res = try_resolve_path('IronPython.Wpf')
    assert res is not None


def test_try_resolve_path_single_path():
    res = try_resolve_path('iph')
    import iph as expect
    assert res == expect
