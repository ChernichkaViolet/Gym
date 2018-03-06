from django.db import models
from django.utils import timezone


NULL_BLANK = {
    'null': True,
    'blank': True
}
NULL = {
    'null': True,
    'blank': False
}


class Exercise(models.Model):
    created_date = models.DateTimeField(
        default=timezone.now)
    description = models.CharField(
        max_length=100,
        default='Squat',
        **NULL_BLANK,
    ) #like тяга к поясу

    set_quantity = models.IntegerField(default=3)
    repeats = models.IntegerField(default=12)


    def workout(self):
        self.date = timezone.now()
        self.save()


    def __str__(self):
        return self.description


class Training(models.Model):
    tittle = models.CharField(
        max_length=50,
        default='Title',
        **NULL_BLANK,
    ) #like leg day

    date = models.DateField(default=timezone.now)
    time = models.TimeField(default=timezone.now)

    exercise = models.ForeignKey(
        Exercise,
        related_name='set',
        on_delete=models.CASCADE,
        **NULL_BLANK,
    )


    def workout(self):
        self.date = timezone.now()
        self.save()


    def __str__(self):
        return self.tittle

