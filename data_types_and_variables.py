# You have rented some movies for your kids: 
# The little mermaid (for 3 days), 
# Brother Bear (for 5 days, they love it), 
# and Hercules (1 day, you don't know yet if they're going to like it). 
# If price for a movie per day is 3 dollars, how much will you have to pay?

the_little_mermaid_days = 3
brother_bear_days = 5
hercules_days = 1
price = 3

(price * the_little_mermaid_days) + (price * brother_bear_days) + (price * hercules_days)

#Suppose you're working as a contractor for 3 companies:
#  Google, Amazon and Facebook, they pay you a different rate per hour.
#  Google pays 400 dollars per hour, Amazon 380, and Facebook 350. 
# How much will you receive in payment for this week? 
# You worked 10 hours for Facebook,
#  6 hours for Google and 4 hours for Amazon.

google_pay = 400
amazon_pay = 380
facebook_pay = 350

google_hours = 6
amazon_hours = 4
facebook_hours = 10 

(google_pay * google_hours) + (amazon_pay * amazon_hours) + (facebook_pay * facebook_hours)

# A student can be enrolled to a class only if the class is not full
#  and the class schedule does not conflict with her current schedule.

class_not_full = True
class_conflicts_with_current_schedule = False 

able_to_enroll = class_not_full and not class_conflicts_with_current_schedule
able_to_enroll 

#A product offer can be applied only if people buys more than 2 items, and the offer has not expired. 
# Premium members do not need to buy a specific amount of products.

more_than_two items = True
offer_not_expired = True 
premium_member = True 

product_offer = (more_than_two_items or premium_member) and offer_not_expired 

username = 'codeup'
password = 'notastrongpassword'

#the password must be at least 5 characters
len(password) >=  5 

#the username must be no more than 20 characters
len(username) =< 20

# the password must not be the same as the username
password != username

#bonus neither the username or password can start or end with whitespace
username[0] != " " and username[-1] != " "
password[0] != " " and password[-1] != " "

password = "Jolie"
username = "Jolien"
len(password) >= 5 and password != username and password[0] != " " and password[-1] != " "
