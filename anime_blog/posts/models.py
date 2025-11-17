from django.db import models
from django.urls import reverse

# Create your models here.

class Post(models.Model):
    title = models.CharField("Título do Anime ou Episódio", max_length=255)
    content = models.TextField("Conteúdo em HTML (Análise, Review ou Curiosidades)")
    posted_at = models.DateTimeField("Data da postagem", auto_now_add=True)

    class Meta:
        ordering = ['-posted_at']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.pk})