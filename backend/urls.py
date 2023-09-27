
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from base.api import views




# from django.views import ProcessWebhookView


urlpatterns = [
    # path(
    #     "password-reset/",
    #     views.PasswordReset.as_view(),
    #     name="request-password-reset",
    # ),
    path(
        "password-reset/<str:encoded_pk>/<str:token>/",
        views.ResetPasswordAPI.as_view(),
        name="reset-password",
    ),
    path('admin/', admin.site.urls),
    path('api/', include('base.api.urls')),
    path('paypal/', include('paypal.standard.ipn.urls')),

    path('', views.hello_world, name='hello_world'),
    # path('', include('base.api.urls')), 
     
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)






