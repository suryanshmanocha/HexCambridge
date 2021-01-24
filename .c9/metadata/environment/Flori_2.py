{"changed":true,"filter":false,"title":"Flori_2.py","tooltip":"/Flori_2.py","value":"","undoManager":{"mark":0,"position":-1,"stack":[[{"start":{"row":0,"column":0},"end":{"row":46,"column":4},"action":"insert","lines":["from Main import *","","print(book.asks)","print(book.bids)","","prices = dict() # empty dict","","print([price_vol.price for price_vol in book.asks])","print([price_vol.price for price_vol in book.bids])","","instrument_id1 = 'PHILIPS_A'","instrument_id2 = 'PHILIPS_B'","books = e.get_last_price_book(instrument_id)","","def print_table(books):","    print(\"bid | price | ask\")","    for ask in books.asks:","        print(f\"    | {round(ask.price,1)} | {ask.volume}\")","    for bid in books.bids:","        print(f\"{bid.volume} | {round(bid.price,1)} |      \")","        ","        ","print_table(books)","print_table(e.get_last_price_book(instrument_id2))","","","","import heapq","","def get_highest_profit(id1,id2):","    # use heaps - max heap for bid price and min heap for ask price ","    # max heap for bid price - accross both books","    book1 = e.get_last_price_book(id1)","    book2 = e.get_last_price_book(id2)","    #bids_heap_max = heapq._heapify_max([bid.price for bid in book1.bids] + [bid2.price for bid2 in book2.bids]) ","    #asks_heap_min = heapq.heapify([ask.price for ask in book1.asks] + [ask2.price for ask2 in book2.asks]) ","    max_profit = max([bid.price for bid in book1.bids] + [bid2.price for bid2 in book2.bids]) - min([ask.price for ask in book1.asks] + [ask2.price for ask2 in book2.asks])","    if max_profit > 0:","        return max_profit","    else:","        return -1 * max_profit","","profit = get_highest_profit(instrument_id1, instrument_id2)","print(profit)","    ","    ","    "],"id":1}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":0,"column":0},"end":{"row":0,"column":0},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1611449065523}