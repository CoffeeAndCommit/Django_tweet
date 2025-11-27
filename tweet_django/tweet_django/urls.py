

from django.contrib import admin
from django.shortcuts import render
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.urls import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('tweet/', include('tweets.urls')),
    path('', include('tweets.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
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



