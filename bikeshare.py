import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

cities =["chicago","new york city","washington","all"]
months = ["january","february","march","april","may","june","all"]
days = ["sunday","monday","tuesday","wednesday","thursday","friday","saturday","all"]

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    print('Please choose a city from ( Chicago, New York City, Washington ) ')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = str(input()).lower()
    while True:
        if city not in cities:
            print("invalid entry,please try again")
            city = str(input()).lower()
            continue
        else: 
            break
      
    # TO DO: get user input for month (all, january, february, ... , june)
    print('Please choose a month from ("January","February","March","April","May","June" ) or type "all" for no filters')
    month=str(input()).lower()
    while True:
        if month not in months:
            print("invalid entry,please try again")
            month = str(input()).lower()
            continue
        else: 
            break
    
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    print('Please choose a day from ("Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday" ) or type "all" for no filters')
    day=str(input()).lower()
    while True:
        if day not in days:
            print("invalid entry,please try again")
            day = str(input()).lower()
            continue
        else: 
            break

    print('-'*40)
    return city,month,day

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    df["Start Time"] = pd.to_datetime(df["Start Time"])
    df["month"] = df["Start Time"].dt.month
    df["day_of_week"] = df["Start Time"].dt.weekday_name
    if month != "all":
        month =months.index(month)+1
        df = df[df["month"] == month]
    if day != "all":
        df = df[df["day_of_week"] == day.title()]
    return df

def show_data(df):
    """ This function takes the dataframe from load_data function as an input and asks the user 
        if he wants to see the next rows of data or not.
        
        Args:
        df : the data frame returned from load_data.
        
        Outcome:
        The function prints the raw data based on the filters if the user 
        applied any, 5 rows at a time.
        """  
    rows=0
    while rows < df.shape[0]:
        show_row= str(input(" Do you want to see next 5 rows of data?\n")).lower()
        if show_row != "yes" or  rows > df.shape[0]:
                      break
        else:
                     
                     n= df[rows:rows+5]
                     rows+=5
                     print(n)
                    
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print("Most Common Month: ",df["month"].mode()[0])

    # TO DO: display the most common day of week
    print("Most Common Day of Week: ",df["day_of_week"].mode()[0])

    # TO DO: display the most common start hour
    df["hour"]= df["Start Time"].dt.hour
    print("Most Common Start Hour : ",df["hour"].mode()[0])
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("Most Used Start Station: ",df["Start Station"].mode()[0])

    # TO DO: display most commonly used end station
    print("Most Used End Station: ",df["End Station"].mode()[0])

    # TO DO: display most frequent combination of start station and end station trip
    df["Trip"] = df["Start Station"] + " TO " + df["End Station"]
    print("Most Frequent Trip : ",df["Trip"].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print("Total Travel Time: ",df["Trip Duration"].count()/3600," Hours")

    # TO DO: display mean travel time
    print("Average Travel Time: ",df["Trip Duration"].mean()/60," Minutes")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print("User Types Breakdown:\n",df["User Type"].value_counts())

    # TO DO: Display counts of gender    
    try:
     print("User Gender Breakdown:\n",df["Gender"].value_counts())
    except:
     print("No Gender Data For This City")
    

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        print("Earliest Year of Birth: ",df["Birth Year"].min())
        print("Most recent Year of Birth: ",df["Birth Year"].max())
        print("Most Common Year of Birth: ",df["Birth Year"].mode()[0])
    except:
        print("No Age Data For This City")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        show_data(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
