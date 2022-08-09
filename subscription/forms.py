from django.forms import ModelForm
from django import forms
from .models import AvailableSubscription




class SubcribeToSomethingForm(ModelForm):
    class Meta:
        model = AvailableSubscription
        # fields = "__all__"
        exclude = ["url_of_feed"]
        widgets = {'feed_name':forms.CheckboxInput}

# article = AvailableSubscription.objects.filter(pk=1)
# form = SubcribeToSomethingForm(instance=article)

