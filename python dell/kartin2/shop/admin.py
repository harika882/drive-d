from django.contrib import admin
from.models import Category,Product
class CategoryAdmin(admin.ModelAdmin):
    list_display=['id','name','slug']
    prepopulated_fields = {'slug':('name',)}
    ordering = ['name']
    list_display_links = ['id','name','slug']
admin.site.register(Category,CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug','stock']
    prepopulated_fields = {'slug' : ('name', )}
    list_editable = ['stock']
admin.site.register ( Product,ProductAdmin )


