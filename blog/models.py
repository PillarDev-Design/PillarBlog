from django.db import models
import datetime

# Create your models here.

#----------------------------------------------------------
# MainPageNote
# * This is the model that controls the front page content
#       that the users see. (Easily edited on the admin
#       page.
#----------------------------------------------------------
class MainPageNote(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    def __unicode__(self):
        return self.title

#----------------------------------------------------------
# PostType
# * The purpose of this model is to allow easy recalling on
#       the main page when seeing the admin's recent
#       activity (blogs,tutorials, etc.)
#----------------------------------------------------------
class PostType(models.Model):
    post_type = models.CharField(max_length=255)
    def __unicode__(self):
        return self.post_type

#----------------------------------------------------------
# BlogCategory
# * This model will be the categories of the blog posts
#----------------------------------------------------------
class BlogCategory(models.Model):
    category = models.CharField(max_length=255)
    description = models.TextField()
    def __unicode__(self):
        return self.category

#----------------------------------------------------------
# BlogPost
# * This model will contain the actual blog post data
#----------------------------------------------------------
class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    description = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    slug = models.CharField(max_length=255)
    post_type = models.ForeignKey(PostType)
    category = models.ForeignKey(BlogCategory)
    def __unicode__(self):
        return "%s %s %s" % (self.title, self.update_date, self.slug)

#----------------------------------------------------------
# TutorialCategory
# * This model will be the categories of the tutorial posts
#----------------------------------------------------------
class TutorialCategory(models.Model):
    category = models.CharField(max_length=255)
    description = models.TextField()
    def __unicode__(self):
        return self.category

#----------------------------------------------------------
# TutorialPost
# * This model will contain the actual tutorial post data
#----------------------------------------------------------
class TutorialPost(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    description = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    slug = models.CharField(max_length=255)
    post_type = models.ForeignKey(PostType)
    category = models.ForeignKey(TutorialCategory)
    def __unicode__(self):
        return "%s %s %s" % (self.title, self.update_date, self.slug)
