from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
class Author(models.Model):
    user = models.CharField(max_length=30)

    def __str__(self):
        return "Author Id: "+str(self.pk)

    


class Blog(models.Model):
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=1000)
    author = models.ForeignKey(Author,related_name='blog', on_delete=CASCADE)

    def __str__(self):
        return "blog id: "+str(self.pk)



class Comment(models.Model):
    body = models.CharField(max_length=200)
    blog = models.ForeignKey(Blog,related_name='comment', on_delete=CASCADE)

    def __str__(self):
        return "comment Id: "+str(self.pk)


    



