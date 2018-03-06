from Gym.celery import app
from .utils import send_activation_email
from .models import Profile
# если перенесу в юзерс то импортить Профиль из юсерс


@app.task
def send_activation_email_task(profile_pk, host):
    profile = Profile.objects.get(pk=profile_pk)
    send_activation_email(profile, host)
