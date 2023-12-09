from django.shortcuts import redirect, render
from django.http import HttpResponse
from .serializers import DocumentSerializer
from .models import Document,UserDetails
from rest_framework import permissions, viewsets
from .forms import SignForm,LoginForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout


def signup(request):
    
    if request.method == 'POST':
        form = SignForm(request.POST,request.FILES)
        if form.is_valid():
            form.full_clean()
            form.save()
        else:
            print('error')
    
    form = SignForm()
    context = {'form' : form}
    return render(request, 'filesharing/signup.html', context)

def login(request):
    message = ''
    form = LoginForm()
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        resp = UserDetails.objects.filter(email=email,password=password).exists()
        user = authenticate(request, username = email, password = password)
        if resp == True:
            return redirect('index')
        else:
            message = 'Wrong username or password'
    context = {'form' : form,
               'message':message}
    return render(request, 'filesharing/login.html', context)


def index(request):        
    data = Document.objects.all()
    context = {'data' : data}
    return render(request, 'filesharing/index.html', context)

class DocumentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows document to be viewed or edited.
    """
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    permission_classes = [permissions.IsAuthenticated]
