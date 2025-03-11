from django.db import models
from django.contrib.auth.models import User

class doctor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    license = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
class hospital(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    license = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    def __str__(self):
        return self.name
class patient(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    qr = models.ImageField(upload_to='qr',blank=True,null=True)
    bloodGroup = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    emergencyContact = models.CharField(max_length=100)
    def __str__(self):
        return self.name
class hospitalLedger(models.Model):
    hospital = models.ForeignKey(hospital, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    reason = models.CharField(max_length=100,blank=True,null=True)
    patient = models.ForeignKey(patient,on_delete=models.CASCADE)
    doctor = models.ForeignKey(doctor, on_delete=models.CASCADE)
    isDischarged = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.hospital.name}-{self.patient.name}-{self.id}"
class hospitalDocument(models.Model):
    name = models.CharField(max_length=100,blank=True,null=True)
    added = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    hospitalLedger = models.ForeignKey(hospitalLedger, on_delete=models.CASCADE)
    isPrivate = models.BooleanField(default=True)
    def __str__(self):
        return f"{self.hospitalLedger.hospital.name}-{self.hospitalLedger.patient.name}-{self.id}"
class patientDocument(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    patient = models.ForeignKey(patient, on_delete=models.CASCADE)
    isPrivate = models.BooleanField(default=True)
    added = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    hash = models.CharField(max_length=100,blank=True,null=True)
    def __str__(self):
        return f"{self.patient.name}-{self.id}"
class documentAcess(models.Model):
    doc = models.ForeignKey(hospitalDocument, on_delete=models.CASCADE)
    to = models.ForeignKey(hospital, on_delete=models.CASCADE)
    sanctioned = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.doc.hospitalLedger.hospital.name}-{self.doc.hospitalLedger}"
class HospitalDoctors(models.Model):
    hospital = models.ForeignKey(hospital, on_delete=models.CASCADE,blank=True,null=True)
    doctor = models.ForeignKey(doctor, on_delete=models.CASCADE,blank=True,null=True)
    def __str__(self):
        return f"{self.hospital.name}-{self.doctor.name}"
    

from . import signals  # This ensures signals are loaded when models are imported
