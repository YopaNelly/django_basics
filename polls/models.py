from django.db import models

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
    pub_data = models.DateTimeField("date published")


class Choice(models.Model):

    # ForeignKey. That tells Django each 
    # Choice is related to a single Question.
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    # . CharField, for example, requires that
    #  you give it a max_length. That’s used 
    # not only in the database schema, but in validation

    choise_text = models.CharField(max_length = 200)

    #  set the default value of votes to 0.
    votes = models.IntegerField(default = 0)
