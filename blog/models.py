from django.db import models


# Create your models here.


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(TimeStampedModel):
    name = models.CharField(max_length=212)

    def __str__(self):
        return self.name


class Tag(TimeStampedModel):
    name = models.CharField(max_length=212)

    def __str__(self):
        return self.name


class Author(TimeStampedModel):
    name = models.CharField(max_length=212)
    image = models.ImageField(upload_to='images/')
    profession = models.CharField(max_length=212)
    description = models.TextField()

    def __str__(self):
        return self.name


class Post(TimeStampedModel):
    title = models.CharField(max_length=212)
    content = models.TextField()
    image = models.ImageField(upload_to='images/')
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    categories = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="categories")

    def __str__(self):
        return self.title
