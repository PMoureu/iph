from iph.main import Manager
from iph.core import modelview
from iph.core import ui
from iph.core.tabs import TabViewItem
from iph.core.basemodel import ModelObject
from System.Windows import Window


def test_01_instance_tabitem():
    res = TabViewItem(ModelObject('simple'))
    assert isinstance(res, TabViewItem)

def test_02_update_grid_with_huge_members():
    man = Manager()
    man.modelview = modelview.ModelView(man)
    res = TabViewItem(ModelObject(ui.MainForm(man),'win'))
    assert len(res.datagrid) > 0

