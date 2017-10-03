from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from django.contrib.auth.models import User
from .models import Coins,Tag_Vocabulary,Tag_Term_Data,User_Coins,Coin_Prices
from .forms import UserCoinForm
import requests,json


def dashboard(request,user_id=None):
	user = get_object_or_404(User, id=user_id)
	if user:
		user_coins = User_Coins.objects.filter(user_id=user.id)
		form = UserCoinForm(request.POST or None)
		if form.is_valid():
			coin_id = form.cleaned_data.get('coin')
			currency_type = form.cleaned_data.get('currency_type')
			total_investment = form.cleaned_data.get('total_investment')
			units_owned = form.cleaned_data.get('units_owned')
			exchange_id = -1
			obj, created = User_Coins.objects.update_or_create(
							    user_id=user.id,coin_id=coin_id,
							    defaults={'currency_type':currency_type,
								    'total_investment':total_investment,'units_owned':units_owned,
								    'exchange_id':exchange_id
							   	},
							)
		
			return redirect('/dashboard/'+str(user.id))
		return render(request, 'dashboard.html', {'form':form,'user_coins':user_coins})


def get_coin_table(request):
	coins_data = [];
	coins = coins_list()
	user = get_object_or_404(User, id=request.user.id)
	user_coins = User_Coins.objects.filter(user_id=user.id)
	current_bitcoin_price = get_current_bitcoin_price()
	current_ethereum_price = get_current_ethereum_price()
	# current_bitcoin_price = 1
	# current_ethereum_price = get_current_ethereum_price()
	total_investment = total_investment_value = 0
	for coin in user_coins:
		coin_data = {}
		coin_data['coin_name'] = coins[coin.coin_id]
		coin_data['total_investment'] = coin.total_investment
		coin_data['units_owned'] = coin.units_owned
		if(coins[coin.coin_id] == 'Bitcoin'):
			coin_data['investment_value'] = round(coin.units_owned * current_bitcoin_price,2)
		elif(coins[coin.coin_id] == 'Ethereum'):
			coin_data['investment_value'] = round(coin.units_owned * current_ethereum_price,2)
		coins_data.append(coin_data)
		total_investment += coin_data['total_investment']
		total_investment_value += coin_data['investment_value']
	coin_table_html = render(request, 'coin_table.html', {'coins_data':coins_data,
			'total_investment':total_investment,'total_investment_value':round(total_investment_value,2)})
	return coin_table_html


def populate_database_with_data(request):
	coins_data = [['Bitcoin','BTC'],['Ethereum','ETH'],['Ripple','XRP'],['Bitcoin Cash','BCH'],
					['Litecoin','LTC'],['Dash','DASH'],['Nem','XCM'],['Monero','XMR'],['Iota','IOT'],
						['Neo','NEO']]
	vocabularies = ['currencies','exchanges']
	currencies = ['USD','INR']
	exchanges = ['Unocoin','Zebpay']
	for coin in coins_data:
		coin_entry = Coins.objects.get_or_create(coin_name=coin[0], coin_abbr=coin[1])
	for vocab in vocabularies:
		vocab_entry = Tag_Vocabulary.objects.get_or_create(vocab_name=vocab)

	currencies_tag = Tag_Vocabulary.objects.get(vocab_name='currencies')
	currencies_id = currencies_tag.id
	exchanges_tag = Tag_Vocabulary.objects.get(vocab_name='exchanges')
	exchanges_id = exchanges_tag.id
	for currency in currencies:
		currency_entry = Tag_Term_Data.objects.get_or_create(ttd_tag_id=currencies_id, 
																	ttd_name=currency)
	for exchange in exchanges:
		exchange_entry = Tag_Term_Data.objects.get_or_create(ttd_tag_id=exchanges_id, 
																	ttd_name=exchange)

	return redirect('/')


def coins_list():
	coins_data = {}
	coins = Coins.objects.all()
	for coin in coins:
		coins_data[coin.id] = coin.coin_name

	return coins_data


def get_current_bitcoin_price(currency='INR'):
	url = 'https://blockchain.info/ticker'
	blockchain_data = requests.get(url)
	blockchain_json = json.loads(blockchain_data.text)
	current_price = blockchain_json[currency]['last']

	return current_price


def get_current_ethereum_price(currency='INR'):
	url = 'https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=USD,INR'
	eth_data = requests.get(url)
	eth_json = json.loads(eth_data.text)
	current_price = eth_json['INR']

	return current_price