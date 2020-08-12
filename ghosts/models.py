from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth import get_user_model


class CustomTimeStampModel(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        abstract = True


class GhostName(CustomTimeStampModel):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=1000, blank=True)


class GhostUser(CustomTimeStampModel):
    user = models.OneToOneField(get_user_model(), on_delete=CASCADE)
    ghost_name = models.OneToOneField(GhostName, on_delete=CASCADE, null=True)

    def __str__(self):
        return "%s %s" % (self.user.first_name, self.user.last_name)
