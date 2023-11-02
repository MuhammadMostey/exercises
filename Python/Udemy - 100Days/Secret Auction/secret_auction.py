secret_auction_logo = '''
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

print("\n \nWelcome to the Secret Auction App - Developed by: Muhammad Mostey")
print(secret_auction_logo, "\n")

remaining_bidders = True
bids = {}

# Function: Compares all values of a dictionary and prints the highst value compared to other dictionary items
def highstBid(bids):
    
    least = 0

    for bidder in bids:
        
        if (least == 0 ):
            least = bids[bidder]
            key = bidder
            
        if(bids[bidder] > least):
            least = bids[bidder]
            key = bidder   
    print(f"\nThe winner is {key} with a bid of ${bids[key]}\n\n")


while(remaining_bidders):
    key = input ("What's your name?: ")
    value = float(input ("What's your bid?: "))
    
    bids[key] = value;
    again = input("Are there other bidders? Type 'yes' or 'no'. ").lower()
    if(again == "no"):
        remaining_bidders = False
        highstBid(bids)