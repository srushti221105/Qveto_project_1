from functools import wraps

from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied

from .roles import user_has_role


def role_required(*allowed_roles):
    """
    Restrict a Django view to users with specified roles.

    Example:
        @role_required("Admin", "HR")
        def hr_dashboard(request):
            ...
    """

    def decorator(view_func):
        @login_required
        @wraps(view_func)
        def wrapper(request, *args, **kwargs):
            if not any(
                user_has_role(request.user, role)
                for role in allowed_roles
            ):
                raise PermissionDenied(
                    "You do not have permission to access this page."
                )

            return view_func(request, *args, **kwargs)

        return wrapper

    return decorator