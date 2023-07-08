from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = "Janhvi Admin"
admin.site.site_title = "Janhvi's Site"
admin.site.index_title = "Welcome to UMSRA Researcher Portal"

urlpatterns = [
    path('dj-admin/', admin.site.urls),
   # path('admin/', include('customadmin.urls')),
    path('', include('home.urls')),
    # path('dashboard',views.dashboard, name='dashboard'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
