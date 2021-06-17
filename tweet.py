import tweepy

# Authenticate to Twitter
auth = tweepy.OAuthHandler(" ", 
    " ")
auth.set_access_token(" ", 
    " ")

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

user = api.get_user("@")
for following in user.friends():
    print(following.name)
print("User details:")
print(user.name)
print(user.description)
print(user.location)
