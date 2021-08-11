from django.shortcuts import render


# Create your views here.
def practice(request):
    context = {}
    return render(request, 'practice.html', context)