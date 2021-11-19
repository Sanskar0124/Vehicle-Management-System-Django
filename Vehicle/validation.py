from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def name(value):
    if value=="" or len(value) > 10:
        raise ValidationError(
            _('%(value)s is not a valid name, Please eneter your valid name.'),
            params={'value': value},
        )
    
def phoneNumber(value):
    if len(value) == 0 or len(value) > 12 or len(value) < 10:
        raise ValidationError(
            _('%(value)s is not a valid number, Please eneter your valid contact number.'),
            params={'value': value},
        )

def policyNumber(value):
    if len(value) == 0 or len(value) > 12 or len(value) < 12:
        raise ValidationError(
            _('%(value)s is not a valid number, Please eneter your valid contact number.'),
            params={'value': value},
        )

def pucNumber(value):
    if len(value) == 0 or len(value) > 7 or len(value) < 7:
        raise ValidationError(
            _('%(value)s is not a valid number, Please eneter your valid contact number.'),
            params={'value': value},
        )