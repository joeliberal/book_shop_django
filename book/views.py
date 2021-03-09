from django.shortcuts import render, get_object_or_404
from .models import Book, BookInstance, Author, Gener
# Create your views here.
from django.views import generic
from django.contrib.auth.decorators import login_required, user_passes_test, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin
from .forms import RenewBookForm
from django.http import HttpResponseRedirect
from django.urls import reverse


def email_check(user):
    return user.email.endswith('@gmail.com')

@login_required
@permission_required('book.can_read_private_section')
@user_passes_test(email_check)
def index(request):
    
    user.has_perms = ('user.can_add')
    
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
        return user.email.endswith('@gmail.com')

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


class BorrowerListUser(PermissionRequiredMixin, generic.ListView):
    model = BookInstance
    template_name = 'book/borrower_lis_book.html'
    context_object_name = 'borrwoer'
    permission_required = 'book.can_read_private_section'
    def get_queryset(self):
        return BookInstance.objects.filter(borrower = self.request.user).filter(status__exact='o').order_by('due_back')


def renew_book_librarian(request, pk):
    book_inst = get_object_or_404(BookInstance, pk = pk)

    if request.method == 'POST':
        form = RenewBookForm(request.POST)

        if form.is_valid():
            book_inst.due_back = form.cleaned_data['renewal_date']
            book_inst.save()

            return HttpResponseRedirect(reverse('all-borrower')) #revers for use names urls.py


    else:
        propsed_renewal_date = datetime.date.today() + datetime.timedelta(weeks = 3)
        form = RenewBookForm(initial = {'renewal_date' : propsed_renewal_date}) # default value form for 3 weeks after


    context = {
        'form':form,
        'book_inst':book_inst,
    }

    return render(request, 'book/book_renew_librarian.html', context)
