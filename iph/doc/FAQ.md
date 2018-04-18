
## An error appears when launching *iph* inside Revit through RevitPythonShell ? 

    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "C:\Users\User\AppData\Roaming\RevitPythonShell2018\iph\__init__.py", line 23, in <module>
      File "C:\Users\User\AppData\Roaming\RevitPythonShell2018\iph\main.py", line 6, in <module>
    IOError: System.IO.IOException: Could not add reference to assembly IronPython.Wpf
    ...
This one comes from a DLL package out of date. Check if you have the latest version of IronPython (2.7.7), then try to replace 2 DLL in this folder (save them before):

   **C:\Program Files (x86)\RevitPythonShell2018**
       
- IronPython.dll  from **C:\Program Files (x86)\IronPython 2.7**
- IronPython.Wpf.dll  from  **C:\Program Files (x86)\IronPython 2.7\DLLs**
    
    