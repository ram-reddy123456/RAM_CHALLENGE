# This code block is used for Validating Credit Card Numbers
import re 
def validate_credit_card(card_number):
    p=r'^(?!.*(\d)(-?\1){3})[456]\d{3}(-?\d{4}){3}$'
    
    regex =re.compile(p)
    if regex.match(card_number):
        return "Valid"
    else:
        return "Invalid"
def main():
    N = int(input().strip())
    
    for _ in range(N):
        card_number = input().strip()
        result = validate_credit_card(card_number)
        print(result)
if __name__=="__main__":
    main()
