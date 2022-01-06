from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from account.models import User
import re


@receiver(pre_save, sender=User)
def user_pre_save_email_field(sender, instance, **kwargs):
    print('user_pre_save')
    if instance.email:
        instance.email = instance.email.lower()


@receiver(pre_save, sender=User)
def user_pre_save_phone_field(sender, instance, **kwargs):
    if instance.phone:
        # instance.phone = re.sub(r'[a-z]', '', instance.phone)
        instance.phone = re.sub('\D', '', instance.phone)


@receiver(post_save, sender=User)
def user_post_save(sender, instance, **kwargs):
    print('post_save')
