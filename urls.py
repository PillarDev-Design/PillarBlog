from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    
    #----------------------------------------------------------
    # Homepage
    url(r'^$', 'blog.views.home'), 
    #----------------------------------------------------------


    #----------------------------------------------------------
    # Directory
    url(r'^directory/(?P<post_type>.+)/', 'blog.views.directory'),
    #----------------------------------------------------------

    #----------------------------------------------------------
    # Blogs
    # Blog search page
    #url(r'^blog_search/', 'blog.views.blog_search'),
    # Blog post page
    #url(r'^blog/(?P<target_slug>.+)$', 'blog.views.get_blog'), 
    #----------------------------------------------------------
 
    #----------------------------------------------------------
    # Tutorials
    # Tutorial search page
    #url(r'^blog_search/', 'blog.views.blog_search'),
    # Tutorial post page
    #url(r'^blog/(?P<target_slug>.+)$', 'blog.views.get_blog'), 
    #----------------------------------------------------------

    #----------------------------------------------------------
    # About
    # About page
    url(r'^about/', 'blog.views.about'),
    #----------------------------------------------------------
    
)

#urlpatterns += staticfiles_urlpatterns()

urlpatterns += patterns('', url(r'^staticfiles/(?P<path>.*)$',
    'django.views.static.serve', {'document_root':'data/www',
        'show_indexes':True}),)
