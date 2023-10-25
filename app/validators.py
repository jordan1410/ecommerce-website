from wtforms import SelectMultipleField, widgets
from wtforms.validators import StopValidation
import re


# Validator field for list of checkboxes
class MultiCheckboxField(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()


# Validator to make sure at least one item is checked off
class AtLeastOneChecked():
    def __init__(self, message=None):
        if not message:
            message = 'At least one option must be selected.'
        self.message = message

    def __call__(self, form, field):
        if len(field.data) == 0:
            raise StopValidation(self.message)


# Validator to make sure at most one item is checked off
class AtMostOneChecked():
    def __init__(self, message=None):
        if not message:
            message = 'Only one can be selected'
        self.message = message

    def __call__(self, form, field):
        if len(field.data) > 1:
            raise StopValidation(self.message)


# Validator to only allow alphabet, spaces, and hyphen characters
class AlphaSpaceHyphen():
    def __init__(self, message=None):
        if not message:
            message = "Accepted characters: a-Z, '-', space"
        self.message = message

    def __call__(self, form, field):
        if not re.match('^[a-zA-Z\s\-]+$', field.data):
            raise StopValidation(self.message)


# Validator to only allow alphabet and space characters
class AlphaSpace():
    def __init__(self, message=None):
        if not message:
            message = 'Accepted characters: a-Z, space'
        self.message = message

    def __call__(self, form, field):
        if not re.match('^[a-zA-Z\s]+$', field.data):
            raise StopValidation(self.message)


# Validator to only allow alphabet characters
class Alpha():
    def __init__(self, message=None):
        if not message:
            message = 'Accepted characters: a-Z'
        self.message = message

    def __call__(self, form, field):
        if not re.match('^[a-zA-Z]+$', field.data):
            raise StopValidation(self.message)


# Validator to only allow viable zipcode format (0-9 and '-')
class ValidZipCode():
    def __init__(self, message=None):
        if not message:
            message = "Accepted characters: 0-9, '-'"
        self.message = message

    def __call__(self, form, field):
        if not re.match('^[0-9\-]+$', field.data):
            raise StopValidation(self.message)
