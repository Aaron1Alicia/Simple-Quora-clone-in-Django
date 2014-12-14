from django.db import models
from django.contrib.auth.models import User
import datetime


from django.utils import timezone

# Create your models here.
# Create QuestionAuthor module
# class QuestionAuthor(models.Model):
#     author =


class Question(models.Model):
    question_text = models.CharField(max_length=1000)
    pub_date = models.DateTimeField('date published')
    modification_time = models.DateTimeField('date modified')

    def __unicode__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    author = models.ForeignKey(User, null=True)
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


class Answers(models.Model):
    question = models.ForeignKey(Question)
    answer_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    modification_time = models.DateTimeField('date modified')
    up_votes = models.IntegerField(default=0)
    down_votes = models.IntegerField(default=0)
    net_votes = models.IntegerField(default=0)
    up_list = models.ManyToManyField(User, related_name="up_list")
    down_list = models.ManyToManyField(User, related_name="down_list")

    def __unicode__(self):
        return self.answer_text

    author = models.ForeignKey(User, null=True)
