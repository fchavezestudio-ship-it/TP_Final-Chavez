from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    subtitle = models.CharField(max_length=300, verbose_name="Subtítulo")
    content = RichTextField(verbose_name="Contenido")
    image = models.ImageField(upload_to='posts/', blank=True, null=True, verbose_name="Imagen")
    created_at = models.DateField(auto_now_add=True, verbose_name="Fecha de creación")
    updated_at = models.DateField(auto_now=True, verbose_name="Última actualización")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Autor")

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    def __str__(self):
        return self.title
