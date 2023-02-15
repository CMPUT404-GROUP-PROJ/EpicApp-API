import uuid

from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import AbstractUser

class Author(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    displayName = models.CharField(unique=True, max_length=36)
    email = models.EmailField(unique=True, max_length=64)
    password = models.CharField(max_length=255)
    host = models.CharField(max_length=255)
    github = models.CharField(unique=True, max_length=255)
    profile_image = models.TextField()

    # remove unused fields inherited from AbstractUser
    username = None
    first_name = None
    last_name = None

    USERNAME_FIELD = 'displayName'


class Post(models.Model):
    @property
    def type(self):
        return 'post'

    class ContentType(models.TextChoices): 
        textMarkdown = 'text/markdown'
        textPlain = 'text/plain'
        # various image types
        appImg = 'application/base64'
        pngImg = 'image/png;base64'
        jpegImg = 'image/jpeg;base64'
    
    class Visibility(models.TextChoices):
        PUBLIC = 'PUBLIC'
        PRIVATE = 'PRIVATE'
 
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=50)
    source = models.CharField(max_length=255)
    origin = models.CharField(max_length=255)
    description = models.TextField(max_length=500, blank=True)
    content = models.TextField()
    contentType = models.CharField(max_length=18, choices=ContentType.choices)
    published = models.DateTimeField(auto_now_add=True)
    visibility = models.CharField(max_length=7, choices=Visibility.choices, default=Visibility.PUBLIC)
    categories = ArrayField(
        models.CharField(max_length=24),
        default=list
    )
    unlisted = models.BooleanField(default=False)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)


class Comment(models.Model):
    @property
    def type(self):
        return 'comment'
    
    class ContentType(models.TextChoices): 
        textMarkdown = 'text/markdown'
        textPlain = 'text/plain'
        # various image types
        appImg = 'application/base64'
        pngImg = 'image/png;base64'
        jpegImg = 'image/jpeg;base64'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    comment = models.TextField(max_length=500)
    published = models.DateField(auto_now_add=True)
    contentType = models.CharField(max_length=18, choices=ContentType.choices)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

# todo:
# class Friend(models.Model):
#     id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
#     friendId = 
#     authorAccepted = models.BooleanField(default=False, null=False)
#     friendAccepted = models.BooleanField(default=False, null=False)

# Todo:
# class Inbox(models.Model):
#     pass
