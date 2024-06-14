from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse
from .models import User
from .serializers import UserSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .forms import UploadForm, LoginForm
from django.contrib.auth import login, authenticate
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_str, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail, EmailMultiAlternatives
import random
import uuid
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from .utils import generate_token
from django.urls import reverse
import  threading
from django.utils.html import strip_tags

class EmailThread(threading.Thread):
    def __init__(self, email):
        self.email = email
        threading.Thread.__init__(self)

    def run(self):
        self.email.send()


def send_activate_email(user, request):
    current_site= get_current_site(request)
    email_subject = 'Activate your account'
    email_body = render_to_string('activateEmail.html', {
        'user': user,
        'domain': current_site,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': generate_token.make_token(user)
    })

    plain_message = strip_tags(email_body)

    email = EmailMultiAlternatives(subject=email_subject, body=plain_message,
                from_email=settings.EMAIL_HOST_USER,
                 to=[user.email]
                 )
    
    email.attach_alternative(email_body, "text/html")

    EmailThread(email).start()

def index(request):
    return render(request, 'index.html')

# def about(request):
#     return render(request, 'tickets.html')

# @api_view(['GET', 'POST'])
def register(request):

    if request.POST:
        form = UploadForm(request.POST)

        username = request.POST.get('username')
        email = request.POST.get('email')
        user = User.objects.all()

        if user.filter(username=username).exists():
            return render(request, 'register.html', {'form':form})
        
        if user.filter(email=email).exists():
            return render(request, 'register.html', {'form':form})

        if form.is_valid():
            if form.is_valid():  
 
                post = form.save(commit = False)
                post.is_active = False

                myUUID = uuid.uuid1(random.randint(0, 281474976710655))
                post.activateUUID = myUUID


                post.save() 

                send_activate_email(post, request)

                messages.add_message(request, messages.SUCCESS, 
                                     "Account confirmation email sent, please verify.", extra_tags="email")
                
                return redirect('login')

                # return render(request, 'login.html', {'message': "Please Check Email to Confirm Account"})
                # return HttpResponse('Please confirm your email address to complete the registration')
                
        else:
            return render(request, "register.html", {'form':form})  
        
    else:

        form = UploadForm(None)   
        return render(request, 'register.html', {'form':form})
    #         form.save()
    #     return redirect(register)
    # return render(request, 'register.html', {'form': UploadForm})
    


    return render(request, 'register.html')

def activate_user(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))

        user = User.objects.get(pk=uid)
    except Exception as e:
        user = None

    if user and generate_token.check_token(user, token):
        user.confirmed = 1
        user.save()
        messages.add_message(request, messages.SUCCESS, 'Email Verified!', extra_tags="email")
        return redirect(reverse('login'))
    
    return render(request, 'activate-failed.html', {"user": user})


def check_username(request):

    username = request.POST.get('username')
    user = User.objects.all()
    print(user.filter(username=username).exists())

    if user.filter(username=username).exists():
        return HttpResponse('<p style="color: red">username already exists</p>')
    elif username == "":
        return HttpResponse('<p></p>')
    else:
        return HttpResponse('<p style="color: green">username is available</p>')
    
def check_email(request):

    email = request.POST.get('email')
    user = User.objects.all()
    print(user.filter(email=email).exists())

    if user.filter(email=email).exists():
        return HttpResponse('<p style="color: red">Email already exists</p>')
    elif email == "":
        return HttpResponse('<p></p>')
    else:
        return HttpResponse('<p style="color: green">Email is available</p>')
    

def login(request):

    if request.POST:
        form = LoginForm(request.POST)

        # context = {'has_error': False, 'date': request.POST}
        password = request.POST.get('password')
        email = request.POST.get('email')
        user = User.objects.all()

        myUser = user.filter(email=email).values()

        # print(myUser[0])

        if user.filter(email=email, password=password, confirmed = 1).exists():
            return render(request, 'home.html', {'form':myUser[0]})

        else:         
            form = LoginForm(None)   

            messages.add_message(request, messages.ERROR, 
                                            "Incorrect Credentials!", extra_tags="login")
            
            return render(request, 'login.html', {'form':form})

    else:

        form = LoginForm(None)   
        return render(request, 'login.html', {'form':form})
    

def home(request):

    uid = request.GET.get('uid')
    users = User.objects.all()

    myUser = users.filter(id=uid).values()

    return render(request, 'home.html', {'form':myUser[0]})

def tickets(request):
    
    print(request.GET.get('uid'))
    uid = request.GET.get('uid')
    users = User.objects.all()

    myUser = users.filter(id=uid).values()

    return render(request, 'tickets.html', {'form':myUser[0]})

def explore(request):
    return render(request, 'explore.html')