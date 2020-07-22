import pandas as pd

CITY_DATA = {
    'chicago':'chicago.csv',
    'new york':'new_york_city.csv',
    'washington':'washington.csv'
}

CITY_TYPE = 'city'
TIME_TYPE = 'time'

ALL = 'all'
BOTH = 'both'
MONTH = 'month'
DAY = 'day'
NONE = 'none'
TIME_DATA = [BOTH, MONTH, DAY, NONE]


def check_input(input, type):
    valid = False
    cleaned_data = input.strip().lower()

    print(cleaned_data)
   
    if input:
        if type == CITY_TYPE:
            if cleaned_data in CITY_DATA.keys():
                valid = True
            else:
                print(f"It seems like you provided an invalid {type}. Please enter again.")
        else:
            if cleaned_data in TIME_DATA:
                valid = True
            else:
                print(f"It seems like you provided an invalid {type}. Please enter again.")
    else:
        print(f"It seems like you provided nothing for {type}. Please enter again.")

    check_result ={
        "valid": valid,
        "cleaned_data": cleaned_data
    }

    return check_result

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - pandas DataFrame containing city data filtered by month and day
    """
    
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df["Start Time"])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df["Start Time"].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name ()

    # filter by month if applicable
    if month != ALL:
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
    
        # filter by month to create the new dataframe
        df = df[df["month"] == month]

    # filter by day of week if applicable
    if day != ALL:
        # filter by day of week to create the new dataframe
        df = df[df["day_of_week"] == day.title()]
    
    return df
    

def month_mapper(month):
    months_map = {
        '1': 'January', '2': 'Feburay', '3': 'March', '4':'April', '5':'May', '6': 'June',
        '7': 'July', '8': 'August', '9': 'September', '10': 'October', '11':'November', '12': 'December'
    }
    return months_map[month]
    

# def day_mapper(day):
#     days_map = {
#         '0': 'Monday', '1': 'Tuesday', '2': 'Wednesday', '3':'Thursday',
#         '4':'Friday', '5': 'Saturday', '6':'Sunday'
#      }
#     return days_map[day]


def format_time(seconds):
    #return time.strftime("%H:%M:%S", time.gmtime(seconds))
    return pd.to_timedelta(seconds, unit='s')


def show_statistics(data):
    """
    Gather Descriptive Statistics of bike share information.

    Args:
        (pandas dataframe) data - raw data frame
    """

    #1 Popular times of travel (i.e., occurs most often in the start time)
    # most common month
    # most common day of week
    # most common hour of day
    print("\nCalculating Popular times of travel...")

    popular_month = data["month"].mode()[0]
    popular_month = month_mapper(str(popular_month))
    print("Popular Month: ", popular_month)

    popular_day = data["day_of_week"].mode()[0]
    print("Popular Day: ", popular_day)

    popular_hour = data["Start Time"].dt.hour.mode()[0]
    print("Popular Hour: ", popular_hour)


    #2 Popular stations and trip
    # most common start station
    # most common end station
    # most common trip from start to end (i.e., most frequent combination of start station and end station)
    print("\nCalculating Popular stations and trip...")

    popular_start_station = data["Start Station"].mode()[0]
    print("Popular Start Station: ", popular_start_station)

    popular_end_station = data["End Station"].mode()[0]
    print("Popular End Station: ", popular_end_station)

    # popular_trip = data.groupby(['Start Station', 'End Station']).size().reset_index(name='counts')
    popular_trip = (data['Start Station'] + " --> " + data['End Station']).mode()[0]
    print("Popular Trip: ", popular_trip)

    #3 Trip duration
    # total travel time
    # average travel time
    print("\nCalculating Trip duration...")

    summary_time = data['Trip Duration'].describe()
    total_travel_time = data["Trip Duration"].sum()

    print("Total Trip Duration: ", format_time(total_travel_time))
    print("Shortest Trip Duration: ", format_time(summary_time['min']))
    print("Longest Trip Duration: ", format_time(summary_time['max']))
    print("Average Trip Duration: ", format_time(summary_time['mean']))

    # 4 User info
    # counts of each user type
    # counts of each gender (only available for NYC and Chicago)
    # earliest, most recent, most common year of birth (only available for NYC and Chicago)
    print("\nCalculating User Info...")
    user_types = data.groupby(["User Type"])["User Type"].count()
    gender_types = data.groupby(["Gender"])["Gender"].count()
    summary_dob = data["Birth Year"].describe()

    print("User Group Information: ", user_types)
    print("Gender Type Information: ", gender_types)
    print("Most common Year of Birth: ", data["Birth Year"].mode())
    print("Earlist Year of Birth: ", summary_dob["min"])
    print("Recent Year of Birth: ", summary_dob["max"])


def main():
    print("***** Welcome to Bike Share Analysis Project *****")
    print("You can explore the statistics of bike share information across different city.")
    while True:
        city = input("\nWhich city would you like to explore? (Chicago, New York, Washington) : ")
        city_check_result = check_input(city, CITY_TYPE)

        if city_check_result["valid"]:
            print(f'ok check for {city_check_result["cleaned_data"]}')

            while True:
                time = input("\nWould you like to filter the data by month, day or both? Type \"none\" for no filter : ")
                time_check_result = check_input(time, TIME_TYPE)

                if time_check_result["valid"]:
                    day = ALL
                    month = ALL
                    
                    if time_check_result["cleaned_data"] == BOTH:
                        month = input("\nWhich month? January, Feburary, March, April, May or June ? : ").strip().lower()
                        day = input("\nWhich day? Sat, Sun, Mon, Tue, Wed, Thur, Fri ? : ").strip().lower()
                    elif time_check_result["cleaned_data"] == DAY:
                        day = input("\nWhich day? Sat, Sun, Mon, Tue, Wed, Thur, Fri ? : ").strip().lower()
                    elif time_check_result["cleaned_data"] == MONTH:
                        month = input("\nWhich month? January, Feburary, March, April, May or June ? : ").strip().lower()
                    
                    data = load_data(city, month, day)
                    show_statistics(data)

        user_choice = input("\nWould you like to explore again? (Press Enter to continue. Type \"no\" to exit): ")
        if user_choice.strip().lower() == 'no':
            break

if __name__ == "__main__":
    main()


    # data = load_data("chicago", ALL, ALL)
    # show_statistics(data)