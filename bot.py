from instapy import InstaPy

# Write your automation here
# Stuck ? Look at the github page or the examples in the examples folder

dont_like = []
ignore_words = []
friend_list = []

# If you want to enter your Instagram Credentials directly just enter
# username=<your-username-here> and password=<your-password> into InstaPy
# e.g like so InstaPy(username="instagram", password="test1234")

bot = InstaPy(nogui=True)
bot.login()

# Set Behavior
bot.set_comments([u'👽👽👽'])
bot.set_do_comment(True, percentage=100)
# bot.set_upper_follower_count(limit=2500)

# Decide Targets

bot.like_by_users(usernames=['Chronic.alien',
                             'Poisoneddolly'], amount=100, random=True)
bot.like_by_tags([u'#👽', '#alien'], amount=500)
# bot.set_dont_include(friend_list)
# bot.set_dont_like(dont_like)
# bot.set_ignore_if_contains(ignore_words)
bot.end()
