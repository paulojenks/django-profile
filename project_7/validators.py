import re

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _


class NumberValidator(object):
    def __init__(self, min_digits=1):
        self.min_digits = min_digits

    def validate(self, password, user=None):
        if not len(re.findall('\d', password)) >= self.min_digits:
            raise ValidationError(
                _("The password must contain at least {} digit(s), 0-9.".format(self.min_digits)),
                code='password_no_number',
            )

    def get_help_text(self):
        return _(
            "Your password must contain at least {} digit, 0-9.".format(self.min_digits)
        )


class SymbolValidator(object):
    def __init__(self, min_digits=1):
        self.min_digits = min_digits

    def validate(self, password, user=None):
        if not len(re.findall("[~\!@#\$%\^&\*\(\)_\+{}\":;'\[\]]", password)) >= self.min_digits:
            raise ValidationError(
                _("The password must contain at least {} special character.".format(self.min_digits)),
                code='password_no_number',
            )

    def get_help_text(self):
        return _(
            "Your password must contain at least {} special character".format(self.min_digits)
        )


class LowercaseValidator(object):
    def __init__(self, min_digits=1):
        self.min_digits = min_digits

    def validate(self, password, user=None):
        if not re.findall('[a-z]', password):
            raise ValidationError(
                _("The password must contain at least {} lowercase letter, a-z.".format(self.min_digits)),
                code='password_no_lower',
            )

    def get_help_text(self):
        return _(
            "The password must contain at least {} lowercase letter, a-z.".format(self.min_digits)
        )


class UppercaseValidator(object):
    def __init__(self, min_digits=1):
        self.min_digits = min_digits

    def validate(self, password, user=None):
        if not re.findall('[A-Z]', password):
            raise ValidationError(
                _("The password must contain at least {} uppercase letter, a-z.".format(self.min_digits)),
                code='password_no_lower',
            )

    def get_help_text(self):
        return _(
            "The password must contain at least {} upppercase letter, a-z.".format(self.min_digits)
        )