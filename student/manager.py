from django.contrib.auth.base_user import BaseUserManager
# from django.utils.translation import ugettext_lazy as _

class custommanager(BaseUserManager):

    def create_user(self,email,password,**extra_fields):
        if not email:
            raise ValueError('the email must be set')
        email= self.normalize_email(email)
        user= self.model(email=email,**extra_fields)
        user.set_password(password)
        user.save(self._db)
        return user
    
    def create_superuser(self,email,password,**extra_fields):   
        extra_fields.setdefault('is_staff',False)
        extra_fields.setdefault('is_superuser',True)
        extra_fields.setdefault('is_active',True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('super user must have is stff:true')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('super user must have  is_superuser:true')
        return self.create_user(email,password,**extra_fields)  
        


# learned  how to apply api in our project and How to Disable Browsable API 
# created If the student application is successfully submitted then the student can view the status of the application in the application status page  in the Student and Faculty project.
# created api and crud(create, retrive,update,delete) opertion in student and faculty project
# currently working  Permissions and Authorization in Django(working on)