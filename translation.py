from .models import Category, Store, Contact, Product, Combo
from modeltranslation.translator import TranslationOptions,register

@register(Category)
class ProductTranslationOptions(TranslationOptions):
    fields = ('category_name',)



@register(Store)
class ProductTranslationOptions(TranslationOptions):
    fields = ('store_name', 'description', 'address',)


@register(Contact)
class ProductTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ('product_name', 'description',)



@register(Combo)
class ProductTranslationOptions(TranslationOptions):
    fields = ('combo_name', 'description')