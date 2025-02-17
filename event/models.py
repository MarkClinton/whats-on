from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Category(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        """
        Specify the order of categories
        """
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name}"

class Event(models.Model):
    event_title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="events"
    )
    host = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="event"
    )
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    location = models.CharField(max_length=50) #change soon
    enable_comments = models.BooleanField(default=True)
    limit = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        """
        Specify the order of events
        """
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.event_title} | created by {self.host}"


class Comments(models.Model):
    commenter = models.ForeignKey(
        User, on_delete = models.CASCADE, related_name="commenter"
    )
    event = models.ForeignKey(
        Event, on_delete = models.CASCADE, related_name="comments"
    )
    body = models.TextField()
    is_host = models.BooleanField(default=False)
    is_removed = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    is_pinned = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        """
        Specify the order of comments
        """
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.body} by {self.commenter}"
