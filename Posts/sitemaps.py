from django.contrib.sitemaps import Sitemap
from .models import Post

class PostSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.8

    def items(self):
        # Include all posts
        return Post.objects.all()

    def lastmod(self, obj):
        # Use the creation date as last modified
        return obj.date
