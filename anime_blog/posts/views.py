from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required

from .models import Post, Comment
from .forms import CommentForm


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

    # Enviar comentários para o template
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Comentários mais recentes primeiro
        context["comments"] = self.object.comments.order_by("-date_posted")
        return context


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


# ========================================
# ADICIONAR COMENTÁRIOS (PASSO 5)
# ========================================
@login_required
def add_comment(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect("post_detail", pk=post.pk)
    else:
        form = CommentForm()

    return render(request, "post_add_comment.html", {"form": form, "post": post})