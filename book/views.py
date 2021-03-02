from django.shortcuts import render
from .models import Book, BookInstance, Author, Gener
# Create your views here.
from django.views import generic
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

def email_check(user):
    reurn user.email.endswith('@gmail.com')


@login_required
@user_passes_test(emaile_check)
def index(request):
    num_book = Book.objects.all().count()
    num_instance = BookInstance.objects.all().count()
    num_instance_available = BookInstance.objects.filter(status__exact = 'a' )
    num_author = Author.objects.count()

    context={
        'num_book':num_book,
        'num_instance':num_instance,
        'num_instance_available':num_instance_available,
        'num_author':num_author,
    } 
    return render(request, 'book/index.html', context)

class BookLisView(LoginRequiredMixin, UserPassesTestMixin, generic.ListView):
    model = Book
    paginate_by = 5
    login_url = 'accoints/login/'
    redirect_field_name = '/book'

    def test_func(self):
        reurn user.email.endswith('@gmail.com')

    #context_object_name = 'book_list'
    #template_name = 'book/book_list.html'
    #queryset = Book.objects.filter(title__icontains = 'python')[:5]

    #def get_queryset(self):
    #    return Book.objects.filter(title__icontains = 'python')[:5]

    #def get_context_data(self, **kwargs):
    #    context = super(BookLisView, self).get_context_data(**kwargs)
    #    context['my_book_list'] = Book.objects.all()
    #    return context


class BookDetailView(generic.DetailView):
    model = Book
    context_object_name = 'book'