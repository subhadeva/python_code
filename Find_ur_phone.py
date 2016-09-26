from twilio.rest import TwilioRestClient
account_Sid = "ACa82b0a839fa1914d18dd7c460d3146aa"
authToken = "c54585083d6e22afd8bea9ce13d7a462"
Client    = TwilioRestClient(account_Sid, authToken)
call      = Client.calls.create(from_="+12052360636", 
            to="+919566230673", url="http://twimlets.com/holdmusic?Bucket=com.twilio.music.ambient")