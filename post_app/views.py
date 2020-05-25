from django.shortcuts import render
from .models import Post, SideWidget
from django.views.generic import ListView
from django.db.models import Q
from django.views.generic.detail import DetailView

# Create your views here.
def postview(request):
    return render(request, 'post_app/post.html', {})

class PostListView(ListView):
    model = Post
    template_name = 'post_app/post.html'  # <app>/<model>_<viewtype>.html
    ordering = ['-date_posted']
    paginate_by = 2


    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        context.update({
            'item': Post.objects.all(),
            'side': SideWidget.objects.all(),
        })
        return context

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Post.objects.filter(Q(title__contains=query)|Q(content__contains=query))
        else:
            return Post.objects.all()




class PostDetailView(DetailView):

    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context
