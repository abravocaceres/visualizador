from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

def random_word(request):  
    if 'counter' in request.session:
        request.session['counter'] += 1
        palAl = get_random_string(length = 14)
    else:
        request.session['counter'] = 1
        palAl = get_random_string(length = 14)
    context = {'contador': request.session['counter'], 'palabraAl': palAl}
    return render(request, 'random_word.html', context)

def restart_counter(request):
    request.session.pop('counter')
    return redirect('/random_word')


