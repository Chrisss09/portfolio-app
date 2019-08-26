from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=255)
    created_on = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]

    def created_on_pretty(self):
        return self.created_on.strftime('%b %e %Y')