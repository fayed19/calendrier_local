from django.db import models

# Create your models here.

class Location(models.Model):
    name = models.CharField(max_length=255)
    adress = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    region = models.CharField(max_length=100, blank=True, null=True)
    contry = models.CharField(max_length=100)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} - {self.city}, {self.contry} "




class Organizer(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True, null=True)
    website = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"{self.name}"




class Category(models.Model):
    name = models.CharField(max_length=100)
    color_code = models.CharField(max_length=7, help_text="Couleur hexadecimale (ex : #FF5733)")

    def __str__(self):
        return self.name

class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='events')
    organizer = models.ForeignKey(Organizer, on_delete=models.SET_NULL, null=True, related_name='events')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='events')
    language_code = models.CharField(max_length=15, default='fr')
    is_public = models.BooleanField(default=True)

    def __str__(self):
        return self.title
    

# class EventRegistration(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='registrations')
#     event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='registrations')
#     registered_at = models.DateTimeField(auto_now_add=True)

#     class Meta:
#         unique_together = ('user', 'event')
    
#     def __str__(self):
#         return f"{self.user.username} --> {self.event.title}"
    

"""
| Relation                     | Django Implementation                  |
| ---------------------------- | -------------------------------------- |
| Event → Location             | `ForeignKey(Location, on_delete=...)`  |
| Event → Organizer            | `ForeignKey(Organizer, on_delete=...)` |
| Event → Category             | `ForeignKey(Category, on_delete=...)`  |
| User ↔ Event (Participation) | `EventRegistration` comme table pivot  |
"""