class User:
    def __init__(self, first_name, last_name, email, age, is_rewards_member=False, gold_card_points=0):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = is_rewards_member
        self.gold_card_points = gold_card_points
    
    def display_info(self):
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Email: {self.email}")
        print(f"Age: {self.age}")
        print(f"Rewards Member: {self.is_rewards_member}")
        print(f"Gold Card Points: {self.gold_card_points}")
    
    def enroll(self):
        if self.is_rewards_member:
            print("User already a member.")
            return False
        else:
            self.is_rewards_member = True
            self.gold_card_points = 200
            return True
    
    def spend_points(self, amount):
        if amount <= self.gold_card_points:
            self.gold_card_points -= amount
            print(f"{amount} points spent successfully.")
        else:
            print("Insufficient points to spend.")

# Create a user instance and call display_info method
user1 = User("Mounir", "Said", "niri@gmail.com", 36)
user1.display_info()

# Call enroll method on the user
user1.enroll()

# Create 1 more instances of the User class
user2 = User("ali", "ahmad", "ali@gmail.com", 33)


# Have the first user spend 50 points
user1.spend_points(50)

# Have the second user enroll
user2.enroll()

# Have the second user spend 80 points
user2.spend_points(80)

# Call display_info on each user
user1.display_info()
user2.display_info()


# re-enroll the first user
user1.enroll()
