from django import forms

class UserForm(forms.Form):
    name = forms.CharField(label = "Имя клиента")
    возраст_клиента = forms.IntegerField(label = "Возраст клиента")

class UserForm(forms.Form):
    basket = forms.BooleanField(label = "Положить в корзину", required=False)

class UserForm(forms.Form):
    vyb = forms.NullBooleanField(label="Вы поедете в Сочи эти летом?")

class UserForm(forms.Form):
    name = forms.CharField(label="Имя клиента", max_length=15, help_text="ФИО не более 15 символов")

class UserForm(forms.Form):
    email = forms.EmailField(label="Электронный адрес", help_text="Обязательный символ - @")

class UserForm(forms.Form):
    ip_address = forms.GenericIPAddressField(label="IP адрес", help_text="Пример формата 192.0.2.0")

class UserForm(forms.Form):
    name = forms.CharField(label="Имя клиента", min_length=3)
    age = forms.IntegerField(label="Возраст клиента",min_value=1, max_value=100)
    required_css_class = "field"
    error_css_class = "error"

class UserForm(forms.Form):
    name = forms.CharField(label="Имя клиента", widget=forms.TextInput(attrs={"class": "myfield"}))
    age = forms.IntegerField(label="Возраст клиента", widget=forms.NumberInput(attrs={"class": "myfield"}))