import time
import random

# Short replies your bot can use
replies = [
    "ok", "hmm", "yeah", "nah", "lol",
    "idk", "sure", "wait", "huh", "bruh"
]

print("LazyBot 🤖: hey")

while True:
    user = input("You: ")
    if user.lower() in ["bye", "exit", "quit"]:
        print("LazyBot 🤖: cya")
        break
    
    # Random delay (to simulate "reply laterly")
    delay = random.randint(2, 6)  
    time.sleep(delay)

    # Pick a random short reply
    response = random.choice(replies)
    print(f"LazyBot 🤖: {response}")
