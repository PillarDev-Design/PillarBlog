#----------------------------------------------------------
# * Imports
#----------------------------------------------------------
import models
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail, EmailMessage
from django.core.context_processors import csrf
from django.template import RequestContext

# import forms
# from forms import ContactForm

#----------------------------------------------------------
# * home (Default loaded homepage)
#----------------------------------------------------------
def home(request):
    
    main_page_notes = models.MainPageNote.objects.all().order_by('-pub_date')[:5]
    post_type = models.PostType.objects.all()
    front_page_blogs = models.BlogPost.objects.all().order_by('-pub_date')[:3]
    
    response_dict = {
            'main_page_notes':main_page_notes,
            'post_type':post_type,
            'front_page_blogs':front_page_blogs,
            }
    return render_to_response('blog/home.html', response_dict)

#----------------------------------------------------------
# * directory (Load in which type of directory)
#----------------------------------------------------------
def directory(request, post_type=None):
    
    blog_directory = False
    #search_item_type = None
    #search_category_type = None
    #search_identifier = None
    #search_item_type_blog = False
    #search_category_type_blog = False
    # Set search types according to the post type
    if post_type == 'blog':
        search_item_type = 'BlogPost'
        search_category_type = 'BlogCategory'
        blog_directory = True

    directory_item = None
    directory_category = None
    directory_sides = None
    
    # Run the loop to set the return dict to the post type results
    directory_item = models.__dict__[search_item_type].objects.all().order_by('pub_date')
    directory_category = models.__dict__[search_category_type].objects.all()
    directory_sides = models.__dict__[search_item_type].objects.all().order_by('-pub_date')[:5]

    response_dict = {
            'blog_directory':blog_directory,
            'directory_item':directory_item,
            'directory_category':directory_category,
            'directory_sides':directory_sides,
            }
    return render_to_response('blog/directory.html', response_dict)


#----------------------------------------------------------
# * search (Load in which type of search)
#----------------------------------------------------------
def search(request, post_type):
    # Set return_dict variables to none to avoid invalid
    #   return dictionaries.
    search_item_type = None
    search_sides = None
    search_items = None
    q = None
    error = False

    # Set search types according to the post type
    if post_type == 'blog':
        search_item_type = 'BlogPost'
    
    search_sides = models.__dict__[search_item_type].objects.all().order_by('-pub_date')[:5]

    # Check to see if GET request in URL bar correspends with database query
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            error = True
        else:
            search_items = models.__dict[search_item_type].objects.filter(title__icontains=q)

    response_dict = {
            'error':error,
            'query':q,
            'search_sides':search_sides,
            'search_item_type':search_item_type,
            'search_items':search_items,
            }
