from django.db import models

# Create your models here.
class PersonManager(models.Manager):
    pass
class Person(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    connections = models.ForeignKey('self', related_name="connection", on_delete=models.CASCADE, default=None, blank=True, null=True)
    objects = PersonManager()

    @staticmethod
    def printConnections(user):
        for u in user.connection.all():
            print(f"{u.first_name} {u.last_name}")


    @staticmethod
    def findConnectionSpace(user, potCon, count = 0):
        if count == 3:
            return count
        if potCon in user.connection.all():
            return count
        else:
            for u in user.connection.all():
                return Person.findConnectionSpace(u, potCon, count+1)