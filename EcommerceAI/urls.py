from django.contrib import admin
from django.urls import path,include

handler404 = 'base.views.custom_page_not_found_view'
handler500 = 'base.views.custom_error_view'
handler403 = 'base.views.custom_permission_denied_view'
handler400 = 'base.views.custom_bad_request_view'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base.urls')),
]
