from django.contrib import admin
from ghosts.models import GhostName, GhostUser

# Register your models here.
admin.site.register(GhostName)
admin.site.register(GhostUser)
