from THD_MD.marketStores import market_stores
from THD_MD.store_info import store_info
from THD_MD.getMarkets import listMarkets
from THD_MD.directions_api import get_directions_duration




#def test_store_list():
   #assert isinstance(market_stores(2), dict)


#def test_market_list():
    #to to see if get_markets returns a list of markets with numbers
    # [{market_name: name, market_number},{...}]
    #assert isinstance(listMarkets(), dict)


def test_store_info_experience():
    markets = listMarkets()
    assert isinstance(markets,dict)
    assert isinstance(market_stores(2), dict)
    assert isinstance(markets['SAN FRANCISCO BAY'],dict)
    assert markets['SAN FRANCISCO BAY']['stores'] == 44
    assert isinstance(store_info(store_number=114), dict)
    assert isinstance(get_directions_duration('Charlotte, NC', 'Atlanta, Ga', 'Home'), dict)



