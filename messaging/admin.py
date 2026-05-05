from django.contrib import admin
from .models import Message

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['sender', 'receiver', 'subject', 'sent_at', 'read']
    list_filter = ['read', 'sent_at']
    search_fields = ['subject', 'sender__username', 'receiver__username']
