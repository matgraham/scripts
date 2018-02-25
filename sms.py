from twilio.rest import Client

accountSID = 'AC77fc234a4cc8341973094e981497b6c2'
authToken = '369cff118c6adb730a28c7077f9b25a7'
twilioCli = Client(accountSID, authToken)
myTwilioNumber = '+13215783537'
myCellPhone = '+13862166681'
message = twilioCli.messages.create(body='This is coming from my computer', from_=myTwilioNumber,to=myCellPhone)