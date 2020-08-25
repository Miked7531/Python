from django.db import models

CLASS_CHOICES = {
    ('science', 'science'),
    ('math', 'math'),
    ('english', 'english'),
}


class djangoClasses(models.Model):
    title = models.CharField(max_length=50, choices=CLASS_CHOICES)
    course_number = models.IntegerField(null=True)
    instructor_name = models.CharField(max_length=50, default="", blank=True, null=False)
    duration = models.FloatField()

    student = models.Manager()

    # def __str__(self):
    # return self.title
