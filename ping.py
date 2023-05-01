import json
import random
import time
import datetime

from websocket import create_connection, WebSocketConnectionClosedException
ws = create_connection("wss://currency-app-p9p5.onrender.com/course/ws/123456789")
print("Sending 'Hello, World'...")
ws.send("Hello, World")
print("Sent")
print("Receiving...")

hour_value = 2000
count = 0
while True:
    try:
        while True:
            ws.send('?')
            data = ws.recv()
            data = json.loads(data)
            # print(data, type(data))
            time.sleep(1)
            if hour_value / data['data'] > 1.01 or data['data'] / hour_value > 1.01:
                now = datetime.datetime.now()
                print("Current data and time : ", end='')
                print(hour_value, data, now.strftime("%Y-%m-%d %H:%M:%S"))
            if count > 60:
                count = 0
                hour_value = data['data']
            count += 1
    except WebSocketConnectionClosedException:
        print('Exception!!!!!')
        ws = create_connection("wss://currency-app-p9p5.onrender.com/course/ws/12345678")


