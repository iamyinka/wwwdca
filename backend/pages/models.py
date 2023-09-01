import uuid
from django.db import models
from django.urls import reverse
from django.utils import timezone

class Course(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, unique=True, default=uuid.uuid4)
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title.title()

    def get_absolute_url(self):
        return reverse("course_detail", kwargs={"slug": self.slug})
    

class FreeTaster(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, unique=True, default=uuid.uuid4)
    full_name = models.CharField(max_length=100, verbose_name="Full Name")
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=20)
    course = models.ForeignKey(Course, on_delete=models.DO_NOTHING)
    applied_on = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.full_name} - {self.course}"
    
    class Meta:
        verbose_name_plural = "Free Taster Sign Ups"
        ordering = ('-applied_on',)