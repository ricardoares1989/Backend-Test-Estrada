from django.contrib.auth.base_user import BaseUserManager


class CustomUserManager(BaseUserManager):
    """
    Custom user for only set email instead of username as the unique
    identifier.
    """

    def create_user(self, email: str, password: str, **kwargs):
        """
        Create a employee user.
        Args:
            email (str): with format example@domain.com
            password (str): with all the ascii.letters, ascii.digits
                and ascii.punctuation
            **kwargs (dict)
        Returns:
            user (CustomUser):
        """
        if not email:
            raise ValueError("The email must be set")
        email = self.normalize_email(email)
        user = self.model(username=email, email=email, **kwargs)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **kwargs):
        """
        Manager for create a superuser with the attributes of
        is_staff, is_superuser and is_active.
        Args:
            email (str):
            password (str):
            **kwargs (Dict()):

        Returns: CustomUser instance with superuser attributes.

        """
        kwargs.setdefault("is_staff", True)
        kwargs.setdefault("is_superuser", True)
        kwargs.setdefault("is_active", True)

        if kwargs.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True")
        if kwargs.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True")
        return self.create_user(email, password, **kwargs)
