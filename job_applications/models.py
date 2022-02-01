from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


# admin only
class Sector(models.Model):
    name = models.CharField(max_length=200)


# for users
class CustomSector(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sectors')

    name = models.CharField(max_length=200)


# admin only
class Status(models.Model):
    name = models.CharField(max_length=200)
    colour = models.CharField(max_length=20)


# for users
class CustomStatus(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='statuses')

    name = models.CharField(max_length=200)
    colour = models.CharField(max_length=20)


class Company(models.Model):
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE, related_name='companies')

    name = models.CharField(max_length=200)
    description = models.TextField(null=True)
    image = models.ImageField()


class Application(models.Model):
    searcher = models.ForeignKey(User, on_delete=models.CASCADE, related_name='applications')
    status = models.ForeignKey(Status, on_delete=models.CASCADE, related_name='applications')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='applications')

    link = models.URLField()
    comments = models.TextField(max_length=800)
    position = models.CharField(max_length=200)
    cv = models.FileField()
    motivation_letter = models.FileField()
    city = models.CharField(max_length=100)
    street = models.CharField(max_length=500)
    phone_number = models.CharField(max_length=15)
    email = models.CharField(max_length=150)


class Interchange(models.Model):
    application = models.ForeignKey(
        Application,
        on_delete=models.CASCADE,
        related_name='interchanges'
    )

    date = models.DateTimeField(auto_now=True)
    result = models.TextField(max_length=800)
