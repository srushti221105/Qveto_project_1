from django.contrib.auth.models import Group

ADMIN = "Admin"
HR = "HR"
EMPLOYEE = "Employee"

USER_ROLES = [
    ADMIN,
    HR,
    EMPLOYEE,
]


def user_has_role(user, role):
    """Check whether an authenticated user belongs to a role group."""

    if not user.is_authenticated:
        return False

    if role == ADMIN and user.is_superuser:
        return True

    return user.groups.filter(name=role).exists()


def create_default_roles():
    """Create the default role groups if they do not exist."""

    for role in USER_ROLES:
        Group.objects.get_or_create(name=role)