from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    add_comment,
    category_list,
    category_detail,
)

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('novo/', PostCreateView.as_view(), name='post_create'),
    path('<int:pk>/editar/', PostUpdateView.as_view(), name='post_update'),
    path('<int:pk>/remover/', PostDeleteView.as_view(), name='post_delete'),

    # Comentário
    path('post/<int:pk>/comment/', add_comment, name='add_comment'),

    # Categorias
    path("categories/", category_list, name="category_list"),
    path("category/<int:pk>/", category_detail, name="category_detail"),
]