from django.views.generic import RedirectView
from django.contrib import admin
from django.urls import path,include,re_path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('admin/', admin.site.urls),

    path('', RedirectView.as_view(pattern_name='person_changelist'), name='home'),
    path('applicant/', include('applicant.urls')),
]
