from django.db import models

# Create your models here.

class Post(models.Model):
   # id = models.IntegerField()
    name = models.CharField(max_length=100, blank=False)
    author = models.CharField(max_length=50, blank=False)
    content = models.CharField(max_length=5000, blank=False)
    link = models.CharField(max_length=200, blank=True)
    date = models.DateTimeField()
    rating = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Comment(models.Model):
    post_id = models.IntegerField()
    user = models.CharField(max_length = 50, blank=False)
    content = models.CharField(max_length=5000, blank=False)
    date = models.DateTimeField()

    def __str__(self):
        return f'{self.post_id}'


def view_post(request, slug):
    try:
        post = Post.objects.get(slug=slug)
    except Post.DoesNotExist:
        raise Http404("Poll does not exist")

    post.view_count += 1
    post.save()
    return render(request, 'post.html', context={'post': post})
