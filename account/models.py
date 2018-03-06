# from django.contrib.auth.models import User, UserManager

# from django.db.models.signals import post_save



# class CustomUser(User):
#     """User with app settings."""
#     timezone = models.CharField(max_length=50, default='Europe/London')
#
#     # Use UserManager to get the create_user method, etc.
#     objects = UserManager()

#
# def create_custom_user(sender, instance, created, **kwargs):
#     if created:
#         values = {}
#         for field in sender._meta.local_fields:
#             values[field.attname] = getattr(instance, field.attname)
#         user = CustomUser(**values)
#         user.save()
#
# post_save.connect(create_custom_user, User)