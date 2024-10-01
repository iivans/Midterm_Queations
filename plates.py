# Source: https://www.w3schools.com/python/python_regex.asp
# Source: https://docs.python.org/3/howto/regex.html

import re

class PlateValidator:

    def validate_new_mexico_plate(self, plate):        
        #New Mexico plates can have 5 to 7 characters.
        #Allowed characters: uppercase letters, digits, '+', apostrophe (’), dash (-), and Spanish Ñ.
        
        pattern = r"^[A-Z0-9+’Ñ-]{5,7}$"
        if not re.fullmatch(pattern, plate):
            raise ValueError("Invalid New Mexico plate")
        return True

    def validate_california_plate(self, plate):  
        #California plates must be between 5 and 7 characters.
        #Allowed characters: uppercase letters (excluding 'I', 'O', 'Q'), digits, and '+', but '+' can only appear once.
        #The first and third position can't contain 'I', 'O', or 'Q'.

        pattern = r"^[A-HJ-NPR-Z0-9][A-HJ-NPR-Z0-9+][A-HJ-NPR-Z0-9]{2,5}$"
        if not re.fullmatch(pattern, plate):
            raise ValueError("Invalid California plate")
        return True

def main():
    validator = PlateValidator()
    
    while True:
        try:
            # Prompt the user to enter the state and plate
            state = input("Enter State [NM or CA]: ").strip().upper()

            if state not in ["NM", "CA"]:
                raise ValueError("Invalid state. Please enter NM for New Mexico or CA for California.")

            plate = input("Enter Plate to Check: ").strip().upper()

            if state == "NM":
                validator.validate_new_mexico_plate(plate)
                print("Valid New Mexico plate.")
            elif state == "CA":
                validator.validate_california_plate(plate)
                print("Valid California plate.")

        except ValueError as e:
            print(f"Error: {e}")

        # Ask if the user wants to check another plate
        another = input("Do you want to check another plate? (y/n): ").strip().lower()
        if another != 'y':
            break


if __name__ == "__main__":
    main()
