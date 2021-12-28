import os
import random

from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import Q
from django.db.models.signals import post_save, pre_save
from django.urls import reverse
from django.utils import timezone
from django.utils.html import format_html, html_safe, strip_tags

User = get_user_model()


class BlogTag(models.Model):
    title = models.CharField(max_length=200, unique=True, verbose_name="عنوان برچسب")
    status = models.BooleanField(default=True, verbose_name="فعال/غیرفعال")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="زمان ایجاد")
    update_time = models.DateTimeField(auto_now=True, verbose_name="زمان بروزرسانی")

    class Meta:
        verbose_name = "برچسب"
        verbose_name_plural = "برچسب ها"
        ordering = ["-create_time"]

    def __str__(self):
        return self.title


class Blog(models.Model):
    author = models.ForeignKey(
        User,
        null=True,
        on_delete=models.SET_NULL,
        related_name="blogs",
        verbose_name="نویسنده",
        limit_choices_to="is_superuser",
    )
    title = models.CharField(max_length=300, verbose_name="عنوان مقاله")
    slug = models.CharField(max_length=300, verbose_name="عنوان در url", blank=True)
    description = RichTextField(verbose_name="محتوا")
    image = models.ImageField(upload_to="image/blog", verbose_name="تصویر مقاله")
    tags = models.ManyToManyField(
        BlogTag, related_name="blogs", blank=True, verbose_name="تگ ها / برچسب ها"
    )
    hits = models.ManyToManyField(
        "IpAddress", blank=True, related_name="articles", verbose_name="بازید"
    )
    status = models.BooleanField(default=False, verbose_name="وضعیت انتشار")
    publish_time = models.DateTimeField(
        default=timezone.now, verbose_name="زمان انتشار"
    )
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "مقاله"
        verbose_name_plural = "مقالات"
        ordering = ["-publish_time"]


class IpAddress(models.Model):
    ip_address = models.GenericIPAddressField(verbose_name="آی پی آدرس")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="زمان ثبت")

    class Meta:
        verbose_name = "آی پی آدرس"
        verbose_name_plural = "آی پی آدرس ها"

    def __str__(self):
        return self.ip_address
