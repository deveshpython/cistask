from django.utils import timezone
from django.db.models import Count
from .models import Task, CustomUser
from datetime import timedelta

def auto_deactivate_users():
    one_week_ago = timezone.now() - timedelta(days=7)
    for user in CustomUser.objects.filter(role='user', is_active=True):
        missed = Task.objects.filter(assigned_to=user, deadline__lt=timezone.now(), status='pending', created_at__gte=one_week_ago).count()
        if missed >= 5:
            user.is_active = False
            user.save()
