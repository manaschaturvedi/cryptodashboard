from django import forms
from .choices import COINS_CHOICES,CURRENCY_CHOICES
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions

class UserCoinForm(forms.Form):
	coin = forms.ChoiceField(choices=COINS_CHOICES,initial=COINS_CHOICES[0][0])
	currency_type = forms.ChoiceField(choices=CURRENCY_CHOICES,initial=CURRENCY_CHOICES[0][0])
	total_investment = forms.IntegerField()
	units_owned = forms.FloatField()

	helper = FormHelper()
	helper.add_input(Submit('new-coin-form-button', 'Add', css_class='btn-primary'))
	helper.form_method = 'POST'