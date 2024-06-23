from django.contrib import admin

from shop.models import (
    Product,
    ProductImage,
    Attribute,
)

# Register your models here.

# admin.site.register(Product)
# admin.site.register(ProductImage)
# admin.site.register(Attribute)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'stock', 'images', 'get_attributes')

    @admin.display(description='Фото товара')
    def images(self, obj: Product):
        return list(obj.productimage_set.values_list('image', flat=True))

    @admin.display(description="Свойства")
    def get_attributes(self, obj: Product):
        return list(obj.attributes.all())

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.prefetch_related('productimage_set', 'attributes')


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ('image', 'product')


@admin.register(Attribute)
class AttributeAdmin(admin.ModelAdmin):
    list_display = ('name',)
