from django.contrib import admin
from .models import Details, User, Locations, Categories
# Register your models here.


@admin.register(Details)
class DetailsAdmin(admin.ModelAdmin):
    list_display = ('id','keyword','categories','name', 'profile_url','address',
                    'city','state','postal_code','phone','email', 'website','rating',
                    'review','years_in_business', 'bbb_rating','other_links')
    
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
     list_display = ('id','uuid','f_name','l_name','email', 'password','zipcode')


@admin.register(Locations)
class LocationsAdmin(admin.ModelAdmin):
     list_display = ('id','state_shortform','state','cities')


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
     list_display = ('id','categories_name')