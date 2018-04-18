from System.ComponentModel import PropertyChangedEventArgs, INotifyPropertyChanged


class BaseNotifier(INotifyPropertyChanged):
    """ Base class for all modelviews
    """
    def __init__(self):
        self._events = []

    def add_PropertyChanged(self, value):
        self._events.append(value)

    def remove_PropertyChanged(self, value):
        self._events.remove(value)

    def NotifyPropertyChanged(self, field):
        for event in self._events:
            event(self, PropertyChangedEventArgs(field))
