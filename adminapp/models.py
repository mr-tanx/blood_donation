from django.db import models

class donor(models.Model):
    full_name = models.CharField(max_length=100,unique=True)
    email = models.CharField(max_length=100, default='')
    blood_group = models.CharField(max_length=100, default='')
    gender = models.CharField(max_length=100, default='')
    address = models.CharField(max_length=100, default='')
    age = models.AutoField(primary_key=True)

    class Meta:
        db_table = "donor_table"

class recipient(models.Model):
    FULL_NAME = models.CharField(max_length=100, blank=False, unique=True, default='')
    EMAIL = models.CharField(max_length=100, default='')
    BLOOD_GROUP = models.CharField(max_length=100, default='')
    urgency_level = models.CharField(max_length=100, default='')
    hospital_name = models.CharField(max_length=100, default='')
    hospital_address = models.CharField(max_length=100, default='')

    class Meta:
        db_table = "recipient_table"
