# Twitter API
from requests_oauthlib import OAuth1Session
import json

key = "vORyHnmDqljgnzC0AakEpdrSb"
secret = "cVAZHQjnd5mtYg3HP6TRoW2Ly0zfOZoZccLPtLF4rEIu7BCsK4"
token = "4745335103-g9wsWOWsxS2AzkTVQNPiH3t9CsUcCu1yCjgr95u"
token_secret = "Pu4ZNFVefu5itcS15UW2QEPARoZsNBkFUpCZltAz7ZUt1"

twitter = OAuth1Session(key, client_secret=secret,
                        resource_owner_key=token,
                        resource_owner_secret=token_secret)

r = twitter.get(
    'https://stream.twitter.com/1.1/statuses/sample.json?retweet_count=0&geocode=59.9138688,10.752245399999993',
    stream=True
)

for line in r.iter_lines():
    if line:
        #print line
        parsedLine = json.loads(line) #['text']
        print json.dumps(parsedLine, indent=4, sort_keys=True)


#59.9138688 lat
#10.752245399999993 long
