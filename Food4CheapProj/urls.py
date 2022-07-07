from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index),
    path('Baked Goods', views.bakedgood_view),
    path('Dairy', views.dairys_view),
    path('Fruits', views.fruits_view),
    path('Meats', views.meats_view),
    path('Seafoods', views.seafoods_view),
    path('Vegetables', views.vegetables_view),

    path('Baked Goods/<str:product>', views.bakedgood_product_view),
    path('Dairy/<str:product>', views.dairys_product_view),
    path('Fruits/<str:product>', views.fruits_product_view),
    path('Meat/<str:product>', views.meats_product_view),
    path('Seafoods/<str:product>', views.seafoods_product_view),
    path('Vegetables/<str:product>', views.vegetables_product_view),

    path('Signup', views.signup_view),
    path('Login', views.login_view),
    path('Account', views.account_view),
    path('About', views.about_view),

    path('delete_all_items_', views.delete_all_items, name='delete_all_items'),
    path('sign_out', views.sign_out, name='sign_out')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
