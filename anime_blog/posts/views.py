from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm

# Create your views here.

# LISTAGEM
def post_list(request):
    posts = Post.objects.all()
    return render(request, "post_list.html", {"posts": posts})


# DETALHES (COM 404)
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, "post_detail.html", {"post": post})


# CRIAÇÃO COM FORM
def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("post_list")

    else:
        form = PostForm()

    return render(request, "post_form.html", {"form": form, "post": None})


# ATUALIZAÇÃO COM FORM
def post_update(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == "POST":
        form = PostForm(request.POST, instance=post)

        if form.is_valid():
            form.save()
            return redirect("post_detail", pk=pk)

    else:
        form = PostForm(instance=post)

    return render(request, "post_form.html", {"form": form, "post": post})


# REMOÇÃO (COM CONFIRMAÇÃO)
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == "POST":
        post.delete()
        return redirect("post_list")

    return render(request, "post_confirm_delete.html", {"post": post})