from django.db import models

# Create your models here.
class Department(models.Model):
    dept_name=models.CharField(max_length=100)
    dept_description=models.TextField()
    def __str__(self):
        return self.dept_name
class Doctor(models.Model):
    doc_name=models.CharField(max_length=100)
    doc_specialisation=models.CharField(max_length=200)
    dept_name=models.ForeignKey(Department,on_delete=models.CASCADE)
    doc_image=models.ImageField(upload_to='doctors')
    def __str__(self):
        return self.doc_name
class Booking(models.Model):
    p_name=models.CharField(max_length=100)
    p_phone=models.CharField(max_length=20)
    p_email=models.EmailField()
    doc_name=models.ForeignKey(Doctor,on_delete=models.CASCADE)
    booking_date=models.DateField()
    booked_on=models.DateField(auto_now=True)