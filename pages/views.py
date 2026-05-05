from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Post
from .forms import PostForm


def home(request):
    recent_posts = Post.objects.all()[:3]
    return render(request, 'home.html', {'recent_posts': recent_posts})


def about(request):
    return render(request, 'about.html')


def post_list(request):
    query = request.GET.get('q', '')
    posts = Post.objects.all()
    if query:
        posts = posts.filter(title__icontains=query) | posts.filter(subtitle__icontains=query)
    return render(request, 'pages/post_list.html', {'posts': posts, 'query': query})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'pages/post_detail.html', {'post': post})


@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, '¡Post creado exitosamente!')
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'pages/post_form.html', {'form': form, 'action': 'Crear'})


@login_required
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()
        messages.success(request, 'Post eliminado.')
        return redirect('post_list')
    return render(request, 'pages/post_confirm_delete.html', {'post': post})


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'pages/post_form.html'

    def get_success_url(self):
        messages.success(self.request, '¡Post actualizado exitosamente!')
        return reverse_lazy('post_detail', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['action'] = 'Editar'
        return ctx


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'pages/post_confirm_delete.html'
    success_url = reverse_lazy('post_list')

    def form_valid(self, form):
        messages.success(self.request, 'Post eliminado.')
        return super().form_valid(form)
