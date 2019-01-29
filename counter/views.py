from django.http import HttpResponse
from django.shortcuts import render
from counter.models import cont


def homepage(request):
    return render(request,'home.html')

def search(request):
    data=request.GET['t1']
    data2=cont.objects.filter(name__icontains=data)
    print(data2)
    return render(request,'search_pg.html', {'dic': data2})



