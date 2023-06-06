from django.urls import path
from core.views import BusinessSearchView, BusinesslistView, BusinessDetailView, BusinessListingView, SignupView, LoginView, log_out

urlpatterns = [
    path('signup/',SignupView.as_view(), name='Signup'),
    path('login/',LoginView.as_view(), name='Login'),
    path('',BusinessSearchView.as_view(), name='Business-Search'),
    path('business-list/<str:abc>/<str:location>',BusinesslistView.as_view(), name='Business-list'),
    path('business-list/',BusinesslistView.as_view(), name='Business-list'),
    path('business-detail/<uuid:pk>/',BusinessDetailView.as_view(), name='Business-Detail'),
    path('business-listing/',BusinessListingView.as_view(), name='Business-Listing'),
    path('logout/', log_out, name='logout'),
]