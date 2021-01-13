from django.db import models
from django.conf import settings
from django.utils import timezone

# define the model/object.
# Post is a Django Model, which is saved in the db
class Post(models.Model):
    # models.ForeignKey: link to another model
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    # define the publish function/method inside the class
    def publish(self):
        self.published_date = timezone.now()
        self.save()
    
    def __str__(self):
        return self.title
