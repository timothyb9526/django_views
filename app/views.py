from django.shortcuts import render


def add(request):
    num1 = request.GET.get('num1')
    num2 = request.GET.get('num2')

    if num1 is not None and num2 is not None:
        num1 = float(num1)
        num2 = float(num2)
        answer = num1 + num2
        return render(request, 'app/add.html', {'answer': answer})
    else:
        return render(request, 'app/add.html')
