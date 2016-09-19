from django.shortcuts import render_to_response


def index(request):
    return render_to_response('index.html')


def signup(request):
    return render_to_response('signup.html')


def logged_in(request):
    return render_to_response('logged_in.html', {'email': request.user.email})
