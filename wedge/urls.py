from django.urls import path
from django.contrib import admin

from ims import views as ims_views


urlpatterns = [
    path('admin/', admin.site.urls),

    path('ajax_fragment/<param>/', ims_views.ajax_fragment, name='ajax-fragment'),

    path('', ims_views.home, name='home'),
]
