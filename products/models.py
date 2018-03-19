from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify
import openpyxl
from django.contrib.auth.models import User
from unidecode import unidecode


class ProductCategory(models.Model):
    name = models.CharField(max_length=16, blank=True, null=True, default=None)
    slug = models.SlugField(max_length=16, unique=True)
    description = RichTextField(blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = 'CategoryProduct'
        verbose_name_plural = 'CategoryProducts'


class Product(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True, default=None)
    ref_number = models.CharField(max_length=7, blank=True, null=True, default=None)
    name_common = models.CharField(max_length=64, blank=True, null=True, default=None)
    name_pl = models.CharField(max_length=64, blank=True, null=True, default=None)
    slug = models.SlugField(max_length=64, unique=True)
    size = models.CharField(max_length=10, blank=True, null=True, default=None)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    discount = models.IntegerField(default=0)
    category = models.ForeignKey(ProductCategory, blank=True, null=True, default=None)
    name_description = models.CharField(max_length=64, blank=True, null=True, default='Opis')
    description = RichTextField(default=None)
    # description = models.TextField(blank=True, null=True, default=None)
    name_description_1 = models.CharField(max_length=64, blank=True, null=True, default='Sposób użycia')
    description_1 = RichTextField(default=None)
    name_description_2 = models.CharField(max_length=64, blank=True, null=True, default='Składniki aktywne')
    description_2 = RichTextField(default=None)
    name_description_3 = models.CharField(max_length=64, blank=True, null=True, default='Zużycie')
    description_3 = models.CharField(max_length=5, blank=True, null=True, default=None)
    name_description_4 = models.CharField(max_length=64, blank=True, null=True, default=None)
    description_4 = models.TextField(blank=True, null=True, default=None)
    name_description_5 = models.CharField(max_length=64, blank=True, null=True, default=None)
    description_5 = models.TextField(blank=True, null=True, default=None)
    short_description = models.TextField(blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        # return "%s" % self.name
        return "%s, %s" % (self.price, self.name)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        # self.slug = slugify(unidecode(self.name))
        super(Product, self).save(*args, **kwargs)


class ProductImage(models.Model):
    product = models.ForeignKey(Product, blank=True, null=True, default=None)
    image = models.ImageField(upload_to='products_images/')
    is_active = models.BooleanField(default=True)
    is_main = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s" % self.id

    class Meta:
        verbose_name = 'Photo'
        verbose_name_plural = 'Photos'


class ProductAddFile(models.Model):
    comments = models.CharField(max_length=124, blank=True, null=True, default=None)
    product_file = models.FileField(upload_to='product_file_add/')
    is_active = models.BooleanField(default=False)
    start_import = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    modified_by = models.ForeignKey(User, blank=True, null=True, default=None)

    def __str__(self):
        return "%s" % self.id
        # return "%s, %s" % (self.price_avg, self.name)

    def __unicode__(self):
        return "%s" % self.id
        # return "%s, %s" % (self.price_avg, self.name)

    class Meta:
        verbose_name = 'ProductAddFile'
        verbose_name_plural = 'ProductAddFiles'

    def save(self, *args, **kwargs):
        file_opened = openpyxl.load_workbook(filename=self.product_file) # put attention for Excel file version
        active_sheet = file_opened.active
        data_file = active_sheet.values
        data_file = list(data_file)
        for i in range(1, len(data_file)):
            name_common = data_file[i][0]
            name = data_file[i][1]
            ref_number = data_file[i][2]
            name_pl = data_file[i][3]
            size = data_file[i][4]
            price = data_file[i][5]
            discount = data_file[i][6]
            category = ProductCategory.objects.get(id=data_file[i][8])
            zus_number = data_file[i][9]
            d = data_file[i][10]
            d_1 = data_file[i][11]
            d_2 = data_file[i][12]
            # category = data_file[i][7]  # try delete it (not needed)
            new_product = Product(
                name_common=name_common,
                name=name,
                ref_number=ref_number,
                name_pl=name_pl,
                size=size,
                price=price,
                discount=discount,
                category=category,
                description_3=zus_number,
                description=d,
                description_1=d_1,
                description_2=d_2,
                is_active=True)
            new_product.save()

            super(ProductAddFile, self).save(*args, **kwargs)
