from django.db import models

# BlogPost model - database structure
class BlogPost(models.Model):
    title = models.CharField(max_length=101)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
