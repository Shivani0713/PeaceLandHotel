from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import BookRoom

@receiver(post_save, sender=BookRoom)
def update_booked_rooms(sender, instance, created, **kwargs):
    if created:  # Only update BookedRooms if a new booking is created
        room = instance.room
        room.BookedRooms += 1
        room.save()
