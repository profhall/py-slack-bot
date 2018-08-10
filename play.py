from THD_MD.getMarkets import listMarkets

mkts = listMarkets()
print(mkts)

def markets():
    for market in mkts:
        yield market

mktss = markets()
print(next(mktss))
print(next(mktss))
print(next(mktss))