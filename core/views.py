from django.shortcuts import render, redirect
from django.views import View
from core.models import Details, User, Categories, Locations
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


# @method_decorator(cache_page(60 * 60 * 24), name='dispatch')
class BusinessSearchView(View):
    def get(self, request, *args, **kwargs):
        location = []
        loc_obj = Locations.objects.all()
        for loc in loc_obj:
            detail = {
                'state':loc.state,
                'cities':loc.cities
            }
            location.append(detail)
        categories = []
        categories_obj = Categories.objects.all()
        for obj in categories_obj:
            categories.append(obj.categories_name)
        
        detail_obj = Details.objects.all()
        keyword = []
        postal = []
        for obj in detail_obj:
            keyword.append(obj.keyword)
            postal.append(obj.postal_code)
        allkey = list(set(keyword))
        allcode = list(set(postal))
        context = {
            'detail_service':categories+allkey,
            'detail_postalcode':list(filter(lambda x: x is not None, allcode)),
            'city_state': location
        }
        return render(request, 'index.html', context=context)


@method_decorator(csrf_exempt, name='dispatch')
# @method_decorator(cache_page(60 * 60 * 24), name='dispatch')
class BusinesslistView(View):
    def post(self, request, *args, **kwargs):
        print("*****",request.POST.get('keyword'),'*****',request.POST.get('location'))
        if request.POST.get('keyword') != '':
            if request.POST.get('location') != '':
                try:
                    loc_obj = request.POST.get('location').split(',')
                    if Details.objects.filter(categories__icontains=request.POST.get('keyword'), city__iexact=loc_obj[0], state__iexact=loc_obj[-1].split(' ')[-1]).exists():
                        details_obj = Details.objects.filter(categories__icontains=request.POST.get('keyword'), city__iexact=loc_obj[0], state__iexact=loc_obj[-1].split(' ')[-1])
                        context = {
                            'keyword':request.POST.get('keyword'),
                            'location':request.POST.get('location'),
                            'details_obj':details_obj
                        }
                        return render(request, 'jobs-list-layout-1.html',context=context)
                    else:
                        pass
                except:
                    pass

                try:
                    postalcode = int(request.POST.get('location'))
                    if Details.objects.filter(categories__icontains=request.POST.get('keyword'), postal_code = postalcode).exists():
                        details_obj = Details.objects.filter(categories__icontains=request.POST.get('keyword'), postal_code = postalcode)
                        context = {
                            'keyword':request.POST.get('keyword'),
                            'location':request.POST.get('location'),
                            'details_obj':details_obj
                        }
                        return render(request, 'jobs-list-layout-1.html',context=context)
                    else:
                        pass
                except:
                    pass

                try:
                    postalcode = int(request.POST.get('location'))
                    if Details.objects.filter(keyword__iexact=request.POST.get('keyword'), postal_code = postalcode).exists():
                        details_obj = Details.objects.filter(keyword__iexact=request.POST.get('keyword'), postal_code = postalcode)
                        context = {
                            'keyword':request.POST.get('keyword'),
                            'location':request.POST.get('location'),
                            'details_obj':details_obj
                        }
                        return render(request, 'jobs-list-layout-1.html',context=context)
                    else:
                        pass
                except:
                    pass
                
                try:
                    loc_obj = request.POST.get('location').split(',')
                    if Details.objects.filter(keyword__iexact=request.POST.get('keyword'), city__iexact=loc_obj[0], state__iexact=loc_obj[-1].split(' ')[-1]).exists():
                        details_obj = Details.objects.filter(keyword__iexact=request.POST.get('keyword'), city__iexact=loc_obj[0], state__iexact=loc_obj[-1].split(' ')[-1])
                        context = {
                            'keyword':request.POST.get('keyword'),
                            'location':request.POST.get('location'),
                            'details_obj':details_obj
                        }
                        return render(request, 'jobs-list-layout-1.html',context=context)
                    else:
                        categories = []
                        categories_obj = Categories.objects.all()
                        for obj in categories_obj:
                            categories.append(obj.categories_name)
                        
                        detail_obj = Details.objects.all()
                        keyword = []
                        postal = []
                        for obj in detail_obj:
                            keyword.append(obj.keyword)
                            postal.append(obj.postal_code)
                        allkey = list(set(keyword))
                        allcode = list(set(postal))
                        context = {
                            'detail_service':categories+allkey,
                            'detail_postalcode':list(filter(lambda x: x is not None, allcode))
                        }
                        return render(request,'404.html', context=context)
                except:
                    pass
            else:
                try:
                    if Details.objects.filter(name__iexact=request.POST.get('keyword')).exists():
                        details_obj = Details.objects.get(name__iexact=request.POST.get('keyword'))
                        context = {
                                    'details_obj':details_obj
                                }
                        return render(request, 'single-job-page.html',context=context)
                    else:
                        categories = []
                        categories_obj = Categories.objects.all()
                        for obj in categories_obj:
                            categories.append(obj.categories_name)
                        
                        detail_obj = Details.objects.all()
                        keyword = []
                        postal = []
                        for obj in detail_obj:
                            keyword.append(obj.keyword)
                            postal.append(obj.postal_code)
                        allkey = list(set(keyword))
                        allcode = list(set(postal))
                        context = {
                            'detail_service':categories+allkey,
                            'detail_postalcode':list(filter(lambda x: x is not None, allcode))
                        }
                        return render(request,'404.html', context=context)
                except:
                    pass          
        else:
            return redirect('Business-Search')


# @method_decorator(cache_page(60 * 60 * 24), name='dispatch')
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


class LocationSearchView(View):
    def get(self, request, *args, **kwargs):
        location = []
        loc_obj = Locations.objects.all()
        for loc in loc_obj:
            detail = {
                'state':loc.state,
                'cities':loc.cities
            }
            location.append(detail)
        categories = []
        categories_obj = Categories.objects.all()
        for obj in categories_obj:
            categories.append(obj.categories_name)
        
        detail_obj = Details.objects.all()
        keyword = []
        postal = []
        for obj in detail_obj:
            keyword.append(obj.keyword)
            postal.append(obj.postal_code)
        allkey = list(set(keyword))
        allcode = list(set(postal))
        cat = []
        loc_obj = Locations.objects.get(state=request.GET.get('state'))
        category_obj = Details.objects.filter(city__iexact=request.GET.get('city'))

        for data in category_obj:
            for obj in data.categories.split(','):
                cat.append(obj)

        context = {
            'city':request.GET.get('city'),
            'state':loc_obj.state_shortform,
            'categories':[item.title() for item in list(set(cat))],
            'detail_service':categories+allkey,
            'detail_postalcode':list(filter(lambda x: x is not None, allcode)),
            'city_state': location,
            'location':f"{request.GET.get('city')}, {request.GET.get('state')}"
        }
        return render(request, 'locationsearch.html',context=context)
        

class CategoriesBusinessView(View):
    def get(self, request, *args, **kwargs):
        if request.GET.get('keyword') != '':
            if request.GET.get('location') != '':
                print("=======",request.GET.get('keyword'),"=======",request.GET.get('location'))
                try:
                    print("-1")
                    loc_obj = request.GET.get('location').split(',')
                    print("-----",loc_obj)

                    if Details.objects.filter(categories__icontains=request.GET.get('keyword'), city__iexact=loc_obj[0], state__iexact=loc_obj[-1].split(' ')[-1]).exists():
                        print("1")
                        details_obj = Details.objects.filter(categories__icontains=request.GET.get('keyword'), city__iexact=loc_obj[0], state__iexact=loc_obj[-1].split(' ')[-1])
                        context = {
                            'keyword':request.GET.get('keyword'),
                            'location':request.GET.get('location'),
                            'details_obj':details_obj
                        }
                        return render(request, 'jobs-list-layout-1.html',context=context)
                    else:
                        pass
                except:
                    pass

                try:
                    print("-2")
                    postalcode = int(request.GET.get('location'))
                    if Details.objects.filter(categories__icontains=request.GET.get('keyword'), postal_code = postalcode).exists():
                        print("2")
                        details_obj = Details.objects.filter(categories__icontains=request.GET.get('keyword'), postal_code = postalcode)
                        context = {
                            'keyword':request.GET.get('keyword'),
                            'location':request.GET.get('location'),
                            'details_obj':details_obj
                        }
                        return render(request, 'jobs-list-layout-1.html',context=context)
                    else:
                        pass
                except:
                    pass

                try:
                    print("-3")
                    postalcode = int(request.GET.get('location'))
                    if Details.objects.filter(keyword__iexact=request.GET.get('keyword'), postal_code = postalcode).exists():
                        print("3")
                        details_obj = Details.objects.filter(keyword__iexact=request.GET.get('keyword'), postal_code = postalcode)
                        context = {
                            'keyword':request.GET.get('keyword'),
                            'location':request.GET.get('location'),
                            'details_obj':details_obj
                        }
                        return render(request, 'jobs-list-layout-1.html',context=context)
                    else:
                        pass
                except:
                    pass
                
                try:
                    print("-4")
                    loc_obj = request.GET.get('location').split(',')
                    if Details.objects.filter(keyword__iexact=request.GET.get('keyword'), city__iexact=loc_obj[0], state__iexact=loc_obj[-1].split(' ')[-1]).exists():
                        print("4")
                        details_obj = Details.objects.filter(keyword__iexact=request.GET.get('keyword'), city__iexact=loc_obj[0], state__iexact=loc_obj[-1].split(' ')[-1])
                        context = {
                            'keyword':request.GET.get('keyword'),
                            'location':request.GET.get('location'),
                            'details_obj':details_obj
                        }
                        return render(request, 'jobs-list-layout-1.html',context=context)
                    else:
                        categories = []
                        categories_obj = Categories.objects.all()
                        for obj in categories_obj:
                            categories.append(obj.categories_name)
                        
                        detail_obj = Details.objects.all()
                        keyword = []
                        postal = []
                        for obj in detail_obj:
                            keyword.append(obj.keyword)
                            postal.append(obj.postal_code)
                        allkey = list(set(keyword))
                        allcode = list(set(postal))
                        context = {
                            'detail_service':categories+allkey,
                            'detail_postalcode':list(filter(lambda x: x is not None, allcode))
                        }
                        return render(request,'404.html', context=context)
                except:
                    pass
            else:
                return redirect('Business-Search')
        else:
            return redirect('Business-Search')



class DiscoverCategoriesView(View):
    def get(self, request, *args, **kwargs):
        print("*********", request.GET.get('keyword'))
        location = []
        loc_obj = Locations.objects.all()
        for loc in loc_obj:
            detail = {
                'state':loc.state,
                'cities':loc.cities
            }
            location.append(detail)
        categories = []
        categories_obj = Categories.objects.all()
        for obj in categories_obj:
            categories.append(obj.categories_name)
        
        detail_obj = Details.objects.all()
        keyword = []
        postal = []
        for obj in detail_obj:
            keyword.append(obj.keyword)
            postal.append(obj.postal_code)
        allkey = list(set(keyword))
        allcode = list(set(postal))
        context = {
            'keyword':request.GET.get('keyword'),
            'detail_service':categories+allkey,
            'detail_postalcode':list(filter(lambda x: x is not None, allcode)),
            'city_state': location
        }

        return render(request, 'discover_categories.html', context=context)


def log_out(request):
        logout(request)
        return redirect('Login')