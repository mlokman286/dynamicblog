from django.contrib import admin

from blogs.models import Blogs, Category

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','category_name','created_at','updated_at')

class BlogsAdmin(admin.ModelAdmin):
    list_display = ('id','title','category','author','blog_image','status','is_fetured','created_at','updated_at')
    prepopulated_fields = {'slug':('title',)}
    search_fields = ('id','title','category__category_name','status')
    list_editable = ('is_fetured',)

admin.site.register(Category,CategoryAdmin)
admin.site.register(Blogs,BlogsAdmin)