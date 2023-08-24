from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'djangoapp'
urlpatterns = [
    # route is a string contains a URL pattern
    # view refers to the view function
    # name the URL  path for mytemplate
    path('mytemplate/', views.my_view, name='myview'),
    # path for about view
    path('about/', views.about, name='about'),

    # path for contact us view
    path('contactus/', views.contact, name='contactus'),


    # path for registration

    # path for login

    # path for logout

    path(route='', view=views.get_dealerships, name='index'),

    # path for dealer reviews view

    # path for add a review view

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)