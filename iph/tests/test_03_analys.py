''' test module for analysis
'''
import os
import clr
import System
from System.Collections.ObjectModel import ObservableCollection
from iph.ana.analysis import *
from iph.ana.anatable import TYPES_TABLE
from iph.core.basemodel import ModelObject

def functiontest(arg):
    pass

sequence_test = [ 
    (clr, TYPES_TABLE['module']),
    (System, TYPES_TABLE['namespace#']),
    (System.Activator, TYPES_TABLE['classtype']),
    (System.Activator.CreateInstance, TYPES_TABLE['builtin_function_or_method']),
    (System.AttributeTargets , TYPES_TABLE['enumtype']),
    (System.AppContext.BaseDirectory , TYPES_TABLE['getset_descriptor']),
    (System.Action,  TYPES_TABLE['type-collision']),
    (System.Windows.Window().Visibility, TYPES_TABLE['subenumtype']),
    (System.Windows.Window().Activated, TYPES_TABLE['BoundEvent']),
    (System.Windows.Window().UnloadedEvent, TYPES_TABLE['RoutedEvent']),
    (os._Environ, TYPES_TABLE['classobj']),
    (None, TYPES_TABLE['NoneType']),
    ('test str', TYPES_TABLE['str']),
    (True, TYPES_TABLE['bool']),
    (False, TYPES_TABLE['bool']),
    (8, TYPES_TABLE['int']),
    (-8, TYPES_TABLE['int']),
    (8.8, TYPES_TABLE['float']),
    (-8.8, TYPES_TABLE['float']),
    ([8,'te', None], TYPES_TABLE['list']),
    ({'icon':'dict', 
     'doc' : get_std_doc}, TYPES_TABLE['dict']),
    ((8, 'rr'), TYPES_TABLE['tuple']),
    ({8,8,8,8}, TYPES_TABLE['set']),
    (ObservableCollection[object](), TYPES_TABLE['listtype']),
    (functiontest, TYPES_TABLE['function']),
    (ModelObject, TYPES_TABLE['class']),
    (ModelObject('test'), TYPES_TABLE['class']),
    (ModelObject('test').get_doc, TYPES_TABLE['instancemethod'])
]

def test_check_types_table():
    for k, val in TYPES_TABLE.items():
        assert len(val) == 5
        assert val.has_key('icon')
        assert val.has_key('category')
        assert val.has_key('members')
        assert val.has_key('value')
        assert val.has_key('doc')

def test_get_model_details_python_type():
    res = get_model_details(ModelObject)
    assert res['category'] == 'prop'

def test_get_model_details_python_instance():
    res = get_model_details(ModelObject(None))
    assert res['category'] == 'prop'

def test_sequence_details():
    for elem, exp in sequence_test:
        res = ModelObject(elem)
        assert res.category == exp['category']


