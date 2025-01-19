from .serializers import *
from .models import *
from rest_framework import viewsets, generics
from .filters import StoreFilter, ProductFilter, ComboFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .permissions import CheckOwner, CheckUserReview, CheckStoreOwner


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileFullSerializer

    def get_queryset(self):
        return UserProfile.objects.filter(id=self.request.user.id)


class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer


class CategoryDetailAPIView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryDetailSerializer


class StoreListAPIView(generics.ListAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreListSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = StoreFilter
    search_fields = ['store_name']


class StoreOwnerAPIView(generics.ListAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreListSerializer

    def get_queryset(self):
        return Store.objects.filter(owner=self.request.user)


class StoreDetailAPIView(generics.RetrieveAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreDetailSerializer


class StoreCreateAPIView(generics.CreateAPIView):
    serializer_class = StoreCreateSerializer
    permission_classes = [CheckOwner]


class StoreDetailUpdateDestroyOwnerAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreCreateSerializer
    permission_classes = [CheckOwner, CheckStoreOwner]


class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = ProductFilter
    search_fields = ['Product_name']
    ordering_fields = ['price']


class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer


class ProductCreateAPIView(generics.CreateAPIView):
    serializer_class = ProductCreateSerializer


class ProductOwnerAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer


class ProductDetailUpdateDestroyOwnerAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductCreateSerializer
    permission_classes = [CheckOwner]


class ComboListAPIView(generics.ListAPIView):
    queryset = Combo.objects.all()
    serializer_class = ComboListSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = ComboFilter
    search_fields = ['combo_name']
    ordering_fields = ['combo_price']


class ComboDetailAPIView(generics.RetrieveAPIView):
    queryset = Combo.objects.all()
    serializer_class = ComboDetailSerializer


class ComboCreateAPIView(generics.CreateAPIView):
    serializer_class = ComboCreateSerializer


class ComboOwnerAPIView(generics.ListAPIView):
    queryset = Combo.objects.all()
    serializer_class = ComboListSerializer


class ComboDetailUpdateDestroyOwnerAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Combo.objects.all()
    serializer_class = ComboCreateSerializer
    permission_classes = [CheckOwner]


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class CartAPIView(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


class CartItemAPIView(viewsets.ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer


class CourierAPIView(viewsets.ModelViewSet):
    queryset = Courier.objects.all()
    serializer_class = CourierSerializer


class StoreReviewCreateAPIView(generics.CreateAPIView):
    serializer_class = StoreReviewCreateSerializer
    permission_classes = [CheckUserReview]


class CourierRatingViewSet(viewsets.ModelViewSet):
    queryset = CourierRating.objects.all()
    serializer_class = CourierRatingSerializer
    permission_classes = [CheckUserReview]