"""
URL configuration for tweet_django project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.shortcuts import render
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('tweet/', include('tweets.urls')),
    path('', include('tweets.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


def error_view(request, exception=None, status=500, message="Something went wrong."):
    return render(request, 'error.html', {
        "status_code": status,
        "message": message
    }, status=status)

handler404 = lambda request, exception: error_view(request, exception, 404, "Page not found.")
handler500 = lambda request: error_view(request, None, 500, "Internal server error.")
handler403 = lambda request, exception: error_view(request, exception, 403, "Permission denied.")
handler400 = lambda request, exception: error_view(request, exception, 400, "Bad request.")



