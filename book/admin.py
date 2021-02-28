from django.contrib import admin
from .models import Author, Book, BookInstance, Gener 
# Register your models here.
admin.site.register(Author)
admin.site.register(BookInstance)
admin.site.register(Book)
admin.site.register(Gener)
