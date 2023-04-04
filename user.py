class User:
    def __init__(self, firstName, lastName, email, age):
        self.first_name = firstName
        self.last_name = lastName
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0

    def display_info(self):
        print(f"{self.first_name}")
        print(f"{self.last_name}")
        print(f"{self.email}")
        print(f"{self.age}")
        print(f"{self.is_rewards_member}")
        print(f"{self.gold_card_points}")
        return self
    
    def enroll_self(self):
        self.is_rewards_member = True
        self.gold_card_points = 200
        return self
    
    def spend_points(self,amount):
        self.gold_card_points -= amount
        return self


user1 = User("Mark", "Lambson", "mj@lambson.com", 30)
user1.display_info().enroll_self().spend_points(100).display_info()


user2 = User("Levi", "Ackerman", "titanssuck@scouts.com", 25)
user2.display_info().enroll_self().spend_points(73).display_info()
