from django.db import models



from django.utils import timezone


class Extractore(models.Model):

    name = models.CharField(max_length=200, blank = False)
    bank_name = models.CharField(max_length=200 , blank = False)
    email_id = models.EmailField(max_length=200 , unique = True, blank = False)
    password = models.CharField(max_length=50)

    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name



class StoreData(models.Model):

    username = models.CharField(max_length=200)
    useremailid = models.CharField(max_length=200)
    email_from = models.CharField(max_length=200)
    email_to = models.CharField(max_length=200)
    date = models.DateTimeField(blank=False, null=False)
    subject = models.CharField(max_length=200)
    filename = models.CharField(max_length=200)
    filedata = models.TextField()

    def __str__(self):
        return self.subject
