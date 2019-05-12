from django.http import HttpResponse
from django.template.loader import render_to_string


def show_main_page(request):
    result = render_to_string('main.html', {
        'title': 'Books',
    })

    return HttpResponse(result)
