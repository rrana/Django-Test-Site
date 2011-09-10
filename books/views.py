from django.shortcuts import render_to_response
from django.http import HttpResponse
from mysite.books.models import Book

def search(request):
    errors = []
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
           errors.append('Enter a search term.')
        elif len(q) > 20:
            errors.append('Please enter at most 20 characters.')
        else:
            books = Book.objects.filter(title__icontains=q)
            return render_to_response('search_results.html',
                                     {'books': books, 'query': q})
    return render_to_response('search_form.html', {'errors': errors})

def books(request):
    errors = []
    if 'book' in request.GET:
        book = request.GET['book']
        if not book:
            errors.appent('Please enter a search term.')
        else:
            title = Book.object.filter(title_icontains=book)
            return render_to_response('test.html', {'title': title, 'query': book})
        return render_to_response
