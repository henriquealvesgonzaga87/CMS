from django import forms
from .models import Customer


class DateImput(forms.DateInput):
    input_type = "date"


class CustomerForm(forms.ModelForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    birth_date = forms.DateField(widget=DateImput())
    area_code = forms.RegexField(regex=r"^\+?1?[0-9]{2}$", error_messages={"invalid": "Number not valid"})
    phone_number = forms.RegexField(regex=r"^\+?1?[0-9]{9,15}$", error_messages={"invalid": "Number not valid"})
    country = forms.CharField()

    class Meta:
        model = Customer
        fields = (
            "first_name",
            "last_name",
            "email",
            "birth_date",
            "area_code",
            "phone_number",
            "country",
            "state",
            "city"
        )
