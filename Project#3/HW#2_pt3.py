def read_original_date():
    # Prompt user for a date
    print("************************************************************")
    date = input("Enter a date in the form of MM/DD/YY or MM/DD/YYYY: ")
    print("************************************************************")
    return date

def break_original_date(date):
    # Split the date into parts and validate format
    try:
        date_result = date.split("/")
        # Check if input has exactly 3 parts
        if len(date_result) != 3:  
            # Raise error for invalid format
            raise ValueError  
        month, day, year = date_result
    except ValueError:
        # Print error message for invalid input
        print("Invalid date format. Please enter in MM/DD/YY or MM/DD/YYYY format.")
        return None, None, None  
    
    # Print the date components
    print(f"{date} is the original date")
    print(f"{month} is the month")
    print(f"{day} is the day")
    print(f"{year} is the year")
    return month, day, year

def print_date_3_ways(month, day, year):
    
    # Convert two-digit year to four-digit
    if len(year) == 2:
        year_full = f"20{year}"
    else:
        year_full = year
    
    # List of month names
    months = ["January" , "February" , "March" , "April" , "May" , "June" , "July" , "August" , "September" , "October" , "November" , "December"]
    
    # Get month name
    month_name = months[int(month) - 1]
    
    # Print in European format
    european_date = f"{day}-{month}-{year}"
    print(f"European way of printing: {european_date}")
    
    # Print in American format
    american_date = f"{month_name} {int(day)}, {year_full}"
    print(f"American way of printing: {american_date}")
    
    # Print in full format
    full_date = f"{month.zfill(2)}-{day.zfill(2)}-{year_full}"
    print(f"Full way of printing: {full_date}")

def main():
    # Main loop to process multiple dates
    while True:
        original_date = read_original_date()  
        if original_date.lower() == "quit": 
            print("Exiting program.")
            break
        # Split date
        month, day, year = break_original_date(original_date) 
        # Skip invalid dates
        if month is None: 
            continue
        # Print date in 3 formats
        print_date_3_ways(month, day, year) 

main()
