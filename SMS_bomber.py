from twilio.rest import Client
import time
import platform
import os

try:
    raw_input
except NameError:
    raw_input = input

def banner():
    if platform.system().lower() == "windows":
        os.system("cls")
    else:
        os.system("clear")
    print("""
    /$$$$$$  /$$      /$$  /$$$$$$        /$$$$$$$   /$$$$$$  /$$      /$$ /$$$$$$$  /$$$$$$$$ /$$$$$$$ 
    /$$__  $$| $$$    /$$$ /$$__  $$      | $$__  $$ /$$__  $$| $$$    /$$$| $$__  $$| $$_____/| $$__  $$ 
    | $$  \__/| $$$$  /$$$$| $$  \__/      | $$  \ $$| $$  \ $$| $$$$  /$$$$| $$  \ $$| $$      | $$  \ $$ 
    |  $$$$$$ | $$ $$/$$ $$|  $$$$$$       | $$$$$$$ | $$  | $$| $$ $$/$$ $$| $$$$$$$ | $$$$$   | $$$$$$$/  
     \____  $$| $$  $$$| $$ \____  $$      | $$__  $$| $$  | $$| $$  $$$| $$| $$__  $$| $$__/   | $$__  $$   
     /$$  \ $$| $$\  $ | $$ /$$  \ $$      | $$  \ $$| $$  | $$| $$\  $ | $$| $$  \ $$| $$      | $$  \ $$    
    |  $$$$$$/| $$ \/  | $$|  $$$$$$/      | $$$$$$$/|  $$$$$$/| $$ \/  | $$| $$$$$$$/| $$$$$$$$| $$  | $$  
     \______/ |__/     |__/ \______/       |_______/  \______/ |__/     |__/|_______/ |________/|__/  |__/              
                                                                                                                                                                                                    
                                       By : D3XBugg3R                                                                                                 
    Note : I won't be responsible for any damage caused by this script, Use at your own risk
    """)

def send_sms(account_sid, auth_token, to_number, message, count, sleep_time):
    # Twilio client
    client = Client(account_sid, auth_token)

    for x in range(count):
        try:
            message_sent = client.messages.create(
                body=message,
                from_='+18647774680',  # Your Twilio number
                to=to_number
            )
            print(f"Message {x+1} sent successfully: {message_sent.sid}")
        except Exception as e:
            print(f"Error sending message {x+1}: {e}")
        time.sleep(sleep_time)

try:
    banner()
    account_sid = ''  # Replace with your Twilio SID
    auth_token = '4edb0933402a1b11a4d3faa475ca0691'  # Replace with your Twilio Auth Token
    
    number = raw_input("Enter mobile number (Yemen format +967xxxxxxxxx): ")
    count = int(raw_input("Enter number of messages to send: "))
    sleep_time = int(raw_input("Enter time of sleep (seconds): "))
    message = raw_input("Enter the message: ")
    
    send_sms(account_sid, auth_token, number, message, count, sleep_time)
except Exception as e:
    print("Something went wrong. Please check your inputs or Twilio account.")
