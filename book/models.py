from django.db import models
import uuid
# Create your models here.


class Gener(models.Model):
    name = models.CharField(max_length=200, help_text='Enter a book gener')

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    summery = models.TextField()
    ISBN = models.CharField(max_length=13)
    gener = models.ManyToManyField(Gener)
    author = models.ForeignKey('Author', on_delete = models.SET_NULL, null=True)

    def __str__(self):
        return self.title

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_birth = models.DateField(null=True, blank=True)
    date_death = models.DateField(null=True, blank=True)    

    def __str__(self):
        return f'{self.first_name}-{self.last_name}'

class BookInstance(models.Model):
    LOAN_STATUS = (
        ('m', 'Maintence'),
        ('o', 'On Loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    book = models.ForeignKey(Book, on_delete=models.SET_NULL, null=True)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='m')

    class Meata:
        ordering=['due_back']

    def __str__(self):
        return f'{self.id}-{self.book.title}'
        