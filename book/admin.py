from django.contrib import admin
from .models import Author, Book, BookInstance, Gener 
# Register your models here.

admin.site.register(Gener)

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_birth', 'date_death')
   
    fields = [
        'first_name',
        'last_name',
        ('date_birth', 'date_death')
        ]

class BookInstanceInline(admin.TabularInline):
    model = BookInstance

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_gener')
    inlines = [BookInstanceInline]
    
    def display_gener(self, obj): #for look manytomanyfields
        return ', '.join([gener.name for gener in obj.gener.all()[:3]])

    display_gener.short_description = 'Gener'


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ('status', 'due_back', 'borrower', 'id')
    fieldsets = (
        (None, {
            'fields':('book', 'imprint', 'id')
        }),
        ('Advailable',{
            'fields':('status', 'due_back', 'borrower')
        })
    )    
