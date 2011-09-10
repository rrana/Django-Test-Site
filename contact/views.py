from mysite.contact.forms import ContactForm
from django.shortcuts import render_to_response

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email', 'noreplay@example.com'),
                ['siteowner@example.com'],
                )
        return HttpResponseRedirect('/contact/thanks/')
    else:
        form = ContactForm(
            initial={'subject': 'I love your site!' }
            )
    return render_to_response('contact_form.html',
                                  {'form': form})
