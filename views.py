from django.shortcuts import render_to_response
from django.http import HttpResponse
import datetime

def hello(request):
    return HttpResponse("Hello world")

def current_datetime(request):
    current_date = datetime.datetime.now()
   # t = get_template('current_datetime.html')
   # html = t.render(Context({'current_date':now}))
   # return HttpResponse(html)
   # return render_to_response('current_datetime.html', {'current_date':now})
    return render_to_response('current_datetime.html', locals())
    
def hours_ahead(request, offset):
    try:
        offset=int(offset)
    except ValueError:
        raise Http404()
    next_time = datetime.datetime.now() + datetime.timedelta(hours=offset)
    return render_to_response('hours_ahead.html', locals())

def display_meta(request):
        return render_to_response('meta.html',{'values': sorted(request.META.items())})
        
