from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import User
from .serializers import UserSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .forms import UploadForm

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'tickets.html')

# @api_view(['GET', 'POST'])
def register(request):

    if request.POST:
        form = UploadForm(request.POST)
        print(request)
        if form.is_valid():
            form.save()
        return redirect(register)
    return render(request, 'register.html', {'form': UploadForm})

    # if request.method == 'GET':
            
    #     userInfo = User.objects.all()
    #     serializer = UserSerializer(userInfo, many=True)
    #     return JsonResponse({'userInfo': serializer.data})
    
    # if request.method == 'POST':
    #     serializer = UserSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    


    return render(request, 'register.html')

def login(request):
    return render(request, 'login.html')