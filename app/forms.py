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
    a = forms.FloatField(min_value=0)
    b = forms.FloatField(min_value=0)
    c = forms.FloatField(min_value=0)


class PopulationForm(forms.Form):
    population = forms.FloatField(min_value=0)
    area = forms.FloatField(min_value=1)


class GoldStarForm(forms.Form):
    score = forms.FloatField(min_value=0)


class ScoringActionForm(forms.Form):
    action = forms.CharField(min_length=1)


class TrueOrFalseForm(forms.Form):
    num1 = forms.BooleanField(required=False)
    num2 = forms.BooleanField(required=False)


class WalkOrDriveForm(forms.Form):
    miles = forms.FloatField(min_value=0)
    weather = forms.BooleanField(required=False)
