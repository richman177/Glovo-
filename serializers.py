from rest_framework import serializers
from .models import *


class UserProfileFullSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class UserProfileSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['username']


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'category_name']


class CategorySimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['category_name']


class StoreListSerializer(serializers.ModelSerializer):
    category = CategorySimpleSerializer()
    avg_rating = serializers.SerializerMethodField()
    count_rating = serializers.SerializerMethodField()
    good_grade = serializers.SerializerMethodField()

    class Meta:
        model = Store
        fields = ['id', 'store_name', 'category', 'store_image', 'avg_rating', 'count_rating', 'good_grade']

    def get_avg_rating(self, obj):
        return obj.get_avg_rating()

    def get_count_rating(self, obj):
        return obj.get_count_rating()

    def get_good_grade(self, obj):
        return obj.get_good_grade()


class StoreCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = '__all__'


class CategoryDetailSerializer(serializers.ModelSerializer):
    category_store = StoreListSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['category_name', 'category_store',]


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['title', 'contact_number', 'social_network']


class ComboListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Combo
        fields = ['combo_name', 'combo_image', 'description', 'combo_price']


class ComboDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Combo
        fields = ['combo_name', 'combo_image','description', 'combo_price']


class ComboCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Combo
        fields = '__all__'


class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['product_name', 'product_image', 'description', 'price']


class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['product_name', 'product_image', 'description', 'price']


class ProductCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'


class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class CourierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courier
        fields = '__all__'


class StoreReviewSerializer(serializers.ModelSerializer):
    client = UserProfileSimpleSerializer()
    created_date = serializers.DateTimeField(format('%d-%m-%Y %H:%M'))

    class Meta:
        model = StoreReview
        fields = ['client', 'text', 'stars', 'created_date']


class CourierRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourierRating
        fields = '__all__'


class StoreReviewCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoreReview
        fields = '__all__'


class StoreDetailSerializer(serializers.ModelSerializer):
    category = CategorySimpleSerializer()
    contact = ContactSerializer(many=True, read_only=True)
    product_list = ProductListSerializer(many=True, read_only=True)
    combo_list = ComboListSerializer(many=True, read_only=True)
    store_review = StoreReviewSerializer(many=True, read_only=True)
    owner = UserProfileSimpleSerializer()

    class Meta:
        model = Store
        fields = ['store_name', 'category', 'description', 'store_image', 'address', 'contact', 'owner',
                  'product_list', 'combo_list', 'store_review']