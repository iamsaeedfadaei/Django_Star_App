from django.contrib import admin
from groups.models import Group,GroupMember
from . import models
# Register your models here.

class GroupMemberInLine(admin.TabularInline):
    model = models.GroupMember


admin.site.register(models.Group)
