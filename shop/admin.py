from django.contrib import admin

from shop.models import (
    Product,
    ProductImage,
    Attribute,
)


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]
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
    list_display = ('id', 'image', 'product')


@admin.register(Attribute)
class AttributeAdmin(admin.ModelAdmin):
    list_display = ('name',)
