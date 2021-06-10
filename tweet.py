import tweepy

# Authenticate to Twitter
auth = tweepy.OAuthHandler("oNIL1OS98awVJAZbnbsoGRhGW", 
    "0CRV5G2btlHJluDnZwcoMC8f0EUQis874N12wrMaxbXsEEBswQ")
auth.set_access_token("1400465690755096587-RiMVYAeuFKoK6fVFNQz1xb1J2jioB3", 
    "lgbBuyDSxKVutVX2S3Kq78oTXq4m6brwVVnwykXwbh2SW")

api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK Verified ")
except:
    print("Error during authentication")


# Create API object
api = tweepy.API(auth)

# Create a tweet
api.update_status("Hello Twitter")

user = api.get_user("@PRANJAL58541898")
for following in user.friends():
    print(following.name)
print("User details:")
print(user.name)
print(user.description)
print(user.location)
