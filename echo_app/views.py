from django.shortcuts import render

# Create your views here.
def websocket_front_end(request):
    return render(request, 'index.html')