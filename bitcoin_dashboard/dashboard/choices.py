from .models import Coins


coins = Coins.objects.all()
COINS_CHOICES = [('','Please select a coin')]
for coin in coins:
	COINS_CHOICES.append((coin.id,coin.coin_name+' ('+coin.coin_abbr+')'))

CURRENCY_CHOICES = (
		('USD','USD'),
		('INR','INR'),
	)

COINS_CHOICES = tuple(COINS_CHOICES)