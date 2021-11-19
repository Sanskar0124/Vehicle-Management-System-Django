from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def name(value):
    if value=="" or len(value) > 10:
        raise ValidationError(
            _('%(value)s is not a valid name, Please eneter your valid name.'),
            params={'value': value},
        )

def ownerName(value):
    if value=="" or len(value) > 25:
        raise ValidationError(
            _('%(value)s is not a valid name, Please eneter your valid name.'),
            params={'value': value},
        )
    
def phoneNumber(value):
    number = str(value)
    if len(number) == 0 or len(number) > 12 or len(number) < 10:
        raise ValidationError(
            _('%(value)s is not a valid number, Please eneter your valid contact number.'),
            params={'value': number},
        )
        
def rcNumber(value):
    if len(value) == 0 or len(value) > 12 or len(value) < 12:
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

def vehicleNumber(value):
    if len(value) == 0 or len(value) > 10:
        raise ValidationError(
            _('%(value)s is not a valid number, Please eneter your valid contact number.'),
            params={'value': value},
        )