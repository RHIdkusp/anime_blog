from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Post


# --------------------------
# LISTAGEM
# --------------------------
class PostListView(ListView):
    model = Post
    template_name = "post_list.html"
    context_object_name = "posts"


# --------------------------
# DETALHE (AUTOMÁTICO: 404)
# --------------------------
class PostDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"
    context_object_name = "post"


# --------------------------
# CRIAÇÃO
# --------------------------
class PostCreateView(CreateView):
    model = Post
    fields = ["title", "content"]
    template_name = "post_form.html"
    success_url = reverse_lazy("post_list")


# --------------------------
# ATUALIZAÇÃO
# --------------------------
class PostUpdateView(UpdateView):
    model = Post
    fields = ["title", "content"]
    template_name = "post_form.html"

    def get_success_url(self):
        return reverse_lazy("post_detail", kwargs={"pk": self.object.pk})


# --------------------------
# REMOÇÃO COM CONFIRMAÇÃO
# --------------------------
class PostDeleteView(DeleteView):
    model = Post
    template_name = "post_confirm_delete.html"
    success_url = reverse_lazy("post_list")