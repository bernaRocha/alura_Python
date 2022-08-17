from django.shortcuts import render
#from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request,'index.html')
    #return HttpResponse('<h1>Receitas</h1> <h2>Bem vindo! </h2>')