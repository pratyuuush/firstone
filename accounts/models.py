from django.db import models
from django.core.validators import MaxValueValidator
from imagekit.models import ProcessedImageField
from django.contrib.auth.models import User
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField
from django_countries.fields import CountryField
from django.utils import timezone
from datetime import datetime
from django.urls import reverse


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)                            
    image = ProcessedImageField(upload_to='profile_pics',
                                      format='JPEG',
                                      options={'quality': 100},
                                      null=True,
                                      blank=True, default='default.jpg')

    bio = models.CharField(max_length=200, null=True, blank=False, default = " ")
    AC_TYPE = (
        ('Individual', 'Individual'),
        ('Organization', 'Organization'),
    )


    email = models.EmailField(max_length=70)
    ac_type = models.CharField(max_length=12, choices=AC_TYPE, default=" ")

    address1 = models.CharField(
        "Address line 1",
        max_length=1024,
        blank=False,
        default=" "
    )

    address2 = models.CharField(
        "Address line 2",
        max_length=1024,
        blank=False, 
        default=" "
    )

    zip_code = models.CharField(
        "ZIP / Postal code",
        max_length=10,
        blank=False, 
        default=" "
    )

    city = models.CharField(
        max_length=1024,
        blank=False, 
        default=" "
    )
    state = models.CharField(
        max_length=1024,
        blank=False, 
        default=" "
    )
    country = CountryField(
        blank_label='Select Country')

    phone = PhoneNumberField(blank=False,null=True)
    
    @property
    def followers(self):
        return Follow.objects.filter(follow_user=self.user).count()

    @property
    def following(self):
        return Follow.objects.filter(user=self.user).count()

    def __str__(self):
        return self.user.username
    
        

class Post(models.Model):
    author = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE,null=True, blank=True)
    post_something = models.TextField(max_length=1000, null=True, blank=False)
    posted_on = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(default=timezone.now)
    

    POST_TYPE = (
        ('Job Post', 'Job'),
        ('Blog Post', 'Blog'),
    )
    post_type = models.CharField(max_length=9, choices=POST_TYPE, default=" ")


    def __str__(self):
        return self.post_something

class Follow(models.Model):
    user = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE)
    follow_user = models.ForeignKey(User, related_name='follow_user', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

class Rating(models.Model):
    author = models.ForeignKey(UserProfile, related_name='user_rated',
    on_delete=models.CASCADE, null=True, blank=True)
    reciever = models.ForeignKey(User, related_name='user_recieved',
    on_delete=models.CASCADE, null=True, blank=True)
    comment = models.TextField(max_length=600, null=True, blank=False)
    date_posted = models.DateTimeField(default=timezone.now)
    RATE_TYPE = (
        ('5 Star', '5 Star'),
        ('4 Star', '4 Star'),
        ('3 Star', '3 Star'),
        ('2 Star', '2 Star'),
        ('1 Star', '1 Star'),
    )
    rate_type = models.CharField(max_length=7, choices=RATE_TYPE, default=" ")


class Comment(models.Model):
    post_connected = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.CharField(max_length=100)
    posted_on = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.comment

    def save(self, **kwargs):
        super().save()    




