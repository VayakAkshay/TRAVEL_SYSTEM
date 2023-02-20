from django.db import models
import datetime

class MasterPackages(models.Model):
    package_id = models.AutoField
    image = models.ImageField(upload_to="images",default="")
    main_image = models.ImageField(upload_to='main_images',default="")
    package_name = models.TextField(max_length=100,default="")
    package_detail = models.TextField(max_length=100,default="")
    package_date = models.DateField(default=datetime.date.today)
    package_price = models.IntegerField(default=0)
    package_desc = models.TextField(max_length=5000,default="")
    package_duration = models.TextField(max_length=100,default="")
    package_difficulty = models.TextField(max_length=100,default="")
    package_agegroup = models.TextField(max_length=100,default="")
    max_altitude = models.TextField(max_length=100,default="")
    package_event = models.TextField(max_length=100,default="")

class contactform(models.Model):
    contact_id = models.AutoField
    email_id = models.EmailField(max_length=100,default="")
    message = models.TextField(max_length=500,default="")

    def __str__(self):
        return self.email_id
    
class CustomerData(models.Model):
    customer_id = models.IntegerField(default=0)
    customer_fname = models.TextField(max_length=100,default="",blank=True, null=True) 
    customer_lname = models.TextField(max_length=100,default="",blank=True, null=True)
    customer_address = models.TextField(max_length=100,default="")
    customer_mobile = models.TextField(max_length=100,default="")
    customer_email = models.TextField(max_length=100,default="")
    customer_gender = models.TextField(max_length=100,default="")
    customer_dob = models.DateField(default=datetime.date.today)
    customer_img = models.ImageField(upload_to="myprofile")
    customer_package_id = models.TextField(max_length=100,default="")

    def __str__(self):
        return str(self.customer_id)

class Review(models.Model):
    review_id = models.AutoField
    customer_id = models.IntegerField(default=0)
    event_id = models.IntegerField(default=0)
    stars = models.IntegerField(default=0)
    reviewer_name = models.TextField(max_length=200,default="")
    review_text = models.TextField(max_length=1000,default="")

    def __str__(self):
        return str(self.customer_id) + " - " + str(self.stars)
    
class Booked_package(models.Model):
    package_id = models.IntegerField(default=0)
    customer_id = models.IntegerField(default=0)
    payment_id = models.IntegerField(default=0)

    def __str__(self):
        return str(self.customer_id)
    
