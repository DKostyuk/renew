from django.contrib import admin
from .models import *
from django.forms import TextInput, Textarea


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 0


class ProductCategoryAdmin (admin.ModelAdmin):
    list_display = [field.name for field in ProductCategory._meta.fields]
    prepopulated_fields = {'slug': ('name',)}

    class Meta:
        model = ProductCategory

admin.site.register(ProductCategory, ProductCategoryAdmin)


class ProductAdmin (admin.ModelAdmin):
    list_display = ('name', 'ref_number', 'name_pl', 'name_common', 'slug', 'size', 'price', 'discount', 'category',
                    'is_active')

    def is_description(self, obj):
        if obj.description_1:
            return True
        else:
            return False
    is_description.short_description = 'Train'

    # list_display = [field.name for field in Product._meta.fields]
    prepopulated_fields = {'slug': ('name',)}
    inlines = [ProductImageInline]

    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '50'})},
        models.TextField: {'widget': Textarea(attrs={'rows': 4, 'cols': 100})},
    }

    class Meta:
        model = Product

admin.site.register(Product, ProductAdmin)


class ProductImageAdmin (admin.ModelAdmin):
    list_display = [field.name for field in ProductImage._meta.fields]

    class Meta:
        model = ProductImage

admin.site.register(ProductImage, ProductImageAdmin)


class ProductAddFileAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProductAddFile._meta.fields]

    class Meta:
        model = ProductAddFile

admin.site.register(ProductAddFile, ProductAddFileAdmin)
