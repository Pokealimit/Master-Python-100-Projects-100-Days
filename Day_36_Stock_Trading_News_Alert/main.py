import os, requests, pprint
from twilio.rest import Client
# from datetime import datetime
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

AV_API_KEY = os.environ.get("AV_API_KEY")
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_API_KEY = os.environ.get("NEWS_API_KEY")
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
TWILIO_SID = "<Twilio_Account_ID>"         
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")    # In terminal, RUN "export TWILIO_AUTH_TOKEN=<your_twilio_auth_token>"


## STEP 1: Use https://newsapi.org/docs/endpoints/everything
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
#HINT 1: Get the closing price for yesterday and the day before yesterday. Find the positive difference between the two prices. e.g. 40 - 20 = -20, but the positive difference is 20.
#HINT 2: Work out the value of 5% of yerstday's closing stock price. 

# * Getting TSLA stock data from alphavantage.co API
stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": AV_API_KEY
}

response = requests.get(STOCK_ENDPOINT, params=stock_parameters)
response.raise_for_status()
tsla_data = response.json()['Time Series (Daily)']
# pprint.pprint(tsla_data)
# ? Notice the first 2 keys are always the 2 latest date
# pprint.pprint(tsla_data.keys())

# * Getting hold of yesterday and the day before tsla closing price
tsla_list = [value for (key, value) in tsla_data.items()]
""" 
{'1. open': '753.4100',
  '2. high': '762.1000',
  '3. low': '751.6301',
  '4. close': '754.8600',
  '5. volume': '14077731'}]
"""
# ytd_and_day_before = tsla_list[:2]
ytd_and_day_before_closing = [ item['4. close'] for item in tsla_list[:2] ]     # [0] - yesterday, [1] - the day before
pprint.pprint(ytd_and_day_before_closing)

# * Finding the % diff in ytd vs the day before close price
diff = round( float(ytd_and_day_before_closing[0]) - float(ytd_and_day_before_closing[1]) ) * 100 / float(ytd_and_day_before_closing[0])
change_symbol = None
if diff > 0:
    change_symbol = "🔺"
else:
    change_symbol = "🔻"

abs_diff = abs(diff)

# ! NOTE: Doing the above method does not work well on SUN and MON as it will retrieve FRI and THURS (Stock market doesn't open on weekends)
# TODO Alternatively: can use datetime to check day of the week

## STEP 2: Use https://newsapi.org/docs/endpoints/everything
# Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME. 
#HINT 1: Think about using the Python Slice Operator

# * If positive_diff > 5%, need to get news from newsapi
if abs_diff > 5:
    # print("Get News")
    
    news_parameters = {
        "qInTitle": COMPANY_NAME,  # qInTitle has higher chance to search for TSLA news than q (which bunch everything with tsla together)
        "apiKey": NEWS_API_KEY

    }

    response = requests.get(NEWS_ENDPOINT, params=news_parameters)
    news_articles = response.json()['articles']
    # Get first 3 articles about TSLA
    first_3_articles = news_articles[:3]
    # pprint.pprint(first_3_articles)

    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    # Send a separate message with each article's title and description to your phone number. 
    #HINT 1: Consider using a List Comprehension.

    # * Put the 3 articles in the following format: Headline: {article title}. Brief: {article description}
    formatted_articles = [f"{STOCK}: {change_symbol}{abs_diff}%\n Headline: {article['title']}. Brief: {article['description']}" for article in first_3_articles]
    print(formatted_articles)

    #Optional: Format the SMS message like this: 
    """
    TSLA: 🔺2%
    Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
    Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
    or
    "TSLA: 🔻5%
    Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
    Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
    """

    # * Send a SMS via Twilio for each of the 3 articles
    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    for article in formatted_articles:
        message = client.messages.create(body=article, from_="<Twilio_Number>", to="<Your_own_number>")