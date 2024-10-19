from django import forms
from food_delivery.models import Order,Menu

class OrderForm(forms.ModelForm):
    first_name = forms.CharField(max_length=50, label='Имя')
    surname = forms.CharField(max_length=60, label='Фамилия', required=False)
    address = forms.CharField(max_length=100, label='Адрес')
    dishes = forms.ModelMultipleChoiceField(
        queryset=Menu.objects.none(),
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}),
        label="Выберите блюда"
    )

    class Meta:
        model = Order
        fields = ['first_name', 'surname', 'address', 'dishes', 'promocode', 'comment']

    def __init__(self, restaurant=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})

        if restaurant:
            self.fields['dishes'].queryset = Menu.objects.filter(id_rest=restaurant)