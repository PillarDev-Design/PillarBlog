from django.contrib import admin
# Import Models
from blog.models import MainPageNote
from blog.models import PostType
from blog.models import BlogCategory
from blog.models import BlogPost
from blog.models import TutorialCategory
from blog.models import TutorialPost

#class BlogPostAdmin(admin.ModelAdmin):
    # Custom Admin View Parameters

# Register Models
admin.site.register(MainPageNote)
admin.site.register(PostType)
admin.site.register(BlogCategory)
admin.site.register(BlogPost)
admin.site.register(TutorialCategory)
admin.site.register(TutorialPost)
