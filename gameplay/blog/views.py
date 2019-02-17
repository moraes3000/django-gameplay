from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import ListView,CreateView, DeleteView, UpdateView




from .models import Post

#
# def post_list(request):
#     posts = Post.objects.all().order_by('published_date')
#     return render(request, 'blog/post_list.html', {'posts': posts})
#



class PostListView(ListView):
    model = Post
    template_name = 'blog/blog-post_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = Post.objects.all()
        return context


# admin
class PostCreateView(CreateView):
    model = Post
    fields = ('nome','sumario','descricao', 'imagem', )
    # template_name = 'game/jogo_novo.html'

class AdminPostView(ListView):
    model = Post
    template_name = "blog/admin-post_list.html"
    paginate_by = 3


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = Post.objects.all().order_by('-criado')
        return context

class AdminPostUpdate(UpdateView):
    model = Post
    fields = ('nome','sumario','descricao', 'imagem', )
    success_url = reverse_lazy('admin-post')


class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('admin-post')



def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})