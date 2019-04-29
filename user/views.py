from django.conf import settings
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from .forms import ExtendedUserCreationForm,UserProfileForm
from django.core.mail import send_mail
from .tokens import account_activation_token
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.contrib.auth.models import User
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text
from django.contrib.auth import login, authenticate
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, 'home.html')


def signup(request):
    if request.method== 'POST':
        form=ExtendedUserCreationForm(request.POST)
        profile_form=UserProfileForm(request.POST,request.FILES)
        print (form.is_valid())
        if form.is_valid() and profile_form.is_valid():
            user=form.save(commit=False)
            user.is_active = False
            user.save()
            profile=profile_form.save(commit=False)
            profile.user=user
            profile.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate your crowd_funding account.'
            message = render_to_string('acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                        mail_subject, message, to=[to_email]
            )
            email.send()
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password1')
            user=authenticate(username=username,password=password)
            return render(request,'check_mail.html')
    else:
        form=ExtendedUserCreationForm()
        profile_form=UserProfileForm()    
    return render(request,'registration/signup.html',{
        'form':form,
        'profile_form':profile_form
    })

@login_required
def secret_page(request):
    return render(request, 'secret_page.html')



def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return redirect('home')
        #return HttpResponse("Thank you for your email confirmation. Now you can go to your homepage")
    else:
        return HttpResponse('Activation link is invalid!')    

