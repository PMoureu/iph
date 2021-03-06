"""
    sets of excluded members 
    You can un-hide a member by commenting a line
"""

# System Object inherited + 3 first
ATTR_OBJECT = {
    '__dict__',
    '__module__',
    '__weakref__',
    'Contains',
    'CopyTo',
    'Count',
    'CreateExpression',
    'Equals',
    'GetEnumerator',
    'GetHashCode',
    'GetType',
    'IndexOf',
    'Item',
    'MemberwiseClone',
    'ReferenceEquals',
    'ToString',
    '__add__',
    '__class__',
    '__contains__',
    '__delattr__',
    '__doc__',
    '__eq__',
    '__format__',
    '__ge__',
    '__getattribute__',
    '__getitem__',
    '__getnewargs__',
    '__getslice__',
    '__gt__',
    '__hash__',
    '__init__',
    '__iter__',
    '__le__',
    '__len__',
    '__lt__',
    '__mul__',
    '__ne__',
    '__new__',
    '__radd__',
    '__reduce__',
    '__reduce_ex__',
    '__repr__',
    '__rmul__',
    '__setattr__',
    '__sizeof__',
    '__str__',
    '__subclasshook__',
    'count',
    'index'
}

# Revit Element inherited
ATTR_REVIT = {
    'ArePhasesModifiable',
    'AssemblyInstanceId',
    'BoundingBox',
    'CanBeHidden',
    'CanBeLocked',
    'CanHaveAnalyticalModel',
    'CanHaveTypeAssigned',
    # 'Category',
    'ChangeTypeId',
    'CreatedPhaseId',
    'DeleteEntity',
    'DemolishedPhaseId',
    'DesignOption',
    'Dispose',
    # 'Document',
    'Equals',
    # 'Geometry',
    'GetAnalyticalModel',
    'GetAnalyticalModelId',
    'GetChangeTypeAny',
    'GetChangeTypeElementAddition',
    'GetChangeTypeElementDeletion',
    'GetChangeTypeGeometry',
    'GetChangeTypeParameter',
    'GetEntity',
    'GetEntitySchemaGuids',
    'GetExternalFileReference',
    'GetExternalResourceReference',
    'GetExternalResourceReferences',
    'GetGeneratingElementIds',
    'GetGeometryObjectFromReference',
    'GetHashCode',
    'GetMaterialArea',
    'GetMaterialIds',
    'GetMaterialVolume',
    'GetMonitoredLinkElementIds',
    'GetMonitoredLocalElementIds',
    'GetOrderedParameters',
    'GetParameterFormatOptions',
    'GetParameters',
    'GetPhaseStatus',
    'GetType',
    'GetTypeId',
    'GetValidTypes',
    'GroupId',
    'HasPhases',
    # 'Id',
    'IsExternalFileReference',
    # ' IsHidden',
    'IsMonitoringLinkElement',
    'IsMonitoringLocalElement',
    'IsPhaseCreatedValid',
    'IsPhaseDemolishedValid',
    'IsTransient',
    'IsValidObject',
    'IsValidType',
    # 'LevelId',
    # 'Location',
    'LookupParameter',
    'MemberwiseClone',
    # 'Name',
    'OwnerViewId',
    # 'Parameter',
    # 'Parameters',
    # 'ParametersMap',
    'Pinned',
    'ReferenceEquals',
    'RefersToExternalResourceReference',
    'RefersToExternalResourceReferences',
    'ReleaseUnmanagedResources',
    'SetEntity',
    'ToString',
    # 'UniqueId',
    'ViewSpecific',
    'WorksetId',
    'getBoundingBox',
    'setElementType',
    'ToString',
    '__add__',
    '__class__',
    '__contains__',
    '__delattr__',
    '__doc__',
    '__eq__',
    '__format__',
    '__ge__',
    '__getattribute__',
    '__getitem__',
    '__getnewargs__',
    '__getslice__',
    '__gt__',
    '__hash__',
    '__init__',
    '__iter__',
    '__le__',
    '__len__',
    '__lt__',
    '__mul__',
    '__ne__',
    '__new__',
    '__radd__',
    '__reduce__',
    '__reduce_ex__',
    '__repr__',
    '__rmul__',
    '__setattr__',
    '__sizeof__',
    '__str__',
    '__subclasshook__'
}
