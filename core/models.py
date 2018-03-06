import os
import binascii

from django.contrib.auth.models import User, UserManager, AbstractUser
from django.db import models
from django.utils.timezone import now
from django.utils.translation import ugettext as _
from solo.models import SingletonModel
from django.db.models.signals import post_save

NULL_BLANK = {
    'null': True,
    'blank': True
}
NULL = {
    'null': True,
    'blank': False
}


def get_profile_image_path(instance, filename):
    return '{username}/{filename}'.format(
        username=instance.user.username,
        filename=filename
    )


class TimeStampable(models.Model):
    date_created = models.DateTimeField(
        default=now
    )
    date_updated = models.DateTimeField(
        auto_now=True,
        **NULL_BLANK
    )

    class Meta:
        abstract = True


class SiteSettings(SingletonModel):
    activation_url_preiod = models.SmallIntegerField(
        verbose_name=_('Срок действия ссылки на активацию, ч.'),
        default=100
    )
    default_user_image = models.ImageField(
        verbose_name=_('Аватар пользователя по умолчанию'),
        **NULL_BLANK
    )

    class Meta:
        verbose_name = _('Настройки сайта')


class Activation(models.Model):
    valid_until = models.DateTimeField(
        verbose_name=_('Дата окончания действия ссылки активации'),
    )
    url = models.URLField(
        verbose_name=_('Ссылка'),
    )

    def set_url(self):
        self.url = 'activate/{token}/'.format(
            token=binascii.hexlify(os.urandom(10)).decode('utf-8')
        )
        pass

#
# class Profile(User):
#     avatar = models.ImageField(
#         verbose_name=_('Аватар'),
#         upload_to=get_profile_image_path,
#         **NULL_BLANK
#     )
#     activation = models.OneToOneField(
#         verbose_name=_('Активация'),
#         to=Activation,
#         on_delete=models.SET_NULL,
#         **NULL_BLANK
#     )


class Profile(User):

    timezone = models.CharField(max_length=50, default='Europe/Minsk')
    birth_date = models.DateField(verbose_name=_('День Рождения'),null=True, blank=True)
    purpose = models.TextField(verbose_name=_('Цель на ближайшие 3 месяца'),max_length=500, blank=True)

    avatar = models.ImageField(
        verbose_name=_('Аватар'),
        upload_to=get_profile_image_path,
        **NULL_BLANK
    )
    activation = models.OneToOneField(
        verbose_name=_('Активация'),
        to=Activation,
        on_delete=models.SET_NULL,
        **NULL_BLANK
    )

    objects = UserManager()

    def create_custom_user(sender, instance, created, **kwargs):
        if created:
            values = {}
            for field in sender._meta.local_fields:
                values[field.attname] = getattr(instance, field.attname)
            user = Profile(**values)
            user.save()

    post_save.connect(create_custom_user, User)

