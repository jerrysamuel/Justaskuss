from django.db import models
from PIL import Image
from io import BytesIO
from django.core.files import File

class Company(models.Model):
    company_name = models.CharField(max_length=45)
    company_details= models.TextField(max_length= 255)


    class Meta:
        ordering= ('company_name',)

    def __str__(self):
        return self.company_name

class Product(models.Model):
    phone_company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    release_date = models.CharField(max_length=100)
    price = models.CharField(max_length=30)
    front_camera= models.CharField(max_length=100, blank=True)
    rear_camera= models.CharField(max_length=100, blank=True)
    processor= models.CharField(max_length=100, blank=True)
    battery_capacity=models.CharField(max_length=25, blank=True)
    sensors=models.CharField(max_length=255, blank=True)
    speakers=models.CharField(max_length=255, blank=True)
    Screen_resolution= models.CharField(max_length=115, blank=True)
    charging=models.CharField(max_length=200, blank=True)
    fingerprint=models.CharField(max_length=60, blank=True)
    platform= models.CharField(max_length=40, blank=True)
    memory= models.CharField(max_length=255, blank=True)
    video= models.CharField(max_length=255, blank=True)
    slots= models.CharField(max_length=255, blank=True)
    phone_image = models.ImageField(upload_to="uploads/", blank=True, null=True)
    thumbnail = models.ImageField(upload_to="uploads/", blank=True, null=True)
    

    class Meta:
        ordering= ('name',)

    def __str__(self):
        return self.name

    def get_thumbnail(self):
        if self.thumbnail:
            return self.thumbnail.url
        else:
            if self.phone_image:
                self.thumnail = self.make_thumbnail(self.phone_image)
                self.save()

                return self.thumbnail.url
            else:
                return 'https://via.placeholder.com/240x240x.jpg'

    def make_thumbnail(self, image, size=(300, 300)):
        img = Image.open(phone_image)
        img.convert('RGB')
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=85)

        thumbnail = file(thumb_io, name=phone_image.name)

        return thumbnail






