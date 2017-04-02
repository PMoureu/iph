# Running scheme

After init and startup, everything begins in the treeview, with the options to target an API :
- all API/modules saved in options are resolved and displayed as a root node, allowing a manual exploration.

- Each object explored is wrapped in a model to provide special details (icon, members, type, doc, values....) 
- This model is given to tree items at first, then to tabs items or datagrid table depending on your actions.
When you select a node, the modelview transmits its model to the current tab, which will extract all details needed.

- For the tree logic, all children members are generated when a node is expanded, 
bindings complete the job to refresh views.

Talking about bindings, i used Observablecollections first.
Then i implemented the INotifyPropertyChanged class to relay changes more easily.
Attributes of items in ObservableCollection don't trigger changes and i needed that to update views (__ doc __ workaround)




# Project pattern


Let's make it simple, the relevant part is in the iph.core folder, the main manager is kind of top layer.

Then i tried to follow a classic MVVMMVMVM pattern:

### Main manager (main.py):
The main manager just wraps the other components and deals with settings, it's not part of MV pattern.

  - loads the settings
  - init/check the main components
  - close app
  
### View (ui.xaml + ui.py):
- most of user events are handled in the code-behind, calling modelview methods to update bindings  
- the main datacontext is set to the modelview

### Modelview (modelview.py + tree.py + tabs.py):
Gathers all sub-components to control bindings, 
also manages the tabs list and autocompletion logic.

- sub treemanager : tree.py (manage the tree content linked to options saved)
- sub tabitems : tabs.py (manage datagrid logic)
    
### Model (basemodel.py + analysis):
Base class for all inspected objects
- analyses and filters to provide the appropriate representation (doc, value)








