from django.core.exceptions import PermissionDenied
from django.shortcuts import HttpResponseRedirect ,reverse


def role_required(allowed_roles=[]):
    def decorator(func):
        def wrap(request, *args, **kwargs):
            if request.role in allowed_roles:
                return func(request, *args, **kwargs)
            else:
                return HttpResponseRedirect(reverse('employee_list'))
        return wrap
    return decorator
