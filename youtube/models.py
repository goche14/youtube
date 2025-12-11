from django.db import models

class Channel(models.Model):
    youtube_id = models.TextField(max_length=200,unique=True)
    name = models.TextField(max_length=200,blank=False)
    
    def __str__(self):
        return self.name
    
class Video(models.Model):
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE)
    title = models.TextField(max_length=200,blank=False)
    subscribers = models.PositiveSmallIntegerField(default=0)
    views = models.PositiveIntegerField(default=0)
    duration = models.TimeField()

    def __str__(self):
        return self.channel

class Playlist(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    release_year = models.IntegerField()
    likes = models.PositiveIntegerField(default=0)
    dislike = models.PositiveIntegerField(default=0)

    def __str__(self):
        return str(self.release_year)