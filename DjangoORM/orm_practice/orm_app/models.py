from django.db import models
import re
# Create your models here.
class UserManager(models.Manager):
    def user_validator(self, post_data):
        errors = {}
        if len(post_data["first_name"]) < 2:
            errors["first_name"] = "Please enter a longer first name"
        if len(post_data["last_name"]) < 2:
            errors["last_name"] = "Please enter a longer last name"
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(post_data['email']):   
            errors['email'] = "Invalid email address!"
        if post_data["password"] != post_data["confirm"]:
            errors["confirm_pass"] = "The passwords do not match"
        if len(post_data["password"]) < 3:
            errors["pass_len"] = "Your password's length must be greater"
        if post_data["password"].isalpha():
            errors["special_characters"] = "You password must contain at least one special character"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    confirm = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class Pets(models.Model):
    name = models.CharField(max_length=45)
    age = models.IntegerField()
    user = models.ForeignKey(User, related_name="pets", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Groomers(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    pets = models.ManyToManyField(Pets, related_name="groomers")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)