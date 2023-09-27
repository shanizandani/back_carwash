# from django.urls import path
# from . import views
# from .views import MyTokenObtainPairView

# from rest_framework_simplejwt.views import (
#     TokenRefreshView,
# )


# urlpatterns = [
#     path('', views.getRoutes),
#     path('notes/', views.getNotes),

#     path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
#     path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
# ]





from django.urls import path, include
from . import views
from.views import MyTokenObtainPairView, ProcessWebhookView
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)


from .views import  UserOrdersAPIView
from django.conf.urls.static import static
from django.conf import settings






urlpatterns = [
    path('', views.getRoutes),
    # path('notes/' , views.getNotes),

    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', views.register_user, name='register'),
    # ----------------------------------
    path('auth/', include('djoser.urls')),
     path('auth/', include('djoser.urls.jwt')),

    # path('forgot-password/', ForgotPasswordView.as_view(), name='forgot-password'),
   
    path('products/', views.getProducts, name='get_products'),
    # path('products/<int:id>/', views.product_api, name='product_detail'),
    path('orders/', views.getOrders, name='get_orders'),
    # path('orders/create/', views.create_order, name='order-create'), 

    path('orders/create/', views.create_or_update_order, name='create_order'),
    path('orders/update/<int:order_id>/', views.create_or_update_order, name='update_order'),
    # path('orders/<int:order_id>/update_washing_amount/', views.update_washing_amount, name='update_washing_amount'),
    
    # Define the URL for retrieving an order by ID
    path('orders/<int:order_id>/', views.create_or_update_order, name='get_order_by_id'),

    path('orders/user/<int:user_id>/', views.getOrders, name='get_orders'),

    # path('users/', views.get_all_users, name='get_all_users'),
    #  path('users/<int:user_id>/', views.get_user_by_id, name='get_user_by_id'), 
     path('orders/user/', UserOrdersAPIView.as_view(), name='user-orders'),
     path("webhooks/paypal/", ProcessWebhookView.as_view()),
    #  path('paypal/webhook/', paypal_webhook, name='paypal-webhook'),

    # path('orders', views.create_order_view, name='create_order'),
    # path('orders/<str:order_id>/capture', views.capture_payment_view, name='capture_payment'),

    #  path('', views.home , name='home'),
    #  path("paypal-return/", views.paypal_return, name='paypal-return'),
    #  path("paypal-cancel", views.paypal_cancel, name="paypal-cancel"),
    re_path(r'^media/(?P<path>.*)$', static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)),


    #   path('notes/', views.getNotes),
    # path('orders/<int:order_id>/update_washing_amount/', views.update_washing_amount, name='update_washing_amount'),
    # path('change_password/', change_password, name='change_password'),
    # path('reset-password/<str:token>/', views.reset_password, name='reset-password'),

    # path("password-reset/<str:token>/",views.ResetPasswordAPI.as_view(),name="reset-password" ),
        path(
        "password-reset/",
        views.PasswordReset.as_view(),
        name="request-password-reset",
    ),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


