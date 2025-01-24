import data
import art
import random
print(art.logo)
score = 0
def higher_lower():
    global score
    random_data = random.sample(game_data.data, 2)
    a = random_data[0]
    b = random_data[1]
    if score > 0:
        print(f"You're right! current score: {score}")
    print(f"Compare A: {a['name']}, a {a['description']} from {a['country']}.")
    print(art.vs)
    print(f"Against B: {b['name']}, a {b['description']} from {b['country']}.")
    u_input = input("Who has more followers? Type 'A' or 'B':  ").lower()

    if a['follower_count'] > b['follower_count'] and u_input == "a":
        score += 1
        higher_lower()
    elif a['follower_count'] < b['follower_count'] and u_input == "b":
        score += 1
        higher_lower()
    else:
        print(f"Sorry, That is wrong. Final score: {score}")


higher_lower()