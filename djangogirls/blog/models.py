from django.conf import settings
from django.db import models
from django.utils import timezone

class Post(models.Model):
    #AUTH_USER_MODEL will delay the retrieval of the actual model until all apps are loaded
    #get_user_model would wil attempt to retreieve the model class at the moment the app is imported the first time
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    #CharField() typically used with a maximum length, and can be more effiecent on storage, while TextField() isn't limited by the database scheme but typically by hardcoded implementation limits
    title = models.CharField(max_length=200)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title