from django.shortcuts import render, get_object_or_404, redirect
from .models import Post

# Create your views here.

# ---------------------------
# LISTAGEM
# ---------------------------
def post_list(request):
    posts = Post.objects.all()
    return render(request, "post_list.html", {"posts": posts})


# ---------------------------
# DETALHES (COM 404)
# ---------------------------
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, "post_detail.html", {"post": post})


# ---------------------------
# CRIAÇÃO DE POST (SEM FORM)
# ---------------------------
def post_create(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")

        Post.objects.create(
            title=title,
            content=content,
        )

        return redirect("post_list")

    return render(request, "post_form.html", {"post": None, "form": None})


# ---------------------------
# ATUALIZAÇÃO DE POST (SEM FORM)
# ---------------------------
def post_update(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == "POST":
        post.title = request.POST.get("title")
        post.content = request.POST.get("content")
        post.save()

        return redirect("post_detail", pk=post.pk)

    return render(request, "post_form.html", {"post": post, "form": None})


# ---------------------------
# REMOÇÃO (COM PÁGINA DE CONFIRMAÇÃO)
# ---------------------------
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == "POST":
        post.delete()
        return redirect("post_list")

    return render(request, "post_confirm_delete.html", {"post": post})