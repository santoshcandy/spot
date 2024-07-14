from twilio.rest import Client
import os

# Load your Twilio credentials from environment variables
account_sid = 'ACc641b7eea4f8c5918213214049ba79c4'
auth_token = '3545dafa53f96c22325defd297a3524c'

# Create a Twilio client
client = Client(account_sid, auth_token)

# Send a WhatsApp message
message = client.messages.create(
  from_='whatsapp:+14155238886',
  body='Your appointment is coming up on July 21 at 3PM',
  to='whatsapp:+918015153921'
)

 
print(f"Message sent with SID: {message.sid}")
