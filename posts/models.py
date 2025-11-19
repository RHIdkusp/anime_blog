from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

# Passo 3

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

# Passo 1

class Post(models.Model):
    title = models.CharField("Título do Anime ou Episódio", max_length=255)
    content = models.TextField("Conteúdo em HTML (Análise, Review ou Curiosidades)")
    posted_at = models.DateTimeField("Data da postagem", auto_now_add=True)

    categories = models.ManyToManyField(Category, related_name="posts", blank=True)

    class Meta:
        ordering = ['-posted_at']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.pk})
    
User = get_user_model()

# Passo 2

class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comentário de {self.author} em {self.post}"