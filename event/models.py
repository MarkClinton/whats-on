"""
Event model

This model defines the Event, Comments and Categories models. 
"""
from django.db import models
from django.contrib.auth import get_user_model
from cloudinary.models import CloudinaryField

User = get_user_model()

RESPONSE = ((0, "Not Going"), (1, "Going"), (2, "Maybe"))

class Category(models.Model):
    """
    Defines the category model fields

    :param models.Model: Django class to define data models
    """
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
    """
    Defines the Event model fields

    :param models.Model: Django class to define data models
    """
    event_title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="events"
    )
    host = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="event"
    )
    event_image = CloudinaryField('Event Image', default='event_image')
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    # Look to update the location field to something better
    location = models.CharField(max_length=50)
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


class Comment(models.Model):
    """
    Defines the Comment model fields

    :param models.Model: Django class to define data models
    """
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

class EventAttendees(models.Model):
    """
    Defines the EventAttendees model fields

    :param models.Model: Django class to define data models
    """
    event = models.ForeignKey(
        Event, on_delete = models.CASCADE, related_name="attending"
    )
    attendee = models.ForeignKey(
        User, on_delete = models.CASCADE, related_name="attendee"
    )
    rsvp = models.IntegerField(choices=RESPONSE, default=0)
    is_blocked = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        """
        Specify the order of Attendees
        """
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.attendee} is going to {self.event}"
