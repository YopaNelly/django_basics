from django.db import models
import datetime

from django.utils import timezone

"""
adding custom method to this model

"""
# Create your models here.

"""

class Question and Choice. 
A Question has a question and
 a publication date. A Choice has 
 two fields: the text of the choice 
 and a vote tally. Each Choice is 
 associated with a Question.

 """

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    """
    adding a __ste__() method to both Question and Choice

    for this to return a string and not as bellow

    "
    objects.all() displays all the questions in the database.
    >>> Question.objects.all()
    <QuerySet [<Question: Question object (1)>]>
    "
    """
    def __str__(self):
        return self.question_text
    
    # Handling time
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):

    # ForeignKey. That tells Django each 
    # Choice is related to a single Question.
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    # . CharField, for example, requires that
    #  you give it a max_length. That’s used 
    # not only in the database schema, but in validation

    choice_text = models.CharField(max_length = 200)

    #  set the default value of votes to 0.
    votes = models.IntegerField(default = 0)

    def __str__(self):
        return self.choice_text
