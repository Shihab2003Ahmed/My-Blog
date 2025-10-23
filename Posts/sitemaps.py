from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Post

class PostSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.9

    def items(self):
        return Post.objects.all()

    def lastmod(self, obj):
        return obj.date  # since you use date = models.DateTimeField(auto_now_add=True)

    def location(self, obj):
        return reverse('post_detail', args=[obj.id])
