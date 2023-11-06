from typing import List

import pandas as pd

df = pd.read_csv("hotels.csv", dtype={"id": str})  # dtype = str)
df_cards: list[dict] = pd.read_csv("cards.csv", dtype=str).to_dict(orient="records")
df_cards_security = pd.read_csv("card_security.csv", dtype=str)

class Hotel:
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
        self.name = df.loc[df["id"] == self.hotel_id, "name"].squeeze()

    def book(self):
        """Book a hotel by changing its availability to no"""
        df.loc[df["id"] == self.hotel_id, "available"] = "no"
        # df.to_csv("hotels.csv", index=False)

        # df.to_csv(r"C:\Users\shibb\PythonProjectsFinal\app11.1_hotel_booking\hotels.csv")

    def available(self):
        """Checks if the hotel is available"""
        availability = df.loc[df["id"] == self.hotel_id, "available"].squeeze()
        if availability:
            return True
        else:
            return False


class ReservationTicket:
    def __init__(self, customer_name, hotel_object):
        self.name = customer_name
        self.hotel = hotel_object

    def generate(self):
        content = f"""
        Thank you for your reservation!
        Here are your booking data:
        Name: {self.name}
        Hotel name: {self.hotel}
        """
        return content


class CreditCard:
    def __init__(self, number):
        self.number = number

    def validate(self, expiration, holder, cvc):
        card_data = {"number": self.number, "expiration": expiration,
                     "holder": holder, "cvc": cvc}
        if card_data in df_cards:
            return True
        else:
            return False


class SecureCreditCard(CreditCard):
    def authenticate(self, given_password):
        password = df_cards_security.loc[df_cards_security["number"] == self.number, "password"].squeeze()
        if password == given_password:
            return True
        else:
            return False


# class ReservationSpa(Hotel):
#     def generate(self):
#         content = f"""
#         Thank you for your SPA reservation!
#         Here are your SPA booking data:
#         Name: {self.name}
#         Hotel name: {self.hotel}
#         """
#         return content


## PROGRAMME MAIN LOOP

print(df)
print(df.info())
hotel_ID = input("Enter the id of the hotel: ")
hotel = Hotel(hotel_ID)

if hotel.available():
    # number = input("Input card number:")
    # expiration = input("Input expiration:")
    # holder= input("Input holder:")
    # cvc = input("Input cvc:")

    credit_card = SecureCreditCard(number="1234")
    if credit_card.validate(expiration="Dec-26", holder="JOHN SMITH", cvc="123"):
        # given_password = input("Please enter your credit card password:)

        if credit_card.authenticate(given_password="mypass"):
            hotel.book()
            name = input("Enter your name: ")
            reservation_ticket = ReservationTicket(customer_name=name, hotel_object=hotel.name)
            print(reservation_ticket.generate())
        else:
            print("Please enter a valid password")
    else:
        print("There was a problem with you card payment")
else:
    print("Hotel is not free")


# spa = input("Do you want a spa package(yes or no)? ")
#
# if spa == "yes":
#     # spa_reservation.book()
#     name = input("Enter your name: ")
#     spa_ticket = ReservationSpa(customer_name=self.name, hotel_object=hotel.name)
#     print(spa_ticket.generate())
