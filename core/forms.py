from django.forms import ModelForm
from .models import Item
class CreateItemForm(ModelForm):
    class Meta:
        model = Item
        fields=['title', 'description', 'due_date']
