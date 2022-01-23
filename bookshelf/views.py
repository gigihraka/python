from django.shortcuts import redirect, render
from django.http import Http404
from django.contrib import messages
from .models import Bookshelf
from .forms import BookForm

def index_view(request):
    books = Bookshelf.objects.all()
    context = {
        'books': books
    }
    return render(request, 'bookshelf/index.html', context)

def create_view(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            new_book = BookForm(request.POST)
            new_book.save()
            messages.success(request, 'Sukses Menambah Buku baru.')
            return redirect('bookshelf:index')
    else:
        form = BookForm()
    return render(request, 'bookshelf/form.html', {'form': form})

def update_view(request, book_id):
    try:
        books = Bookshelf.objects.get(pk=book_id)
    except Bookshelf.DoesNotExist:
        raise Http404("Buku tidak ditemukan.")
    if request.method == 'POST':
        form = BookForm(request.POST, instance=books)
        if form.is_valid():
            form.save()
            messages.success(request, 'Sukses Mengubah Buku.')
            return redirect('bookshelf:index')
    else:
        form = BookForm(instance=books)
    return render(request, 'bookshelf/form.html', {'form': form})

def delete_view(request, book_id):
    try:
        books = Bookshelf.objects.get(pk=book_id)
        books.delete()
        messages.success(request, 'Sukses Menghapus Buku.')
        return redirect('bookshelf:index')
    except Bookshelf.DoesNotExist:
        raise Http404("Buku tidak ditemukan.")