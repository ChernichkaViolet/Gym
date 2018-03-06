from django.contrib import admin

from .models import Training, Exercise

class ExerciseAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'description',
        'set_quantity',
        'repeats',
        'created_date'
    ]
#
class TrainingAdmin(admin.ModelAdmin):
    list_display = [
        'tittle',
        'date',
        'time',
        'exercise_id'
    ]


admin.site.register(Exercise,ExerciseAdmin)
admin.site.register(Training,TrainingAdmin)