from django.http import HttpResponse
from django.shortcuts import redirect

def unauthenticated_user(view_function):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return view_function(request, *args, **kwargs)
    return wrapper_func

def allowed_user(allowed_roles=[]):
    def decorator(view_function):
        def wrapper_function(request, *args, **kwargs):
            group= None
            if request.user.groups.exists():
                group= request.user.groups.all()[0].name
            if group in allowed_roles:
               return view_function(request, *args, **kwargs)
            else:
                return HttpResponse('You are not authorized to view this page.')
        return wrapper_function
    return decorator

def admin_only(view_function):
    def wrapper_function(request, *args, **kwargs):
        group= None
        if request.user.groups.exists():
            group= request.user.groups.all()[0].name
            if group=='customers':
                return redirect('user')
            if group=='admin':
                return view_function(request, *args, **kwargs)
    return wrapper_function

        