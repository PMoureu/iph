""" Holds the main index to match types to specific model details.
    You can affect other templates or disable whats not relevant for you
    - check the name type as given by type(refobject).__name__
    - Add new functions in analysis to describe the content
    - Create/modify an entry in TYPES_TABLE
"""
from details import *
from members import *

SYS_TYPES = {
    'System.ArgIterator',
    'System.ArraySegment`1',
    'System.Boolean',
    'System.Byte',
    'System.Char',
    'System.ConsoleKeyInfo',
    'System.DateTime',
    'System.DateTimeOffset',
    'System.Decimal',
    'System.Double',
    'System.Guid',
    'System.Int16',
    'System.Int32',
    'System.Int64',
    'System.IntPtr',
    'System.ModuleHandle',
    'System.RuntimeArgumentHandle',
    'System.RuntimeFieldHandle',
    'System.RuntimeMethodHandle',
    'System.RuntimeTypeHandle',
    'System.SByte',
    'System.Single',
    'System.TimeSpan',
    'System.TypedReference',
    'System.UInt16',
    'System.UInt32',
    'System.UInt64',
    'System.UIntPtr',
    'System.Void'
}

WIN_TYPES = {
    'System.Windows.CornerRadius',
    'System.Windows.DependencyPropertyChangedEventArgs',
    'System.Windows.Duration',
    'System.Windows.FigureLength',
    'System.Windows.FontStretch',
    'System.Windows.FontStyle',
    'System.Windows.FontWeight',
    'System.Windows.GridLength',
    'System.Windows.Int32Rect',
    'System.Windows.LocalValueEntry',
    'System.Windows.LocalValueEnumerator',
    'System.Windows.Point',
    'System.Windows.Rect',
    'System.Windows.RoutedEventHandlerInfo',
    'System.Windows.Size',
    'System.Windows.Thickness',
    'System.Windows.ValueSource',
    'System.Windows.Vector'
}


TYPES_TABLE = {
    #                               #
    #         DEFAULTS TYPES
    #                               #
    
    'listtype': {
        'icon': 'newcoll',
        'category': 'prop',
        'members': get_list_members,
        'value': get_list_val,
        'doc': get_doc
    },
    
    'unknown':  {
        'icon': 'unknown',
        'category': 'prop',
        'members': get_members_default,
        'value': get_std_value,
        'doc': get_doc
    },
    
    'NoneType': {
        'icon': 'prop',
        'category': 'prop',
        'members': None,
        'value': get_std_value,
        'doc': get_std_doc
    },
    
    'systype': {
        'icon': 'prop',
        'category': 'prop',
        'members': None,
        'value': get_std_value,
        'doc': get_doc
    },
    
    'wintype': {
        'icon': 'prop',
        'category': 'prop',
        'members': get_members_default,
        'value': get_std_value,
        'doc': get_doc
    },
    
    'revitclass': {
        'icon': 'class',
        'category': 'prop',
        'members': get_members_filt_revit,
        'value': get_std_value,
        'doc': get_doc
    },

    #                               #
    #        MODULES  TYPES
    #                               #

    'module':   {
        'icon': 'module',
        'category': 'module',
        'members': get_members_default,
        'value': get_std_value,
        'doc': get_doc
    },

    'namespace#': {
        'icon': 'modulec',
        'category': 'module',
        'members': get_members_default,
        'value': get_std_value,
        'doc': get_doc
    },
    
    #                               #
    #        BUILTIN  TYPES
    #                               #
    
    'str': {
        'icon': 'prop',
        'category': 'prop',
        'members': None,
        'value': get_std_value,
        'doc': get_std_doc
    },
    
    'bool': {
        'icon': 'prop',
        'category': 'prop',
        'members': None,
        'value': get_std_value,
        'doc': get_std_doc
    },
    
    'int': {
        'icon': 'prop',
        'category': 'prop',
        'members': None,
        'value': get_std_value,
        'doc': get_std_doc
    },
    
    'float': {
        'icon': 'prop',
        'category': 'prop',
        'members': None,
        'value': get_std_value,
        'doc': get_std_doc
    },
    
    'list': {
        'icon': 'list',
        'category': 'prop',
        'members': get_list_members,
        'value': get_list_val,
        'doc': get_std_doc
    },
    
    'dict': {
        'icon': 'dict',
        'category': 'prop',
        'members': get_dict_members,
        'value': get_dict_val,
        'doc': get_std_doc
    },
    
    'tuple': {
        'icon': 'list',
        'category': 'prop',
        'members': get_list_members,
        'value': get_list_val,
        'doc': get_std_doc
    },
    
    'set': {
        'icon': 'list',
        'category': 'prop',
        'members': get_list_members,
        'value': get_list_val,
        'doc': get_std_doc
    },
    
    #                               #
    #         EVENTS TYPES
    #                               #
    
    'RoutedEvent': {
        'icon': 'interface',
        'category': 'event',
        'members': None,
        'value': get_std_value,
        'doc': get_rout_event_doc
    },
    
    'BoundEvent': {
        'icon': 'interface',
        'category': 'event',
        'members': None,
        'value': get_event_val,
        'doc': get_event_doc
    },
    
    #                               #
    #        PROPERTY TYPES
    #                               #
    'DependencyProperty': {
        'icon': 'prop',
        'category': 'prop',
        'members': None,
        'value': get_std_value,
        'doc': get_doc
    },
    
    'indexer#': {
        'icon': 'prop',
        'category': 'prop',
        'members': None,
        'value': get_std_value,
        'doc': get_indexer_doc
    },
    
    'Array[MethodInfo]': {
        'icon': 'list',
        'category': 'prop',
        'members': get_list_members,
        'value': get_std_value,
        'doc': get_doc
    },
    
    'getset_descriptor': {
        'icon': 'prop',
        'category': 'prop',
        'members': None,
        'value': get_std_value,
        'doc': get_indexer_doc
    },
    
    'flags': {
        'icon': 'prop',
        'category': 'prop',
        'members': None,
        'value': get_std_value,
        'doc': get_doc
    },

    'type-collision': {
        'icon': 'prop',
        'category': 'collision',
        'members': None,
        'value': get_std_value,
        'doc': get_doc
    },

    #                               #
    #        CLASS TYPES
    #                               #

    'instance': {
        'icon': 'class',
        'category': 'instance',
        'members': get_members_default,
        'value': get_std_value,
        'doc': get_doc
    },

    'class': {
        'icon': 'class',
        'category': 'prop',
        'members': get_members_default,
        'value': get_std_value,
        'doc': get_doc
    },
    
    'classobj': {
        'icon': 'class',
        'category': 'prop',
        'members': get_members_default,
        'value': get_std_value,
        'doc': get_doc
    },
    
    #                               #
    #        FUNCTIONS TYPES
    #                               #
    
    'function': {
        'icon': 'function',
        'category': 'function',
        'members': None,
        'value': get_std_value,
        'doc': get_doc
    },
    
    'method_descriptor': {
        'icon': 'function',
        'category': 'function',
        'members': None,
        'value': get_std_value,
        'doc': get_doc
    },
    
    'builtin_function_or_method': {
        'icon': 'function',
        'category': 'function',
        'members': None,
        'value': get_std_value,
        'doc': get_doc
    },
    
    'GenericBuiltinFunction': {
        'icon': 'function',
        'category': 'function',
        'members': None,
        'value': get_std_value,
        'doc': get_doc
    },
    
    'instancemethod': {
        'icon': 'function',
        'category': 'function',
        'members': None,
        'value': get_std_value,
        'doc': get_doc
    },
    
    #                               #
    #            CLR TYPES
    #                               #
    
    'enumtype': {
        'icon': 'list',
        'category': 'prop',
        'members': get_members_enum,
        'value': get_value_enum,
        'doc': get_doc
    },
    
    'subenumtype': {
        'icon': 'list',
        'category': 'prop',
        'members': get_members_subenum,
        'value': get_value_subenum,
        'doc': get_doc
    },
    
    'classtype': {
        'icon': 'class',
        'category': 'prop',
        'members': get_members_default,
        'value': get_std_value,
        'doc': get_class_doc
    },
    
    'subclasstype': {
        'icon': 'class',
        'category': 'prop',
        'members': get_members_default,
        'value': get_std_value,
        'doc': get_class_doc
    },
    
    'interface': {
        'icon': 'interface',
        'category': 'interface',
        'members': get_members_default,
        'value': get_std_value,
        'doc': get_doc
    },

    #                               #
    #            CUSTOM TYPES
    #                               #

    'revitparameter': {
        'name': get_revit_parameter_name,
        'icon': 'class',
        'category': 'parameter',
        'members': get_members_default,
        'value': get_revit_parameter_value,
        'doc': get_doc
    },


}
