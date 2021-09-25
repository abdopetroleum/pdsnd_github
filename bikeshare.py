import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}
MONTH_DATA = {'january': 1,
              'february': 2,
              'march': 3,
              'april': 4,
              'may': 5,
              'june': 6
              }
DAY_DATA = ('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday')
available=False
# asking user to filter for day , moth, both or none
choices = ['month', 'day', 'both', 'none']


def take_user_choice():
    print('would you like to filter for month , day , both or none')
    user_choice = input().lower()
    if user_choice not in choices:
        print("Improper choice")
        return take_user_choice()
    else:
        return user_choice


# function to handle city filter
def filter_for_city():
    city = ''
    print("Would you like to see the data for Chicago, New York City ,Washington")
    city = input().lower()
    if city not in CITY_DATA.keys():
        print("Please choose a valid city.")
        return filter_for_city()
    else:
        return city


# function to handle month filter

def filter_for_month():
    month = ''
    print("Choose a month from January to June")
    month = input().lower()
    if month not in MONTH_DATA.keys():
        print("Please choose a valid month.")
        return filter_for_month()
    else:
        return month


# function to handle day filter

def filter_for_day():
    day = ''
    print("Type the name of the day")
    day = input().lower()
    if day not in DAY_DATA:
        print("Please choose a valid day.")
        return filter_for_day()
    else:
        return day


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Welcome sir.')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = filter_for_city()
    # TO DO: get user input for month (all, january, february, ... , june
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    # asking user to filter for day , moth, both or none
    day = 'none'
    month = 'none'
    user_choice = take_user_choice()
    # month case
    if user_choice == choices[0]:
        month = filter_for_month()
    # day case
    elif user_choice == choices[1]:
        day = filter_for_day()
    elif user_choice == choices[2]:
        month = filter_for_month()
        day = filter_for_day()

    print('-' * 40)
    # print(city,month,day)
    return city, month, day


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
    # drop first column
    df = df.iloc[:, 1:]
    # Drop end time column
    df = df.drop('End Time', axis=1)
    # cast Start time from string to date
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Create month colum of the start time
    df['Month'] = df['Start Time'].dt.month
    # Create day colum of the start time
    df['Day'] = (df['Start Time'].dt.day_name())

    # Create hour colum of the start time
    df['Hour'] = df['Start Time'].dt.hour
    if month != 'none':
        month = MONTH_DATA[month]
        df = df[df['Month'] == month]
    if day != 'none':
        df = df[df['Day'] == day.capitalize()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print(f"The most common month is {df['Month'].mode().values}")

    # TO DO: display the most common day of week
    print(f"The most common day is {df['Day'].mode().values}")

    # TO DO: display the most common start hour
    print(f"The most common start hour is {df['Hour'].mode().values}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print(f"The most common Start station is {df['Start Station'].mode().values}")

    # TO DO: display most commonly used end station
    print(f"The most common end station is {df['End Station'].mode().values}")

    # TO DO: display most frequent combination of start station and end station trip

    print(f"The most common trip is  {df[['Start Station', 'End Station']].dropna().mode().values}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print(f"The total drive time is {df['Trip Duration'].sum()} second")

    # TO DO: display mean travel time
    print(f"The total drive time is {df['Trip Duration'].mean()} second")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print(f"Count of user types:\n{df['User Type'].value_counts()}")

    if available:
        # TO DO: Display counts of gender
        print(f"Count of user Gender :\n{df['Gender'].value_counts()}")
        # TO DO: Display earliest, most recent, and most common year of birth
        print(f"The earliest year of birth:{df['Birth Year'].min()}")

        print(f"The most recent year of birth:{df['Birth Year'].max()}")

        print(f"The earliest year of birth:{df['Birth Year'].mode()}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def see_five_rows(df,iterator):
    restart = input('\nWould you like to see 5 lines of data? Enter yes or no.\n')
    if restart.lower() == 'yes':
        print(df.iloc[iterator:iterator + 5])
        iterator += 5
        see_five_rows(df,iterator)
# Assure that user enter a valid response to know if he wantsto continue or not
def asking_for_continuing():
    restart = input('\nWould you like to restart? Enter yes or no.\n')
    if restart.lower() != 'yes' and restart.lower()!='no':
        print("Please enter a valid answer")
        restart=asking_for_continuing()
    return restart

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        available = False
        if city != "washington":
            available = True
        user_stats(df)
        i = 0
        see_five_rows(df,0)
        restart=asking_for_continuing()
        if restart.lower()!='yes':
            break


if __name__ == "__main__":
    main()