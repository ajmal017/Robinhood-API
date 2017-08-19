from Robinhood import Robinhood

rb = Robinhood()
rb.login_prompt()

watchlist = rb.watchlist()
symbols = ' '.join([instrument['symbol'] for instrument in watchlist])
print(symbols)
with open("watchlist.txt", "w") as text_file:
    text_file.write("{0}".format(symbols))
