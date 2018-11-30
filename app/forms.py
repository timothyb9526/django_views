from django import forms


class AddForm(forms.Form):

    num1 = forms.FloatField()
    num2 = forms.FloatField()


class DoubleForm(forms.Form):
    number = forms.FloatField()


class MultThreeForm(forms.Form):
    x = forms.FloatField()
    y = forms.FloatField()
    z = forms.FloatField()


class EarningsForm(forms.Form):
    a = forms.FloatField()
    b = forms.FloatField()
    c = forms.FloatField()


class PopulationForm(forms.Form):
    population = forms.FloatField()
    area = forms.FloatField()


class GoldStarForm(forms.Form):
    score = forms.FloatField()


class ScoringActionForm(forms.Form):
    action = forms.CharField()


class TrueOrFalseForm(forms.Form):
    num1 = forms.BooleanField(required=False)
    num2 = forms.BooleanField(required=False)


class WalkOrDriveForm(forms.Form):
    miles = forms.FloatField()
    weather = forms.BooleanField(required=False)
