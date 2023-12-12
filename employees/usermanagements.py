from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def __init__(self, db=None):
        super().__init__()
        self.host = 'kanotemm.com'

    def _create_user(self, username=None, email=None, password=None, **extra_fields):
        user = self.model(username=username, email=self.normalize_email(email), **extra_fields)
        print(f"password ={password}")
        user.set_password(password)
        user.save()
        return user

    def new_sale_staff(self, username, email, password, **extra_fields):
        if not username:
            raise ValueError("The given username must be provided")
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault("sale", True)
        extra_fields.setdefault('sale_dept', True)
        if not email:
            email = f"{username}.sale@{self.host}"
            print(email)
        return self._create_user(username, email, password, **extra_fields)

    def new_service_staff(self, username, email, password, **extra_fields):
        if not username:
            raise ValueError("The given username must be provided")
        extra_fields.setdefault('department', 'service')
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_staff', True)
        if not email:
            email = f"{username}.service@{self.host}"
        return self._create_user(username, email, password, **extra_fields)

    def new_audit_staff(self, username, email, password, **extra_fields):
        if not username:
            raise ValueError("The given username must be provided")
        extra_fields.setdefault('department', 'audit')
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_staff', True)
        if not email:
            email = f"{username}.audit@{self.host}"
        return self._create_user(username, email, password, **extra_fields)

    def new_financial_staff(self, username, email, password, **extra_fields):
        if not username:
            raise ValueError("The given username must be provided")
        extra_fields.setdefault('department', 'finance')
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)

        if not email:
            email = f"{username}.finance@{self.host}"
        return self._create_user(username, email, password, **extra_fields)

    def new_moderator(self, username, email, password, **extra_fields):
        if not username:
            raise ValueError("The given username must be provided")
        extra_fields.setdefault('moderator_staff', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('admin_team', True)
        if not email:
            email = f"{username}.finance@{self.host}"
        return self._create_user(username, email, password, **extra_fields)

    def new_manager(self, username, email, password, **extra_fields):
        if not username:
            raise ValueError("The given username must be provided")
        extra_fields.setdefault('department', 'manager')
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        if not email:
            email = f"{username}.finance@{self.host}"
        return self._create_user(username, email, password, **extra_fields)

    def create_superuser(self, username=None, email=None, password=None, **extra_fields):
        if not username:
            print("Your username will be 'admin'. ")
            username = 'admin'
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)

        return self._create_user(username, email, password, **extra_fields)
