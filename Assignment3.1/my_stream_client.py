from websocket import create_connection

ws = create_connection("wss://api.upbit.com/websocket/v1")
print('Sending "[{"ticket":"UNIQUE_TICKET"},{"type":"trade","codes":["KRW- BTC"]},{"type":"orderbook","codes":["KRW-BTC"]}]"...')
ws.send('[{"ticket":"UNIQUE_TICKET"},{"type":"trade","codes":["KRW- BTC"]},{"type":"orderbook","codes":["KRW-BTC"]}]')
print("Sent")
print("Receiving...")

while(True):
    result =  ws.recv()
    print("Received '%s'" % result)
ws.close()