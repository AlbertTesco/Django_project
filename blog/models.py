from django.db import models

NULLABLE = {
    'blank': True,
    'null': True,
}


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class BlogPost(TimeStampedModel):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    preview = models.ImageField(upload_to="blog/", *NULLABLE)
    is_published = models.BooleanField(default=False)
    view_counter = models.IntegerField(default=0)

    class Meta:
        verbose_name = "Публикация"
        verbose_name_plural = "Публикации"

    def __str__(self):
        return self.title
