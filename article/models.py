from django.db import models

# Create your models here.



class Article(models.Model):
    class Meta:
        db_table = 'article'

    article_name = models.CharField(max_length=200)
    article_text = models.TextField()
    article_add_date = models.DateTimeField()
    article_edit_date = models.DateTimeField()

    def __unicode__(self):
        return self.article_name