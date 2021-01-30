import cbpro
import datetime as dt
import matplotlib.pyplot as plt
from yahoo_fin.stock_info import get_data
from coinbase.wallet.client import Client

# API Client Creation
public_client = cbpro.PublicClient()
public_client.get_products()

# Amount of Coins
my_btc  = 0.00640205
my_eth  = 0.03813933
my_wbtc = 0.00054638
my_ltc  = 0.06522024
my_doge = 243.756000

# Rates
btc_price  = float(public_client.get_product_ticker(product_id="BTC-USD")['price'])
eth_price  = float(public_client.get_product_ticker(product_id="ETH-USD")['price'])
wbtc_price = float(public_client.get_product_ticker(product_id="WBTC-USD")['price'])
ltc_price  = float(public_client.get_product_ticker(product_id="LTC-USD")['price'])
# Dogecoin not included
#doge_price =public_client.get_product_ticker(product_id="DOGE-USD")

myWallet = {
    "Bitcoin": float(my_btc * btc_price),
    "Etherium": float(my_eth * eth_price),
    "WBTC": float(my_wbtc * wbtc_price),
    "Litecoin": float(my_ltc * ltc_price)
}
print(myWallet)

# Total Value of Portfolio
total_portfolio_value = sum(myWallet.values())

# Percentages of Portfolio
percent_btc = (myWallet["Bitcoin"] / total_portfolio_value) * 100
percent_eth = (myWallet["Etherium"] / total_portfolio_value) * 100
percent_wbtc = (myWallet["WBTC"] / total_portfolio_value) * 100
percent_ltc = (myWallet["Litecoin"] / total_portfolio_value) * 100

# Printing To Console
seperator = "-------------------------------"

# Printing Current Prices
print('Current Coin Prices:')
print('\tBitcoin: ' + str(btc_price))
print('\tEterium: ' + str(eth_price))
print('\tWrapped Bitcoin: ' + str(wbtc_price))
print('\tLitecoin: ' + str(ltc_price)) 
print(seperator)

# Print Number of Coins
print('Number of Coins:')
print('\tBitcoin: ' + str(my_btc))
print('\tEterium: ' + str(my_eth))
print('\tWrapped Bitcoin: ' + str(my_wbtc))
print('\tLitecoin: ' + str(my_ltc)) 
print(seperator)

# Percentage of Portfolio
print('Percentage of Portfolio:')
print('\tBitcoin: ' + str(percent_btc))
print('\tEterium: ' + str(percent_eth))
print('\tWrapped Bitcoin: ' + str(percent_wbtc))
print('\tLitecoin: ' + str(percent_ltc)) 
print(seperator)

# Print Portfolio:
print('Portfolio:')
print('\tBitcoin: ' + str(myWallet["Bitcoin"]))
print('\tEterium: ' + str(myWallet["Etherium"]))
print('\tWrapped Bitcoin: ' + str(myWallet["WBTC"]))
print('\tLitecoin: ' + str(myWallet["Litecoin"]))
print('\tTotal: ' + str(total_portfolio_value))
print(seperator)

#---------------------------------------------------------------------#

# Tickers for Plots
tickers = ['BTC', 'ETH', 'WBTC', 'LTC']
totals = [(my_btc * btc_price), (my_eth * eth_price), (my_wbtc * wbtc_price), \
    (my_ltc * ltc_price)]

# Plotting
fig, ax = plt.subplots(figsize=(16,8))
ax.set_facecolor('black')
ax.figure.set_facecolor('#121212')
ax.tick_params(axis='x', colors='white')
ax.tick_params(axis='y', colors='white')

# Pie chart
ax.set_title('My Cryptocurrency Portfolio', color='#ffe536', fontsize=20)
patches, texts, autotexts = ax.pie(totals, labels=tickers, autopct='%1.1f%%', pctdistance=0.8)
[text.set_color('white') for text in texts]

# Overview
ax.text(-2,1, 'PORTFOLIO OVERVIEW:', fontsize=14, color="#ffe536", 
    horizontalalignment='center', verticalalignment='center')
# Bitcoin
ax.text(-2, 0.90, f'Bitcoin: ${myWallet["Bitcoin"]:.2f}', fontsize=12, color="white",
    horizontalalignment='center', verticalalignment='center')
#Etherium
ax.text(-2, 0.80, f'Etherium: ${myWallet["Etherium"]:.2f}', fontsize=12, color="white",
    horizontalalignment='center', verticalalignment='center')
#WBTC
ax.text(-2, 0.70, f'Wrapped BTC: ${myWallet["WBTC"]:.2f}', fontsize=12, color="white",
    horizontalalignment='center', verticalalignment='center')
#Litecoin
ax.text(-2, 0.60, f'Litecoin: ${myWallet["Litecoin"]:.2f}', fontsize=12, color="white",
    horizontalalignment='center', verticalalignment='center')
# Seperator
ax.text(-2,0.55, '_____________________________', fontsize=12, 
    color="white", horizontalalignment='center', verticalalignment='center')
# Total Price
ax.text(-2,0.4, f'Total Amount: ${sum(totals):.2f}', fontsize=12, 
    color="white", horizontalalignment='center', verticalalignment='center')

# Coin Prices
ax.text(2,1, 'COIN PRICES:', fontsize=14, color="#ffe536", 
    horizontalalignment='center', verticalalignment='center')
# Bitcoin
ax.text(2, 0.90, f'Bitcoin: ${btc_price:.2f}', fontsize=12, color="white",
    horizontalalignment='center', verticalalignment='center')
#Etherium
ax.text(2, 0.80, f'Etherium: ${eth_price:.2f}', fontsize=12, color="white",
    horizontalalignment='center', verticalalignment='center')
#WBTC
ax.text(2, 0.70, f'Wrapped BTC: ${wbtc_price:.2f}', fontsize=12, color="white",
    horizontalalignment='center', verticalalignment='center')
#Litecoin
ax.text(2, 0.60, f'Litecoin: ${ltc_price:.2f}', fontsize=12, color="white",
    horizontalalignment='center', verticalalignment='center')

# Number of Coins
ax.text(2,-.30, ' NUMBER OF COINS:', fontsize=14, color="#ffe536", 
    horizontalalignment='center', verticalalignment='center')
# Bitcoin
ax.text(2, -.40, f'Bitcoin: {my_btc}', fontsize=12, color="white",
    horizontalalignment='center', verticalalignment='center')
#Etherium
ax.text(2, -0.50, f'Etherium: {my_eth}', fontsize=12, color="white",
    horizontalalignment='center', verticalalignment='center')
#WBTC
ax.text(2, -0.60, f'Wrapped BTC: {wbtc_price}', fontsize=12, color="white",
    horizontalalignment='center', verticalalignment='center')
#Litecoin
ax.text(2, -0.70, f'Litecoin: {my_ltc}', fontsize=12, color="white",
    horizontalalignment='center', verticalalignment='center')

# Show Plot on Screen
plt.show()

'''
Removed Code:
    # # Center Black Circle
    # my_circle = plt.Circle((0,0), 0.55, color='black')
    # plt.gca().add_artist(my_circle)
    Explanation:
        Plots a black circle in pie chart, making it a doughnut
        chart.  
'''