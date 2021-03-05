from django import forms
import datetime
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _

class RenewBookForm(forms.Form):
    renewal_data = forms.DateField()

    def clean_renewal_data(self):
        data = self.cleaned_data['renewal_data']   

        if data < datetime.date.today():
            raise ValidationError(_('Invalid date renewak in past'))

        if data > datetime.date.today() + datetime.timedelta(weeks = 4):
            raise ValidationError(_('your dont more than 4 week'))

        return data