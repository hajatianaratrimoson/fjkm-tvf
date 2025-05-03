from django.shortcuts import render

def custom_500(request):
    return render(request, '500.html', status=500)
