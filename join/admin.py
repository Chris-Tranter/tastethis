from django.contrib import admin
from .models import Join
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Join)
class JoinAdmin(SummernoteModelAdmin):

    summernote_fields = ('content',)