
>   Look at License to see where credit is due, This is a cloned copy of the original creator rohanpai25 with minor customizations



# Robinhood
Python Framework to make trades with Robinhood Private API.
See this [blog post](https://medium.com/@rohanpai25/reversing-robinhood-free-accessible-automated-stock-trading-f40fba1e7d8b).

##Current Features 
- Placing buy orders (`Robinhood.place_buy_order`)
- Placing sell order (`Robinhood.place_sell_order`)
- Quote information (`Robinhood.quote_data`)
- User portfolio data (`Robinhood.portfolios`)
- User positions data (`Robinhood.positions`)
## RedKloud additions
   + Keyring user data is saved via OS key authentication system
   + get watchlist
   + reorganize rh watchlist
   + add to watch rh watchlist
   + remove the last made Order
   + get fundamentals
  

- Still developing more, as i explore

###How To Install:
    pip install -r requirements.txt
***    
###Converting to Python 3
By default, this module is written in Python 2.  For users who wish to use the module in Python 3, use the following command:
    
    2to3 -w Robinhood.py
***
###How to Use (see [example.py](https://github.com/MeheLLC/Robinhood/blob/master/example.py))

    from Robinhood import Robinhood
    
    #if no user is found in the system OS keyring access, then API will prompt to sign up a new user
    my_trader = Robinhood()
    
    #will automatically prompt for a keyring 'sign up' 
    
    my_trader.login()
  
    stock_instrument = my_trader.instruments("GEVO")[0]
    
    #get quote information of the stock
    quote_info = my_trader.quote_data("GEVO")

    
    #add a new symbol to default watchlist, restart robinhood app to see it
    my_trader.addToWatchlist('AMD')
    
    #get the current watchlist of the Robinhood account
    watch_list = my_trader.watchlist() 
    
    #show watch list
    for stock in watch_list:
      print(stock['symbol'])
      

   #place an limit order
   my_trader.place_buy_order("APPL",'limit',bid_price=140.00, quantity=200)
   #place market order
   my_trader.place_buy_order("APPL", quantity=200)
   
   #place sell limit order
   my_trader.place_sell_order("APPL","limit",bid_price=150.00, quantity=200)
   
   #place a market sell order
   my_trader.place_sell_order("APPL",quantity=200)
   
   #remove the last order placed
   my_trader.cancelMostRecentOrder()
     
   #show fundamentals for a given security
   
   my_trader.getFundamentals('APPL')
   
***
###Data returned
* Quote data
  + Ask Price
  + Ask Size
  + Bid Price
  + Bid Size
  + Last trade price
  + Previous close
  + Previous close date
  + Adjusted previous close
  + Trading halted
  + Updated at
  + Historical Price
* User portfolio data
  + Adjusted equity previous close
  + Equity
  + Equity previous close
  + Excess margin
  + Extended hours equity
  + Extended hours market value
  + Last core equity
  + Last core market value
  + Market value
  + Order history
  + Dividend history
* User positions data
  + Securities owned
* News
########### 


------------------

# Related

* [robinhood-ruby](https://github.com/rememberlenny/robinhood-ruby) - RubyGem for interacting with Robinhood API
* [robinhood-node](https://github.com/aurbano/robinhood-node) - NodeJS module to make trades with Robinhood Private API
