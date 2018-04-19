

# Example of script to launch analysis on selected objects 

This script can be saved as a macro within RevitPythonShell to open *iph* directly from any selected object in open models.
```
__window__.Close()
import iph

uidoc = __revit__.ActiveUIDocument
doc = __revit__.ActiveUIDocument.Document
   
selection = [doc.GetElement(id) 
                for id in __revit__.ActiveUIDocument.Selection.GetElementIds()]

if len(selection) == 1:
    iph.go(selection[0])
    
elif len(selection) > 1:
    iph.go(selection)
```