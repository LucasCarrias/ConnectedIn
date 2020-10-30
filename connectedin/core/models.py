from django.db import models
from django.utils.text import slugify
from django.shortcuts import reverse
from user_account.models import UserAccount


class Profile(models.Model):
    user = models.ForeignKey(UserAccount,
                             on_delete=models.CASCADE,
                             related_name='profiles')
    contacts = models.ManyToManyField('self', blank=True)
    name = models.CharField(max_length=100, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    slug = models.CharField(max_length=255, blank=False)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("core:profile", kwargs={"profile_slug": self.slug})



class Invitation(models.Model):
    STATUS_CHOICES = [
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
        ('waiting', 'Waiting'),
    ]

    user_from = models.ForeignKey(Profile,
                                  related_name='invite_from',
                                  on_delete=models.CASCADE)
    user_to = models.ForeignKey(Profile,
                                related_name='invite_to',
                                on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICES,
                              default='waiting')

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return f"Invitation of '{self.user_from.name}'' to '{self.user_to.name}''"

class Post(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="posts")
    body = models.TextField(null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.profile.name}'s post from {self.created}"


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.profile.name}'s comment in {self.post.profile.name}'s post"


class Reaction(models.Model):
    name = models.CharField(max_length=10)
    weigth = models.SmallIntegerField()

    def __str__(self):
        return self.name

class PostReaction(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    reaction = models.ForeignKey(Reaction, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.profile.name}'s reaction in {self.post.profile.name}'s post"
