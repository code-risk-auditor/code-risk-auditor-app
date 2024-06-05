import uuid
from django.db import models

class InstalledApps(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    owner = models.ForeignKey('auth.User', related_name='installed_apps', on_delete=models.CASCADE)

    installation_id = models.CharField(max_length=255)
    code = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.installation_id
