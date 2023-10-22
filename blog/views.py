from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from pytils.translit import slugify

from blog.models import BlogPost


class BlogPostListView(ListView):
    model = BlogPost
    template_name = 'blog/blog_posts_list.html'
    context_object_name = "posts"
    extra_context = {"title": "Блог"}
    # FBV
    # def blog_post_list(request):
    #     # posts = BlogPost.objects.filter(is_published=True)
    #     posts = BlogPost.objects.all()
    #     return render(request, 'blog/blog_posts_list.html', {'posts': posts})


class BlogPostCreatView(CreateView):
    model = BlogPost
    template_name = 'blog/blog_posts_form.html'
    fields = ('title', 'content')
    success_url = reverse_lazy('blog:blog_list')

    def form_valid(self, form):
        if form.is_valid():
            new_post = form.save()
            new_post.slug = slugify(new_post.title)
            new_post.save()
        return super().form_valid(form)


class BlogPostDetailView(DetailView):
    model = BlogPost
    template_name = 'blog/blog_post_detail.html'
    slug_url_kwarg = 'slug'

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.view_counter += 1
        self.object.save()
        return self.object


class BlogPostUpdateView(UpdateView):
    model = BlogPost
    template_name = 'blog/blog_posts_form.html'
    fields = ('title', 'content')
    success_url = reverse_lazy('blog:blog_list')


class BlogPostDeleteView(DeleteView):
    model = BlogPost
    template_name = 'blog/blog_post_confirm_delete.html'
    success_url = reverse_lazy('blog:blog_list')
