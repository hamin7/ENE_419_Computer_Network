from websocket import create_connection
import json

ws = create_connection("wss://api.upbit.com/websocket/v1")
#print('Sending "[{"ticket":"UNIQUE_TICKET"},{"type":"trade","codes":["KRW- BTC"]},{"type":"orderbook","codes":["KRW-BTC"]}]"...')
ws.send('[{"ticket":"UNIQUE_TICKET"},{"type":"trade","codes":["KRW- BTC"]},{"type":"orderbook","codes":["KRW-BTC"]}]')
print("Sent")
print("Receiving...")

while(True):
    ask_price = 0
    result =  ws.recv()
    json_data = json.loads(result)
    orderbook = json_data["orderbook_units"][0]
    #trade = json_data["trade_price"]
    #print(orderbook)
    print(json_data)
ws.close()