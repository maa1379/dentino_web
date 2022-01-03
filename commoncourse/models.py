from ckeditor.fields import RichTextField
from django.db import models


# Create your models here.
class Common_Course(models.Model):
    title = models.CharField(max_length=500)
    image = models.ImageField(upload_to="images/common_course")
    description = models.TextField()
    source = models.CharField(max_length=125)
    video = models.FileField(upload_to="common_course/video", null=True, blank=True)

    def __str__(self):
        return self.title
