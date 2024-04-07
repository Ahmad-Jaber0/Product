from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views
from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static
#router = DefaultRouter()
#router.register('Product', views.viewsets_Product)
urlpatterns = [
    path('', views.index, name='index'), 
    path('add-product/', views.AddProductAPIView.as_view(), name='add_product'),
    path('edit-product/<int:pk>/', views.EditProductAPIView.as_view(), name='edit_product'),
    path('delete-product/<int:pk>/', views.DeleteProductAPIView.as_view(), name='delete_product'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
'''
urlpatterns = [
    path('home/', views.index, name='index'), 
    #path('add/', views.add_product, name='add_product'),
    path('rest/AddProduct/', views.AddProductAPIView.as_view(),name="AddProductAPIView"),
    path('edit/<int:pk>/', views.edit_product, name='edit_product'),
    path('delete/<int:pk>/', views.delete_product, name='delete_product'),
    #path('wether/', views.wether, name='wether'),
    #path('no_rest_from_model/', views.no_rest_from_model, name='no_rest_from_model'),
    #path('rest/mixins/', views.mixins_list.as_view()),
    #path('rest/mixins/<int:pk>', views.mixins_pk.as_view()),
    #path('rest/generics/', views.generics_list.as_view(),),
    #path('rest/generics/<int:pk>', views.generics_pk.as_view()),
    path('rest/viewsets/', include(router.urls)),

]
'''