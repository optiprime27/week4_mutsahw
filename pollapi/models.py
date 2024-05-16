from django.db import models

# Create your models here.

class Topic(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    agree = models.IntegerField(default=0)
    disagree = models.IntegerField(default=0)
    createdAt = models.DateTimeField(auto_now_add=True)

    def total_votes(self):
        return self.agree + self.disagree

    def agree_rate(self):
        total_value = self.total_votes()
        if total_value == 0:
            return 0
        return self.agree / total_value

    def disagree_rate(self):
        total_value = self.total_votes()
        if total_value == 0:
            return 0
        return self.disagree / total_value

    def record_vote(self, is_agree=True):
        if is_agree:
            self.agree += 1
        else:
            self.disagree += 1
        self.save()

    def __str__(self):
        return self.title
