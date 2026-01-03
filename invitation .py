# Invitation Program

print("🎉 Welcome to the Invitation Creator! 🎉\n")

# Get details from the user
event_name = input("event: ")
host_name = input("guest: ")
date = input("date: ")
time = input("time: ")
location = input("venu: ")

# Create the invitation
invitation = f"""
----------------------------------------
        🎊 You're Invited! 🎊


Event: {event_name}
Hosted by: {host_name}
Date: {date}
Time: {time}
Location: {location}
We hope you can join us for this special occasion!
----------------------------------------
"""

# Display the invitation
print(invitation)
