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
            user (User):
        """
        if not email:
            raise ValueError("The email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.save()
        return user
