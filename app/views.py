from django.shortcuts import render
from django.views import View


class Add(View):
    def get(self, request):
        try:
            num1 = float(request.GET.get('num1', ''))
            num2 = float(request.GET.get('num2', ''))
        except ValueError:
            return render(request, 'app/add.html')
        else:
            answer = num1 + num2
            return render(request, 'app/add.html', {'answer': answer})


class Double(View):
    def get(self, request):
        try:
            num = float(request.GET.get('number', ''))
        except ValueError:
            return render(request, 'app/double.html')

        else:
            answer = num * 2
            return render(request, 'app/double.html', {'answer': answer})


class MultThree(View):
    def get(self, request):
        try:
            x = float(request.GET.get('x', ''))
            y = float(request.GET.get('y', ''))
            z = float(request.GET.get('z', ''))
        except ValueError:
            return render(request, 'app/multiply.html')
        else:
            answer = x * y * z
            return render(request, 'app/multiply.html', {'answer': answer})


class Earnings(View):
    def get(self, request):
        try:
            a = float(request.GET.get('a', ''))
            b = float(request.GET.get('b', ''))
            c = float(request.GET.get('c', ''))
        except ValueError:
            return render(request, 'app/earnings.html')
        else:
            answer = a * 15 + b * 12 + c * 9
            return render(request, 'app/earnings.html', {'answer': answer})


class TrueOrFalse(View):
    def get(self, request):
        try:
            num1 = request.GET.get('num1', '')
            num2 = request.GET.get('num2', '')
        except ValueError:
            return render(request, 'app/t_or_f.html')
        else:
            if num1 == 'true' and num2 == 'true':
                answer = True
                return render(request, 'app/t_or_f.html', {'answer': answer})
            elif num1 == 'false' and num2 == 'false':
                answer = False
                return render(request, 'app/t_or_f.html', {'answer': answer})
            else:
                return render(request, 'app/t_or_f.html')


class HowPopulated(View):
    def get(self, request):
        try:
            area = float(request.GET.get('area', ''))
            population = float(request.GET.get('population', ''))
        except ValueError:
            return render(request, 'app/population.html')
        else:
            answer = population / area
            if answer > 1000:

                return render(request, 'app/population.html',
                              {'answer': 'Densely Populated'})
            else:
                return render(request, 'app/population.html',
                              {'answer': 'Sparsely Populated'})


class GoldStar(View):
    def get(self, request):
        try:
            num = float(request.GET.get('score', ''))
        except ValueError:
            return render(request, 'app/gold_star.html')

        else:
            if num < 1000:
                answer = "*"
                return render(request, 'app/gold_star.html',
                              {'answer': answer})
            elif num < 5000 and num >= 1000:
                answer = "**"
                return render(request, 'app/gold_star.html',
                              {'answer': answer})
            elif num < 8000 and num >= 5000:
                answer = "***"
                return render(request, 'app/gold_star.html',
                              {'answer': answer})
            elif num < 10000 and num >= 8000:
                answer = "****"
                return render(request, 'app/gold_star.html',
                              {'answer': answer})
            elif num >= 10000:
                answer = "*****"
                return render(request, 'app/gold_star.html',
                              {'answer': answer})
