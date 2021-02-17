from django.views.generic import ListView
from .models import Post

class DBPageView(ListView):
    model = Post
    template_name = 'db.html'
    context_object_name = 'all_posts_list'



