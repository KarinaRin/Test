import re
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _


class MinimumLengthValidator:
    def __init__(self, min_length=8):
        self.min_length = min_length

    def validate(self, password, user=None):
        if len(password) < self.min_length:
            raise ValidationError(
                _("Пароль не должен быть короче %(min_length)d символов."),
                code='Пароль слишком короткий',
                params={'min_length': self.min_length},
            )

    def get_help_text(self):
        return _(
            "Пароль не должен быть короче %(min_length)d символов."
            % {'min_length': self.min_length}
        )


class NumberValidator:
    def validate(self, password, user=None):
        if not re.search(r'\d', password):
            raise ValidationError(
                _("Пароль должен содержать хотя бы одну цифру."),
                code='Пароль не имеет цифр',
            )

    def get_help_text(self):
        return _(
            "Ваш пароль должен содержать хотя бы одну цифру."
        )


class LetterValidator:
    def validate(self, password, user=None):
        if not re.search(r'[A-Za-z]', password):
            raise ValidationError(
                _("Пароль должен содержать хотя бы одну букву верхнего или нижнего регистра."),
                code='Пароль не имеет букв',
            )

    def get_help_text(self):
        return _(
            "Пароль должен содержать хотя бы одну букву верхнего или нижнего регистра."
        )
