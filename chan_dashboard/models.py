from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator


# Create your models here.
class User(models.Model):
    job_in_choices = (
        ('STUDENT' , 'Student'),
        ('STAFF', 'Staff'),
        ('VIP', 'Vip'),
    )
    name = models.CharField(max_length=200,primary_key=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message= "Phone number must be entered in the format: "
                                                                    "'+999999999'. Up to 15 digits allowed.")
    phone = models.PositiveIntegerField()
    job = models.CharField(max_length=10, choices=job_in_choices, default='student',)
    email = models.EmailField()
    note = models.TextField(blank=True)
    facebook = models.CharField(max_length=255)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Category(models.Model):
    typename = models.CharField(max_length=50,db_index=True)
    slug = models.SlugField(max_length=50,unique=True)
    price_normal = models.DecimalField(max_digits=10, decimal_places=0)
    price_student = models.DecimalField(max_digits=10, decimal_places=0)
    price_staff = models.DecimalField(max_digits=10, decimal_places=0)
    price_vip = models.DecimalField(max_digits=10, decimal_places=0)

    class Meta:
        ordering = ["typename"]
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.typename


class BookDate(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    orderDate = models.DateTimeField(default=timezone.now)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    status_choice = (
        ('waiting', 'Waiting'),
        ('completed', 'Completed'),
        ('cancel', 'Cancel'),
    )
    status = models.CharField(max_length=10, choices=status_choice, default='waiting')

    class Meta:
        ordering = ['orderDate']


class Gallery(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pic = models.ImageField(upload_to='users/%y/%m/%d/', blank=True)

    def __str__(self):
        return 'Profile for user {}'.format(self.user)
