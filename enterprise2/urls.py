from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import path, include
from core.views import Home


urlpatterns = [
    path('', login_required(Home.as_view()), name='home'),
    path('admin/', admin.site.urls),
    path('framework/', include('core.urls')),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls'))
]