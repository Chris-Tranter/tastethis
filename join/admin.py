from django.contrib import admin
from .models import Join, JoinRequest
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Join)
class JoinAdmin(SummernoteModelAdmin):

    summernote_fields = ('content',)


@admin.register(JoinRequest)
class JoinRequestAdmin(admin.ModelAdmin):

    list_display = ('message', 'read',)