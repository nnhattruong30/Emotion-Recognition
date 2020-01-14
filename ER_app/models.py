from django.db import models

# Create your models here.
class Image(models.Model):
    image = models.ImageField(upload_to='image/', blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    res_image = models.ImageField(default='out/output.jpg')
    
    def __str__(self):
        return self.image.name
