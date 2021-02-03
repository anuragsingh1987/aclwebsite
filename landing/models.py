from django.db import models
# from django.utils.text import slugify
# from slug_preview import models as slugmodel
# Create your models here.

class Course(models.Model):
    # author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    course_id = models.CharField(max_length=6,unique=True)
    course_name = models.CharField(max_length=200)
    course_description = models.CharField(max_length=500)
    course_learnings = models.CharField(max_length=500)
    topics_covered = models.CharField(max_length=500)
    course_prerequisites = models.CharField(max_length=500)
    course_prep_required = models.CharField(max_length=500)
    course_pdu = models.CharField(max_length=500)
    course_seu = models.CharField(max_length=500)
    course_logo = models.ImageField(blank=True,upload_to='logo')

    def __str__(self):
        return '%s' % ( self.course_name)


class Event(models.Model):
    # author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    course_id = models.ForeignKey(Course,on_delete=models.CASCADE)
    event_name = models.CharField(max_length=200,default="test")
    event_id = models.CharField(max_length=6,unique=True)
    event_date_time = models.DateTimeField()

    classroom = 'CL'
    online = 'OL'
    CATEGORY_CHOICES = [(classroom , 'Classroom'),(online, 'Online'),]

    event_format = models.CharField(max_length=2,choices=CATEGORY_CHOICES)
    event_who_will_benefit = models.CharField(max_length=500)
    event_what_will_you_learn = models.CharField(max_length=500)
    event_What_you_will_get = models.CharField(max_length=500)
    event_refund_policy = models.CharField(max_length=500)
    event_slug = models.SlugField(max_length=40,default="test")


    def __str__(self):
        return '%s' % ( self.event_name)

class Registration(models.Model):
    event_id = models.ForeignKey(Event,on_delete=models.CASCADE)
    registration_fname = models.CharField(max_length=100,default="test")
    registration_lname = models.CharField(max_length=100,default="test")
    registration_email = models.EmailField(max_length=200,default="test")
    registration_contact_number = models.CharField(max_length=20)
    registration_unique_id = models.CharField(max_length=15)
    registration_coupon_code = models.CharField(max_length=200)
    registration_paid_status = models.BooleanField()
    registration_paid_amount = models.CharField(max_length=200)

    def __str__(self):
        return '%s' % ( self.registration_unique_id)
