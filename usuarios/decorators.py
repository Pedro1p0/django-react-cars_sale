from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from functools import wraps

def login_and_role_required(roles=None):
    def decorator(view_func):
        @wraps(view_func)
        @login_required
        def wrapped_view(request, *args, **kwargs):
            if request.user.role in roles:
                return view_func(request, *args, **kwargs)
            else:
                return redirect('locadora:pagina_principal')  # Redirecionar para a página inicial ou para uma página de permissão negada
        return wrapped_view
    return decorator

