from django.contrib.auth.models import User, Group
from django.test import TestCase, RequestFactory
from django.http import HttpResponse
from django.core.exceptions import PermissionDenied
from django.contrib.auth.models import AnonymousUser

from .roles import user_has_role, create_default_roles
from .permissions import role_required


class RoleHelperTests(TestCase):
    def setUp(self):
        create_default_roles()
        self.employee = User.objects.create_user(
            username="employee1",
            password="testpass123"
        )
        self.employee.groups.add(Group.objects.get(name="Employee"))

    def test_user_has_assigned_role(self):
        self.assertTrue(user_has_role(self.employee, "Employee"))

    def test_user_does_not_have_unassigned_role(self):
        self.assertFalse(user_has_role(self.employee, "HR"))

    def test_anonymous_user_has_no_role(self):
        self.assertFalse(user_has_role(AnonymousUser(), "Employee"))


class RolePermissionDecoratorTests(TestCase):
    def setUp(self):
        create_default_roles()
        self.factory = RequestFactory()
        self.employee = User.objects.create_user(
            username="employee2",
            password="testpass123"
        )
        self.employee.groups.add(Group.objects.get(name="Employee"))

        self.hr = User.objects.create_user(
            username="hr1",
            password="testpass123"
        )
        self.hr.groups.add(Group.objects.get(name="HR"))

    def test_allowed_role_can_access_view(self):
        @role_required("HR")
        def sample_view(request):
            return HttpResponse("Success")

        request = self.factory.get("/test/")
        request.user = self.hr

        response = sample_view(request)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b"Success")

    def test_disallowed_role_is_denied(self):
        @role_required("HR")
        def sample_view(request):
            return HttpResponse("Success")

        request = self.factory.get("/test/")
        request.user = self.employee

        with self.assertRaises(PermissionDenied):
            sample_view(request)

    def test_unauthenticated_user_is_redirected(self):
        @role_required("HR")
        def sample_view(request):
            return HttpResponse("Success")

        request = self.factory.get("/test/")
        request.user = AnonymousUser()

        response = sample_view(request)

        self.assertEqual(response.status_code, 302)
        self.assertIn("/accounts/login/", response.url)