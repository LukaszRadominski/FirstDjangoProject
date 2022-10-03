from django.shortcuts import render

# Create your views here.

def carslist(request):
    return render(request, 'carslist.html')  # 6.6. we define the htmls to render for each route.