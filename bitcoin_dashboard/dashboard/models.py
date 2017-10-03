from __future__ import unicode_literals
from django.db import models


class Tag_Vocabulary(models.Model):
	vocab_name = models.CharField(max_length=100)


class Tag_Term_Data(models.Model):
	ttd_tag_id = models.IntegerField()
	ttd_name = models.CharField(max_length=255)


class Coins(models.Model):
	coin_name = models.CharField(max_length=100)
	coin_abbr = models.CharField(max_length=10)


class Coin_Prices(models.Model):
	coin_id = models.IntegerField()
	exchange_id = models.IntegerField()
	price_usd = models.FloatField()
	price_inr = models.FloatField()
	last_updated = models.DateTimeField(auto_now=True, auto_now_add=False)


class User_Coins(models.Model):
	user_id = models.IntegerField()
	coin_id = models.IntegerField()
	exchange_id = models.IntegerField()
	currency_type = models.CharField(max_length=10)
	total_investment = models.FloatField()
	units_owned = models.FloatField()

	class Meta:

		unique_together = ['user_id','coin_id']





