from django_filters import FilterSet
from .models import Store, Product, Combo


class StoreFilter(FilterSet):
    class Meta:
        model = Store
        fields = {
            'category': ['exact'],
        }


class ProductFilter(FilterSet):
    class Meta:
        model = Product
        fields = {
            'price': ['gt', 'lt']
        }


class ComboFilter(FilterSet):
    class Meta:
        model = Combo
        fields = {
            'combo_price': ['gt', 'lt']
        }
