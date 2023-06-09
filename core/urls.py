from django.urls import path
from core.views import (BusinessSearchView, BusinesslistView, BusinessDetailView, BusinessListingView 
                        ,SignupView, LoginView, LocationSearchView, CategoriesBusinessView, DiscoverCategoriesView, log_out)

urlpatterns = [
    path('signup/',SignupView.as_view(), name='Signup'),
    path('login/',LoginView.as_view(), name='Login'),
    path('',BusinessSearchView.as_view(), name='Business-Search'),
    path('business-list/',BusinesslistView.as_view(), name='Business-list'),
    path('business-detail/<uuid:pk>/',BusinessDetailView.as_view(), name='Business-Detail'),
    path('business-listing/',BusinessListingView.as_view(), name='Business-Listing'),
    path('location/',LocationSearchView.as_view(), name='Location-Search'),
    path('categories/',CategoriesBusinessView.as_view(), name='Categories-Business'),
    path('discover-categories/',DiscoverCategoriesView.as_view(), name='Discover-Categories'),
    path('logout/', log_out, name='logout'),
]