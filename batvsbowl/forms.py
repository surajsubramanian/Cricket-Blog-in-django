from django import forms
from .models import PlayerIpl


class BatBowlForm(forms.Form):
    batsmen = forms.ModelChoiceField(queryset=PlayerIpl.objects.all())
    bowlers = forms.ModelChoiceField(queryset=PlayerIpl.objects.all())
