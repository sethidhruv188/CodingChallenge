import re

# Function to validate if the input date is in correct format
def validate_date(date_str):
    # Define regex pattern for the two possible date formats
    regex1 = r"(\d{1,2})/(\d{1,2})/(\d{4})"
    regex2 = r"(\S+) (\d{1,2}), (\d{4})"

    # Check if input matches either format
    match1 = re.match(regex1, date_str)
    match2 = re.match(regex2, date_str)

    if match1:
        month, day, year = map(int, match1.groups())
        if 1 <= month <= 12 and 1 <= day <= 31:
            return True
    elif match2:
        month_str, day, year = match2.groups()
        month_dict = {
            "January": 1, "February": 2, "March": 3, "April": 4,
            "May": 5, "June": 6, "July": 7, "August": 8,
            "September": 9, "October": 10, "November": 11, "December": 12
        }
        if month_str in month_dict.keys():
            month = month_dict[month_str]
            if 1 <= int(day) <= 31:
                return True
    return False

# Function to convert date to ISO 8601 format
def convert_to_iso(date_str):
    # Define regex pattern for the two possible date formats
    regex1 = r"(\d{1,2})/(\d{1,2})/(\d{4})"
    regex2 = r"(\S+) (\d{1,2}), (\d{4})"

    # Check if input matches either format
    match1 = re.match(regex1, date_str)
    match2 = re.match(regex2, date_str)

    if match1:
        month, day, year = map(int, match1.groups())
        return f"{year:04d}-{month:02d}-{day:02d}"
    elif match2:
        month_str, day, year = match2.groups()
        month_dict = {
            "January": 1, "February": 2, "March": 3, "April": 4,
            "May": 5, "June": 6, "July": 7, "August": 8,
            "September": 9, "October": 10, "November": 11, "December": 12
        }
        month = month_dict[month_str]
        return f"{year}-{month:02d}-{int(day):02d}"

# Main program
def main():
    while True:
        date_input = input("Enter a date in month-day-year format (e.g., 9/8/1636 or September 8, 1636): ")
        if validate_date(date_input):
            iso_date = convert_to_iso(date_input)
            print(f"The date in ISO 8601 format is: {iso_date}")
            break
        else:
            print("Invalid date format. Please enter the date again.")

if __name__ == "__main__":
    main()
