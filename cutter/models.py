from django.db import models


class URL(models.Model):

    full_url = models.CharField(max_length=200)
    short_url = models.CharField(max_length=10, default='')
    max_clicks = models.IntegerField(default=0)
    count_clicks = models.IntegerField(default=0)
    until_date = models.DateField(null=True)
    create_date = models.DateField(auto_now_add=True, null=True)

    def click(self):
        self.count_clicks += 1
        self.save()

    def clicks_check(self):
        if self.count_clicks >= self.max_clicks:
            self.delete()

    def date_check(self):
        ...
