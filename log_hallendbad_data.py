import websocket
import json
import ssl
from datetime import datetime
import os

def on_message(ws, message):
    data = json.loads(message)
    for element in data:
        if element['uid'] == 'SSD-4':
            visitor_count = element['currentfill']
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print(f"Timestamp: {timestamp}, Current visitor count: {visitor_count}")
            
            # Save to file
            # check if file exists
            if not os.path.isfile('visitor_count_log.csv'):
                with open('visitor_count_log.csv', 'w') as file:
                    file.write("Timestamp, Visitor count\n")
            with open('visitor_count_log.csv', 'a') as file:
                file.write(f"{timestamp}, {visitor_count}\n")
            ws.close()

def on_error(ws, error):
    print(error)

def on_close(ws, close_status_code, close_msg):
    print("### closed ###")

def on_open(ws):
    def run(*args):
        ws.send("all")  # Sending "all" as per the JavaScript snippet provided.
    run()

if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("wss://badi-public.crowdmonitor.ch:9591/api",
                              on_open=on_open,
                              on_message=on_message,
                              on_error=on_error,
                              on_close=on_close)

    ws.run_forever(sslopt={"cert_reqs": ssl.CERT_NONE})
