from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('login/', views.login_user, name="login_User"),
    path('logout/', views.logout_user, name="logout_User"),
    path('sales/', views.sales_view, name="user_sales"),
    path('orders/', views.orders_view, name="user_orders"),
    path('not-found/', views.page_not_found, name="page_not_found"),
    path('create-user/', views.signup_users, name="create_user"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
