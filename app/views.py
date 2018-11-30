from django.shortcuts import render
from django.views import View
from . import forms


class Add(View):
    def get(self, request):
        # try:
        #     num1 = float(request.GET.get('num1', ''))
        #     num2 = float(request.GET.get('num2', ''))
        # except ValueError:
        #     return render(request, 'app/add.html')
        # else:
        #     answer = num1 + num2
        #     return render(request, 'app/add.html', {'answer': answer})

        form = forms.AddForm(data=request.GET)
        if form.is_valid():
            num1 = form.cleaned_data['num1']
            num2 = form.cleaned_data['num2']
            answer = num1 + num2
            return render(request, 'app/add.html', {'answer': answer})
        else:
            return render(request, 'app/add.html')


class Double(View):
    def get(self, request):
        # try:
        #     num = float(request.GET.get('number', ''))
        # except ValueError:
        #     return render(request, 'app/double.html')

        # else:
        #     answer = num * 2
        #     return render(request, 'app/double.html', {'answer': answer})

        form = forms.DoubleForm(data=request.GET)
        if form.is_valid():
            num = form.cleaned_data['number']
            answer = num * 2
            return render(request, 'app/double.html', {'answer': answer})
        else:
            return render(request, 'app/double.html')


class MultThree(View):
    def get(self, request):
        # try:
        #     x = float(request.GET.get('x', ''))
        #     y = float(request.GET.get('y', ''))
        #     z = float(request.GET.get('z', ''))
        # except ValueError:
        #     return render(request, 'app/multiply.html')
        # else:
        #     answer = x * y * z
        #     return render(request, 'app/multiply.html', {'answer': answer})

        form = forms.MultThreeForm(data=request.GET)
        if form.is_valid():
            x = form.cleaned_data['x']
            y = form.cleaned_data['y']
            z = form.cleaned_data['z']
            answer = x * y * z
            return render(request, 'app/multiply.html', {'answer': answer})
        else:
            return render(request, 'app/multiply.html')


class Earnings(View):
    def get(self, request):
        # try:
        #     a = float(request.GET.get('a', ''))
        #     b = float(request.GET.get('b', ''))
        #     c = float(request.GET.get('c', ''))
        # except ValueError:
        #     return render(request, 'app/earnings.html')
        # else:
        #     answer = a * 15 + b * 12 + c * 9
        #     return render(request, 'app/earnings.html', {'answer': answer})

        form = forms.EarningsForm(data=request.GET)
        if form.is_valid():
            a = form.cleaned_data['a']
            b = form.cleaned_data['b']
            c = form.cleaned_data['c']
            answer = a * 15 + b * 12 + c * 9
            return render(request, 'app/earnings.html', {'answer': answer})
        else:
            return render(request, 'app/earnings.html')


class TrueOrFalse(View):
    def get(self, request):
        # try:
        #     num1 = request.GET.get('num1', '')
        #     num2 = request.GET.get('num2', '')
        # except ValueError:
        #     return render(request, 'app/t_or_f.html')
        # else:
        #     if num1 == 'true' and num2 == 'true':
        #         answer = True
        #         return render(request, 'app/t_or_f.html', {'answer': answer})
        #     elif num1 == 'false' and num2 == 'false':
        #         answer = False
        #         return render(request, 'app/t_or_f.html', {'answer': answer})
        #     else:
        #         return render(request, 'app/t_or_f.html')

        form = forms.TrueOrFalseForm(data=request.GET)
        if form.is_valid():
            num1 = form.cleaned_data['num1']
            num2 = form.cleaned_data['num2']
            return render(request, 'app/t_or_f.html',
                          {'answer': num1 and num2})


class HowPopulated(View):
    def get(self, request):
        # try:
        #     area = float(request.GET.get('area', ''))
        #     population = float(request.GET.get('population', ''))
        # except ValueError:
        #     return render(request, 'app/population.html')
        # else:
        #     answer = population / area
        #     if answer > 1000:

        #         return render(request, 'app/population.html',
        #                       {'answer': 'Densely Populated'})
        #     else:
        #         return render(request, 'app/population.html',
        #                       {'answer': 'Sparsely Populated'})

        form = forms.PopulationForm(data=request.GET)
        if form.is_valid():
            population = form.cleaned_data['population']
            area = form.cleaned_data['area']
            answer = population / area
            if answer > 1000:

                return render(request, 'app/population.html',
                              {'answer': 'Densely Populated'})
            else:
                return render(request, 'app/population.html',
                              {'answer': 'Sparsely Populated'})
        else:
            return render(request, 'app/population.html')


class GoldStar(View):
    def get(self, request):
        # try:
        #     num = float(request.GET.get('score', ''))
        # except ValueError:
        #     return render(request, 'app/gold_star.html')

        # else:
        #     if num < 1000:
        #         answer = "*"
        #         return render(request, 'app/gold_star.html',
        #                       {'answer': answer})
        #     elif num < 5000 and num >= 1000:
        #         answer = "**"
        #         return render(request, 'app/gold_star.html',
        #                       {'answer': answer})
        #     elif num < 8000 and num >= 5000:
        #         answer = "***"
        #         return render(request, 'app/gold_star.html',
        #                       {'answer': answer})
        #     elif num < 10000 and num >= 8000:
        #         answer = "****"
        #         return render(request, 'app/gold_star.html',
        #                       {'answer': answer})
        #     elif num >= 10000:
        #         answer = "*****"
        #         return render(request, 'app/gold_star.html',
        #                       {'answer': answer})

        form = forms.GoldStarForm(data=request.GET)
        if form.is_valid():
            score = form.cleaned_data['score']
            if score < 1000:
                answer = "*"
                return render(request, 'app/gold_star.html',
                              {'answer': answer})
            elif score < 5000 and score >= 1000:
                answer = "**"
                return render(request, 'app/gold_star.html',
                              {'answer': answer})
            elif score < 8000 and score >= 5000:
                answer = "***"
                return render(request, 'app/gold_star.html',
                              {'answer': answer})
            elif score < 10000 and score >= 8000:
                answer = "****"
                return render(request, 'app/gold_star.html',
                              {'answer': answer})
            elif score >= 10000:
                answer = "*****"
                return render(request, 'app/gold_star.html',
                              {'answer': answer})
        else:
            return render(request, 'app/gold_star.html')


class ScoringAction(View):
    def get(self, request):
        # try:
        #     action = request.GET.get('action', '')
        # except ValueError:
        #     return render(request, 'app/scoring_action.html')

        # else:
        #     if action == 'extra kick':
        #         answer = 1
        #         return render(request, 'app/scoring_action.html',
        #                       {'answer': answer})
        #     elif action == 'extra conversion':
        #         answer = 2
        #         return render(request, 'app/scoring_action.html',
        #                       {'answer': answer})
        #     elif action == 'safety':
        #         answer = 2
        #         return render(request, 'app/scoring_action.html',
        #                       {'answer': answer})
        #     elif action == 'fg':
        #         answer = 3
        #         return render(request, 'app/scoring_action.html',
        #                       {'answer': answer})
        #     elif action == 'td':
        #         answer = 6
        #         return render(request, 'app/scoring_action.html',
        #                       {'answer': answer})
        #     else:
        #         return render(request, 'app/scoring_action.html')

        form = forms.ScoringActionForm(data=request.GET)
        if form.is_valid():
            action = form.cleaned_data['action']
            if action == 'extra kick':
                answer = 1
                return render(request, 'app/scoring_action.html',
                              {'answer': answer})
            elif action == 'extra conversion':
                answer = 2
                return render(request, 'app/scoring_action.html',
                              {'answer': answer})
            elif action == 'safety':
                answer = 2
                return render(request, 'app/scoring_action.html',
                              {'answer': answer})
            elif action == 'fg':
                answer = 3
                return render(request, 'app/scoring_action.html',
                              {'answer': answer})
            elif action == 'td':
                answer = 6
                return render(request, 'app/scoring_action.html',
                              {'answer': answer})
            else:
                return render(request, 'app/scoring_action.html')
        else:
            return render(request, 'app/scoring_action.html')


class WalkOrDrive(View):
    def get(self, request):
        form = forms.WalkOrDriveForm(data=request.GET)
        if form.is_valid():
            miles = form.cleaned_data['miles']
            weather = form.cleaned_data['weather']
            if miles < .25 and weather:
                answer = 'walk'
                return render(request, 'app/walk_or_drive.html',
                              {'answer': answer})
            else:
                answer = 'drive'
                return render(request, 'app/walk_or_drive.html',
                              {'answer': answer})
        else:
            return render(request, 'app/walk_or_drive.html')
