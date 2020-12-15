from django.db import models
import re

class UserManager(models.Manager):
    def user_validator(self, post_data):
        errors = {}
        if len(post_data["first_name"]) < 3:
            errors["first_name"] = "Please enter a longer first name"
        if len(post_data["last_name"]) < 3:
            errors["last_name"] = "Please enter a longer last name"
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(post_data['email']):
            errors['email'] = "Invalid email address!"
        if len(post_data["password"]) < 6:
            errors["password"] = "Please enter a longer password"
        if post_data["password"].isalpha():
            errors["special_character"] = "Please enter a password with a special character"
        if post_data["password"] != post_data["confirm"]:
            errors["confirm"] = "Your passwords don't match"
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

