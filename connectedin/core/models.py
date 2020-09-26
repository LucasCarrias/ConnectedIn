from django.db import models
from django.contrib.auth.models import User


class UserAccount(User):
    birth_date = models.DateField(blank=True, null=True)


class Profile(models.Model):
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE, related_name='profiles')
    contacts = models.ManyToManyField('self', blank=True)
    name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


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
    status = models.CharField(choices=STATUS_CHOICES, default='accepted')

    class Meta:
        ordering = ('-created')

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
