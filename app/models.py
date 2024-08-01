from django.db import models
from django.utils.text import slugify
from autoslug import AutoSlugField

# Create your models here.



class SocialMedia(models.Model):
    SOCIAL_MEDIA_CHOICES = (
        ('facebook', 'Facebook'),
        ('twitter', 'Twitter'),
        ('instagram', 'Instagram'),
        ('linkedin', 'Linkedin'),
        ('youtube', 'YouTube'),
        # Diğer sosyal medya platformları ekleyebilirsiniz
    )

    name = models.CharField(max_length=20, choices=SOCIAL_MEDIA_CHOICES, unique=True, verbose_name="Adı")
    link = models.URLField(verbose_name="Bağlantı")

    class Meta:
        verbose_name = "Sosyal Medya"
        verbose_name_plural = "Sosyal Medya"

    def __str__(self):
        return self.get_name_display()
    



class Address(models.Model):
    address = models.CharField(max_length=255, null=True, blank=True)
    whatsapp_number = models.CharField(max_length=15, null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)

    def __str__(self):
        if self.address:
            return self.address
        elif self.whatsapp_number:
            return self.whatsapp_number
        elif self.phone_number:
            return self.phone_number
        return 'Adres Bilgisi Yok'
    


class Category(models.Model):
    name = models.CharField(max_length=250, verbose_name='İsim')
    slug = AutoSlugField(populate_from='name', unique=True, verbose_name="Slug")
    description = models.TextField(blank=True, null=True, verbose_name='Açıklama')
    image = models.ImageField(upload_to='categories/', blank=True, null=True, verbose_name='Resim')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma Tarihi')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class Product(models.Model):
    CURRENCY_CHOICES = [
        ('EUR', 'Euro (€)'),
        ('USD', 'US Doları ($)'),
        ('TRY', 'Türk Lirası (₺)'),
        # Diğer para birimleri eklenebilir
    ]

    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', verbose_name='Kategori')
    name = models.CharField(max_length=250, verbose_name='İsim')
    slug = AutoSlugField(populate_from='name', unique=True, verbose_name="Slug")
    ingredients = models.TextField(blank=True, null=True, verbose_name='İçindekiler')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Fiyat')
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, default='EUR', verbose_name='Para Birimi')
    image = models.ImageField(upload_to='products/', blank=True, null=True, verbose_name='Resim')
    available = models.BooleanField(default=True, verbose_name='Mevcut')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma Tarihi')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_currency_symbol(self):
        symbols = {
            'EUR': '€',
            'USD': '$',
            'TRY': '₺',
            # Diğer para birimi sembolleri eklenebilir
        }
        return symbols.get(self.currency, '')

    def display_price(self):
        return f"{self.get_currency_symbol()}{self.price}"
    display_price.short_description = 'Fiyat'