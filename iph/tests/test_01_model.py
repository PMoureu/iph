""" test module for base model creation, only tests init attribution,
    analysis and details are tested in others modules
"""


def test_01_instance_model():
    from iph.core.basemodel import ModelObject
    res = ModelObject(None, 'none')
    assert isinstance(res, ModelObject)


def test_02_instance_model_ref():
    from iph.core.basemodel import ModelObject
    res = ModelObject(None, 'none')
    assert res.ref is None


def test_03_instance_model_name():
    from iph.core.basemodel import ModelObject
    res = ModelObject(None, 'testnone')
    assert res.name == 'testnone'


def test_03_instance_model_noname():
    from iph.core.basemodel import ModelObject
    res = ModelObject(12)
    assert res.name == 'int'


def test_04_instance_model_members():
    from iph.core.basemodel import ModelObject
    res = ModelObject(None, 'none')
    assert list(res.get_members()) == []


def test_05_instance_model_cat():
    from iph.core.basemodel import ModelObject
    res = ModelObject('teststring')    
    assert res.category == 'prop'
