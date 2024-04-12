
from django import forms
from restaurant.models import Menu

class MenuCreation(forms.Form):

    # pylint: disable=too-few-public-methods
    image = forms.ImageField()
    class Meta:
        model = Menu
        fields = ['image', 'name','description','type', 'quantity','status','price']
