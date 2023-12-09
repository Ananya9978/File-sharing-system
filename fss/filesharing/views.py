from django.shortcuts import redirect, render
from django.http import HttpResponse
from .serializers import DocumentSerializer
from .models import Document,UserDetails
from rest_framework import permissions, viewsets
from .forms import SignForm,LoginForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout



# Create your views here.

# def download_file(request, file_id):
#     uploaded_file = Document.objects.get(pk=file_id)
#     response = HttpResponse(uploaded_file.file, content_type='application/force-download')
#     response['Content-Disposition'] = f'attachment; filename="{uploaded_file.file.name}"'
#     return response

def signup(request):
    
    if request.method == 'POST':
        print('in post')
        form = SignForm(request.POST,request.FILES)
        if form.is_valid():
            print('is_valid')
            form.full_clean()
            form.save()
        else:
            print('error')
    
    print('not post')
    form = SignForm()
    context = {'form' : form}
    return render(request, 'filesharing/signup.html', context)

def login(request):
    message = ''
    form = LoginForm()
    print('in login')
    u = UserDetails.objects.all()
    for i in u:
        print(i.email,i.password)
    if request.method == 'POST':
        print('in post login')
        email = request.POST['email']
        password = request.POST['password']
        print(email,password)
        resp = UserDetails.objects.filter(email=email,password=password).exists()
        user = authenticate(request, username = email, password = password)
        if resp == True:

            # login(email)
            return redirect('index')
        else:
            message = 'Wrong username or password'
    context = {'form' : form,
               'message':message}
    return render(request, 'filesharing/login.html', context)


def index(request):
    print(request.user)
        
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
