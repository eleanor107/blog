from django.contrib import admin 

# Register your models here.
from .models import Post

class PostModelAdmin(admin.ModelAdmin):
	list_display = ["title", "updated" , "timestamp"]
	list_display_links = ["updated"]
	list_filter = ["updated" , "timestamp"]
	search_fields = ["title", "content"]
	list_editable = ["title"]
	class Meta:
		model = Post

# built in function that registers post model into admin site 

admin.site.register(Post, PostModelAdmin) 

