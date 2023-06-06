from django.shortcuts import render, redirect
from django.views import View
from core.models import Details, User
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.cache import cache
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.views.decorators.cache import cache_page
import uuid

# Create your views here.

class SignupView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'signup.html')
     
    def post(self, request, *args, **kwargs):
        if request.POST.get('f_name') !='':
            if request.POST.get('l_name') !='':
                if request.POST.get('email') !='':
                    if request.POST.get('password') !='':
                        if request.POST.get('confirm') !='':
                            if request.POST.get('password')==request.POST.get('confirm'):
                                if not User.objects.filter(email=request.POST.get('email')).exists():
                                    uu_id = str(uuid.uuid4())
                                    user_obj = User(uuid=uu_id, f_name=request.POST.get('f_name'), l_name=request.POST.get('l_name'), email=request.POST.get('email'), password=request.POST.get('password'), zipcode=request.POST.get('zipcode'))
                                    user_obj.set_password(request.POST.get('password'))
                                    user_obj.save()
                                    return redirect('Login')
                                else:
                                    messages.error(request, 'ERROR: Email already present.')
                            else:
                                messages.error(request, 'ERROR: Password and Confirm Password must be same.')
                        else:
                            messages.error(request, 'ERROR: Confirm Password not found.')
                    else:
                        messages.error(request, 'ERROR: Password not found.')
                else:
                    messages.error(request, 'ERROR: Email not found.')
            else:
                messages.error(request, 'ERROR: Last Name not found.')
        else:
            messages.error(request, 'ERROR: First Name not found.')
        return redirect('Signup')


class LoginView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'login.html')
     
    def post(self, request, *args, **kwargs):
        user = authenticate(email=request.POST.get('email'), password=request.POST.get('pass'))
        if user is not None:
            login(request, user)
            return redirect('Business-Search')
        else:
            messages.error(request, "Error: Invalide Login Credential.")
            return redirect('Login')


@method_decorator(cache_page(60 * 60 * 24), name='dispatch')
class BusinessSearchView(View):
    def get(self, request, *args, **kwargs):
       return render(request, 'index.html')
    

@method_decorator(csrf_exempt, name='dispatch')
# @method_decorator(cache_page(60 * 60 * 24), name='dispatch')
class BusinesslistView(View):
    def post(self, request, *args, **kwargs):
        if request.POST.get('keyword') != '':
            if request.POST.get('location') != '':
                try:
                    postalcode = int(request.POST.get('location'))
                    if Details.objects.filter(keyword=request.POST.get('keyword').lower(), postal_code = postalcode).exists():
                        details_obj = Details.objects.filter(keyword=request.POST.get('keyword').lower(), postal_code = postalcode)
                        context = {
                            'keyword':request.POST.get('keyword'),
                            'location':request.POST.get('location'),
                            'details_obj':details_obj
                        }
                        return render(request, 'jobs-list-layout-1.html',context=context)
                    else:
                        return render(request,'404.html')
                except:
                    pass
                
                try:
                    loc_obj = request.POST.get('location').split(',')
                    if Details.objects.filter(keyword=request.POST.get('keyword').lower(), city=loc_obj[0].lower(), state=loc_obj[-1].split(' ')[-1].lower()).exists():
                        details_obj = Details.objects.filter(keyword=request.POST.get('keyword').lower(), city=loc_obj[0].lower(), state=loc_obj[-1].split(' ')[-1].lower())
                        context = {
                            'keyword':request.POST.get('keyword'),
                            'location':request.POST.get('location'),
                            'details_obj':details_obj
                        }
                        return render(request, 'jobs-list-layout-1.html',context=context)
                    else:
                        return render(request,'404.html')
                except:
                    pass
            else:
                return redirect('Business-Search')
        else:
            return redirect('Business-Search')


@method_decorator(cache_page(60 * 60 * 24), name='dispatch')
class BusinessDetailView(View):
    def get(self, request, pk, *args, **kwargs):
        if Details.objects.filter(uuid=pk).exists():
            detail_obj = Details.objects.get(uuid=pk)
            context = {
                        'details_obj':detail_obj
                    }
            return render(request, 'single-job-page.html',context=context)


class BusinessListingView(LoginRequiredMixin,UserPassesTestMixin,View):
    def test_func(self):
        return self.request.user
    
    def get(self, request, *args, **kwargs):
        return render(request,'business_listing.html')
    
    def post(self, request, *args, **kwargs):
        if request.POST.get('b_year') == '':
            years_in_business = None
        else:
            years_in_business = request.POST.get('b_year')

        detail_obj = Details(user=request.user, keyword=request.POST.get('b_type'), name=request.POST.get('b_name'), 
                             address=request.POST.get('b_address'), city=request.POST.get('b_city'),
                             state=request.POST.get('b_state'),postal_code=request.POST.get('b_postal'),
                             phone=request.POST.get('b_phone'),email=request.POST.get('b_email'),website=request.POST.get('b_web'),
                             years_in_business=years_in_business,other_links=request.POST.getlist('b_other'))
        detail_obj.save()
        return redirect("Business-Detail",pk=detail_obj.uuid)


def log_out(request):
        logout(request)
        return redirect('Login')
