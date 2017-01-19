from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords
from .templatetags.blog_tags import markdown_format
from .models import Post


class LatestPostsFeed(Feed):
    title = 'My Blog'
    link = '/blog/'
    description = 'New post of my blog'

    def items(self):
        return Post.published.all()[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return markdown_format(truncatewords(item.body, 30))