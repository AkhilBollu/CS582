from django.db import models
from django.urls import reverse
# Create your models here.
class Vehicles(models.Model):
    make      = models.CharField(max_length=120) # max_length = required
    model = models.TextField(blank=True, null=True)
    price       = models.DecimalField(decimal_places=2, max_digits=10000)
    info     = models.TextField(blank=False, null=False)
    featured    = models.BooleanField(default=False) # null=True, default=True

    def get_absolute_url(self):
        return reverse("vehicles:vehicle-detail", kwargs={"id": self.id}) #f"/vehicles/{self.id}/"