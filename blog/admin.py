from django.contrib import admin
# Import Models
from blog.models import MainPageNote
from blog.models import PostType
from blog.models import BlogCategory
from blog.models import BlogPost

#class BlogPostAdmin(admin.ModelAdmin):
    # Custom Admin View Parameters

# Register Models
admin.site.register(MainPageNote)
admin.site.register(PostType)
admin.site.register(BlogCategory)
admin.site.register(BlogPost)
