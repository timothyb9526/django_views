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
        except (ValueError, TypeError):
            return render(request, 'app/multiply.html')
        else:
            answer = x * y * z
            return render(request, 'app/multiply.html', {'answer': answer})
