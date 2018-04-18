from System.Windows import (MessageBox,
    MessageBoxButton, MessageBoxImage, 
    MessageBoxResult)


#                               #
#          DIALOG BOXES
#                               #

def ok(message=''):
    MessageBox.Show(message, 'iph', MessageBoxButton.OK)


def ok_help(message=''):
    MessageBox.Show(message, 'iph',
                    MessageBoxButton.OK, MessageBoxImage.Warning)


def ok_error(message=''):
    """ ok + image
    """
    MessageBox.Show('Error : ' + message, "iph is Sorry",
                    MessageBoxButton.OK, MessageBoxImage.Error)


def ok_or_not(question=''):
    """ simple Yes/No
    """
    dial = MessageBox.Show(question, 'iph', MessageBoxButton.YesNo)
    return dial == MessageBoxResult.Yes


def ok_no_cancel(question=''):
    """ cancel = None
        yes/no = True/False
    """
    dial = MessageBox.Show(question, 'iph', MessageBoxButton.YesNoCancel)

    action = None
    if dial == MessageBoxResult.Yes:
        action = True
    elif dial == MessageBoxResult.No:
        action = False
    return action
