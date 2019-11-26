from websocket import create_connection
import json

ws = create_connection("wss://api.upbit.com/websocket/v1")

print("Sent")
print("Receiving...")

while(True):    
    ws.send('[{"ticket":"UNIQUE_TICKET"},{"type":"trade","codes":["KRW-BTC"]},{"type":"orderbook","codes":["KRW-ETH"]}]')
    result =  ws.recv()
    json_data = json.loads(result)

    if json_data["type"] == 'orderbook':
        orderbook = json_data["orderbook_units"][0]
        
        ask_price = orderbook["ask_price"]
        bid_price = orderbook["bid_price"]
        ask_size = orderbook["ask_size"]
        bid_size = orderbook["bid_size"]

        print("ask_price : %s, bid_price : %s, ask_size : %s, bid_size : %s \n" %(ask_price,bid_price,ask_size,bid_size))

    elif json_data["type"] == 'trade':
        trade_price = json_data['trade_price']
        trade_volume = json_data['trade_volume']
        ask_bid = json_data['ask_bid']

        print("trade_price : %s, trade_volume : %s, ask_bid : %s" %(trade_price,trade_volume,ask_bid))
ws.close()
