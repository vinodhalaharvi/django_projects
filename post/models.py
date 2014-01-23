from django.db import models

class Post(models.Model):
    post = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    rating = models.IntegerField()
    username = models.CharField(max_length=50)

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

    def __unicode__(self):
        return self.post


class Comment(models.Model):
    post = models.ForeignKey(Post)
    comment = models.CharField(max_length=200)
    username = models.CharField(max_length=50)
    rating = models.IntegerField()

    def __unicode__(self):
        return self.comment

