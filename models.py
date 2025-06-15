from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import MinValueValidator, MaxValueValidator


class UserProfile(AbstractUser):   
    phone_number = PhoneNumberField(null=True, blank=True)
    profile_image = models.ImageField(upload_to='profiles')
    age = models.PositiveSmallIntegerField(validators=[MinValueValidator(18), MaxValueValidator(65)], null=True, blank=True)
    STATUS_CHOICES = (
        ('client', 'Client'),
        ('courier', 'Courier'),
        ('owner', 'Owner'),
    )
    status = models.CharField(max_length=33, choices=STATUS_CHOICES, default='client')
    date_registered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.first_name}, {self.last_name}, {self.username}'


class Category(models.Model):
    category_name = models.CharField(max_length=33, unique=True)

    def __str__(self):
        return self.category_name


class Store(models.Model):
    store_name = models.CharField(max_length=55)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category_store')
    description = models.TextField()
    store_image = models.ImageField(upload_to='store_images')
    address = models.CharField(max_length=66)
    owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='client' )

    def __str__(self):
        return f'{self.store_name}'


    def get_avg_rating(self):
        ratings = self.store_review.all()
        if ratings.exists():
            return round(sum([i.stars for i in ratings]) / ratings.count(), 1)
        return 0

    def get_count_rating(self):
        ratings = self.store_review.all()
        if ratings.exists():
            if ratings.count() > 3:
                return '3+'
            return ratings.count()
        return 0

    def get_good_grade(self):
        ratings = self.store_review.all()
        if ratings.exists():
            totel_people = 0
            for i in ratings:
                if i.stars > 3:
                    totel_people += 1
            return f'{(totel_people * 100) / ratings.count()}%'
        return '0%'


class Contact(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='contact')
    title = models.CharField(max_length=33)
    contact_number = PhoneNumberField()
    social_network = models.URLField(null=True, blank=True)

    def __str__(self):
        return f'{self.title}, {self.contact_number}'


class Product(models.Model):
    product_name = models.CharField(max_length=33)
    description = models.TextField()
    product_image = models.ImageField(upload_to='product_images')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='product_list')

    def __str__(self):
        return f'{self.product_name}'


class Combo(models.Model):
    combo_name = models.CharField(max_length=66)
    description = models.TextField()
    combo_image = models.ImageField(upload_to='combo_images')
    combo_price = models.DecimalField(max_digits=10, decimal_places=2)
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='combo_list')

    def __str__(self):
        return f'{self.combo_name}'


class Cart(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    combo = models.ForeignKey(Combo, on_delete=models.CASCADE, null=True, blank=True)
    quantity = models.PositiveSmallIntegerField(default=1)


class Order(models.Model):
    client = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='client_profile')
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    ORDER_STATUS_CHOICES = (
        ('Ожидает обработки', 'Ожидает обработки'),
        ('Доставлен', 'Доставлен'),
        ('В процессе доставки', 'В процессе доставки'),
        ('Отменен', 'Отменен'),
    )
    order_status = models.CharField(max_length=66, choices=ORDER_STATUS_CHOICES, default='Ожидает обработки')
    delivery_address = models.CharField(max_length=122)
    courier = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='courier_profile')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.order_status


class Courier(models.Model):
    courier = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    current_order = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='orders')
    CURRENT_STATUS_CHOICES = (
        ('Доступен', 'Доступен'),
        ('Занят', 'Занят')
    )
    courier_status = models.CharField(max_length=66, choices=CURRENT_STATUS_CHOICES)

    def __str__(self):
        return f'{self.courier}, {self.courier_status}'


class StoreReview(models.Model):
    client = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='store_review')
    text = models.TextField()
    stars = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.client}, {self.store}'


class CourierRating(models.Model):
    client = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='clients')
    courier = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='couriers')
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1,6)])
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.client}, {self.courier}'
