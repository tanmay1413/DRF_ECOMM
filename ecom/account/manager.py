from django.contrib.auth.models import AbstractUser, BaseUserManager
# Custom User Manager
class UserManager(BaseUserManager):
    def create_user(self, email, phone_number, password=None, **extra_fields):
        """
        Create and save a regular user with the given email and phone number.
        """
        if not email:
            raise ValueError("The Email field is required")
        if not phone_number:
            raise ValueError("The Phone Number field is required")
        
        email = self.normalize_email(email)
        extra_fields.setdefault('is_active', True)
        
        user = self.model(email=email, phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, phone_number, password=None, **extra_fields):
        """
        Create and save a superuser with the given email and phone number.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if not extra_fields.get('is_staff'):
            raise ValueError("Superuser must have is_staff=True.")
        if not extra_fields.get('is_superuser'):
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(email=email, phone_number=phone_number, password=password, **extra_fields)

