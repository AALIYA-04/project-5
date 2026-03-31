from django.shortcuts import render

# Create your views here.
def todo(request):
     return render(request, 'todo.html')

def index(request):
    return render(request, 'index.html')

