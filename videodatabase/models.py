from django.db import models
from jsonfield import JSONField


class UploadedVideo(models.Model):
    name = models.CharField(max_length=200, default="")


class EditedVideo(models.Model):
    url = models.FileField(upload_to='video', default="")
    name = models.CharField(max_length=200)
    jumpArg = models.IntegerField(default=0)
    speedArg = models.IntegerField(default=0)
    positionArg = models.IntegerField(default=0)
    cramArg = models.IntegerField(default=0)
    colorArg = models.IntegerField(default=0)


class ShotElement(models.Model):
    editedVideo = models.ForeignKey(EditedVideo, on_delete=models.CASCADE)
    start = models.FloatField(default=0)
    end = models.FloatField(default=0)
    during = models.FloatField(default=0)
    speed = JSONField()
    position = JSONField()
    craMotion = JSONField()
    color = JSONField()
    shotSize = JSONField()

    def __str__(self):
        return "%f, %f, %f, %s, %s, %s, %s, %s" % (self.start, self.end, self.during, self.speed, self.position,
                                                   self.craMotion, self.color, self.shotSize)
