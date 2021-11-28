from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _



def validate_username(value):
    if value.isdigit():
        raise ValidationError(
            _(f'Имя пользователя не может состоять только из цифр'),
            params={'value': value},
        )

def validate_name(value):
    if not value.isalpha():
        raise ValidationError(
            _(f'Поля имя и фамилия не могут содержать цифры')
        )
