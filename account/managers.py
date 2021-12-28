# from django.contrib.auth.models import BaseUserManager
#
#
# class MyUserManager(BaseUserManager):
#     def create_user(
#         self,
#         phone_number,
#         national_code,
#         name,
#         family,
#         birthday,
#         profile_image=None,
#         insurance_scan=None,
#         password=None,
#     ):
#         if not phone_number:
#             raise ValueError()
#         if not name:
#             raise ValueError()
#         if not family:
#             raise ValueError()
#         if not birthday:
#             raise ValueError()
#         if not national_code:
#             raise ValueError()
#         user = self.model(
#             phone_number=phone_number,
#             national_code=national_code,
#             name=name,
#             family=family,
#             birthday=birthday,
#             profile_image=profile_image,
#             insurance_scan=insurance_scan,
#         )
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
#
#     def create_superuser(
#         self, phone_number, national_code, name, family, birthday, password
#     ):
#         user = self.create_user(
#             phone_number, national_code, name, family, birthday, password=password
#         )
#         user.is_admin = True
#         user.save(using=self._db)
#         return user
