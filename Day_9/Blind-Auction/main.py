from art import logo

print(logo)
bid_dict = {}


def highest_bidder(bidding_record):
    bid_value = 0
    winner = ""
    for key in bidding_record:
        # storing the values in bid_result
        bid_result = bidding_record[key]
        if bid_result > bid_value:
            bid_value = bid_result
            winner = key
    print(f"The winner is {winner} with a bid of {bid_value}")


should_continue = True
while should_continue:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    bid_dict[name] = bid
    choice = input("Are there any other bidders? Type 'yes' or 'no'.").lower()
    if choice == "yes":
        pass
    elif choice == "no":
        highest_bidder(bidding_record=bid_dict)

        should_continue = False




