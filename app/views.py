from django.shortcuts import render
from django.views import View


class Add(View):
    def get(self, request):
        try:
            num1 = float(request.GET.get('num1'))
            num2 = float(request.GET.get('num2'))
        except ValueError:
            return render(request, 'app/add.html')
        else:
            answer = num1 + num2
            return render(request, 'app/add.html', {'answer': answer})


class Double(View):
    def get(self, request):
        number = request.GET.get('number')
        if number is not None:
            try:
                num = float(number)
            except ValueError:
                return render(request, 'app/double.html')
            answer = num * 2
            return render(request, 'app/double.html', {'answer': answer})
        else:
            return render(request, 'app/double.html')


class MultThree(View):
    def get(self, request):
        x = request.GET.get('x')
        y = request.GET.get('y')
        z = request.GET.get('z')
        if x is not None and y is not None and z is None:
            x = float(x)
            y = float(y)
            z = float(z)
            answer = x * y * z
            return render(request, 'app/multiply.html', {'answer': answer})
        else:
            return render(request, 'app/multiply.html')
