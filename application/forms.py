from django import forms
from django.forms import ValidationError
from .models import Comment, Order
from django.core.exceptions import ValidationError
from phone_field import PhoneField

class AddComment(forms.Form):  # наследование
    title = forms.CharField(max_length=100, label="Адрес доставки:")
    #subtitle = forms.CharField(max_length=300, label="Адрес доставки:")
    content = forms.CharField(widget=forms.Textarea(), label="Описание:")
    image = forms.ImageField(required=False, label="Можете прикрепить фото")
    

class AddOrder(forms.Form):  # наследование
    order_adress = forms.CharField(max_length=300, label="Введите адрес доставки:")
    order_tel = forms.CharField(max_length=18, label="Введите ваш номер телефона с кодом оператора:")
    order_description = forms.CharField(widget=forms.Textarea(), label="Ваши пожелания:") 
    order_type = forms.ChoiceField(choices=Order.ORDER_TYPE, label="Выберите тип услуги")
    

#def clean_order_adress(self):
#
#    order_adress_data = self.cleaned_data['order_adress']
#    order_description_data = self.cleaned_data['order_description']
#    
#    if order_adress_data and order_description_data:  # поля обязательны для заполнения
#        return order_adress_data, 
#    else:
#        raise ValidationError("Поле должно быть заполнено")    