# Code needed to send a message from and to phone numbers
# we import the Twilio client from the dependency we just installed
from twilio.rest import Client

# the following line needs your Twilio Account SID and Auth Token
client = Client("", "026d66a6d5b6954334ec4a1043c1163c")

# change the "from_" number to your Twilio number and the "to" number
# to the phone number you signed up for Twilio with, or upgrade your
# account to send SMS to any phone number
client.messages.create(to="+12817403025", 
                       from_="+17692355901", 
                       body="Hello from Python!")
