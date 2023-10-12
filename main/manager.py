from django.contrib.auth.base_user import BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self,role,password=None,**extra_fields):
        if not role:
            raise ValueError("User must have a role")
        user = self.model(role=role,**extra_fields)
        user.set_password(password)
        user.save(using=self.db)
        return user
    
    def create_superuser(self ,role,password=None,**extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        extra_fields.setdefault('is_active',True)

        return self.create_user(role,password,**extra_fields)