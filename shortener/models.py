from django.db import models

class ShortenURL(models.Model):
    original_url = models.URLField(max_length=2000)
    short_url = models.CharField(max_length=10, unique=True, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    usage_count = models.IntegerField(default=0)
    
    def __str__(self):
        return f"{self.short_url} -> {self.original_url}"
    