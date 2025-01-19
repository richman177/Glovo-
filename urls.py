from django.contrib.auth.views import LogoutView
from .views import *
from django.urls import path, include
from rest_framework import routers


router = routers.SimpleRouter()
router.register(r'users', UserProfileViewSet, basename='users'),
router.register(r'cart', CartAPIView, basename='carts'),
router.register(r'cart_item', CartItemAPIView, basename='cart_item'),


urlpatterns = [
    path('', include(router.urls)),
    path('store/', StoreListAPIView.as_view(), name='store_list'),
    path('store/<int:pk>/', StoreDetailAPIView.as_view(), name='store_detail'),
    path('store/create/', StoreCreateAPIView.as_view(), name='store-create'),
    path('store_list/', StoreOwnerAPIView.as_view(), name='store_list_owner'),
    path('store_list/<int:pk>/', StoreDetailUpdateDestroyOwnerAPIView.as_view(), name='store_list_edit'),
    path('category/', CategoryListAPIView.as_view(), name='category_list'),
    path('category/<int:pk>/', CategoryDetailAPIView.as_view(), name='category_detail'),
    path('products/', ProductListAPIView.as_view(), name='product_list'),
    path('products/<int:pk>/', ProductDetailAPIView.as_view(), name='product_detail'),
    path('products/create/', ProductCreateAPIView.as_view(), name='product-create'),
    path('product_list/', ProductOwnerAPIView.as_view(), name='product_list_owner'),
    path('product_list/<int:pk>/', ProductDetailUpdateDestroyOwnerAPIView.as_view(), name='product_list_edit'),
    path('review/', StoreReviewCreateAPIView.as_view(), name='review-create'),
    path('combo/', ComboListAPIView.as_view(), name='combo_list'),
    path('combo/<int:pk>/', ComboDetailAPIView.as_view(), name='combo_detail'),
    path('combo/create/', ComboCreateAPIView.as_view(), name='combo-create'),
    path('combo_list/', ComboOwnerAPIView.as_view(), name='combo_list_owner'),
    path('combo_list/<int:pk>/', ProductDetailUpdateDestroyOwnerAPIView.as_view(), name='combo_list_edit'),
]

