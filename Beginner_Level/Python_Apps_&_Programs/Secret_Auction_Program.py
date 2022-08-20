import os

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)

bids = {}
currently_bidding = True

def clear_console():
    os.system('cls')

def find_highest_bid(bidding_record):
    highest_bid = 0
    winner = ''
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f'The winner is {winner} with a bid of ${highest_bid}')

while currently_bidding:
    name = input('What is your name?: ')
    price = int(input('What is your bid?: $'))
    bids[name] = price
    keep_bidding = input("Are there any more bidders? Type 'yes' or 'no'.\n")
    if keep_bidding == 'no':
        currently_bidding = False
        find_highest_bid(bids)
    elif keep_bidding == 'yes':
        clear_console()
