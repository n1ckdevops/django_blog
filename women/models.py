from django.db import models
from django.urls import reverse


# Create your models here.
class Women(models.Model):
    title = models.CharField(max_length=255, verbose_name="Title")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    content = models.TextField(blank=True, verbose_name="Article text")
    # очень эффективно когда пользователи загружают много фотографий
    photo = models.ImageField(upload_to="photos/%Y/%m/%d", verbose_name="Photo")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Creation time")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Published time")
    is_published = models.BooleanField(default=True, verbose_name="Published")
    cat = models.ForeignKey("Category", on_delete=models.PROTECT,
                            verbose_name="Category")  # запретим удалять категории на которые есть ссылки

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post", kwargs={"post_slug": self.slug})

    class Meta:
        verbose_name = "Popular person"
        verbose_name_plural = "Popular people"
        ordering = ["time_create", "title"]  # сротировка по нескольким полям


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name="Category")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("category", kwargs={"cat_slug": self.slug})

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ["id"]
