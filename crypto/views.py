from django.shortcuts import render

# Create your views here.


def home(request):
    import requests
    import json

    # Grab crypto news

    api_request = requests.get(
        "https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
    api = json.loads(api_request.content)

    # Grab crypto price
    api_request_price = requests.get(
        "https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,XRP,ETH,XLM,LTC,ADA,NEO,XMR&tsyms=USD")
    api_price = json.loads(api_request_price.content)

    return render(request, 'home.html', {'api': api, 'api_price': api_price})


def prices(request):
    import requests
    import json

    if request.method == 'POST':
        quote = request.POST['quote']
        quote = quote.upper()
        crypto_request_price = requests.get(
            "https://min-api.cryptocompare.com/data/pricemultifull?fsyms="+quote+"&tsyms=USD")
        crypto = json.loads(crypto_request_price.content)
        return render(request, 'prices.html', {'quote': quote, 'crypto': crypto})

    else:
        notfound = "Please search for a crypto with the symbol above in the Search form:"
        return render(request, 'prices.html', {'notfound': notfound})
