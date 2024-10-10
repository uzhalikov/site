from .utils import get_ip
from .models import PostViews, Post

def post_viewing(func):
    def wrapper(request, *args, **kwargs):
        item = Post.objects.get(slug=kwargs['slug'])
        ip = get_ip(request)
        PostViews.objects.get_or_create(post=item, ip_address=ip)
        kwargs['item'] = item
        return func(request, *args, **kwargs)
    return wrapper

def get_unread_post(func):
    def wrapper(request, *args, **kwargs):
        ip = get_ip(request)
        kwargs['unread'] = Post.objects.filter(is_published=True).count() - PostViews.objects.filter(ip_address=ip).count()
        return func(request, *args, **kwargs)
    return wrapper