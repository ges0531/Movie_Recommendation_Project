from django.shortcuts import render

def title(request):
    return render(request, 'title/title.html')