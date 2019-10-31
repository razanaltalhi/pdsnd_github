import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data! Lets go!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input("Enter the name of the city to know more about it: ").lower()
    while (True):
        if(city == 'chicago' or city == 'new york city' or city == 'washington' ):
           break
        else:
            city= input("Please choose from the three cities chicago, new york city, washington: ").lower()
           # TO DO: get user input for month (all, january, february, ... , june)
    month = input("Enter a specific month or 'all' to display the data according to it: ").lower()
    while (True):
        if(month == 'january' or month =='february' or month =='march' or month =='april' or month =='may' or month =='june' or month =='all'):
           break
        else:
            month= input("Enter the correct month: ").lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("Enter a specific day to display the data according to it: ").lower()
    while (True):
        if(day == 'sunday' or day =='monday' or day =='tuseday' or day =='wednesday' or day =='thursday' or day =='friday' or day =='saturday'or day =='all'):
           break
        else:
            day= input("Enter the correct day: ").lower()


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
# load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    return df


def time_stats(df, month , day):
   """Displays statistics on the most frequent times of travel."""

   print('\nCalculating The Most Frequent Times of Travel...\n')
    # TO DO: display the most common month
   if(month == 'all'):
      popular_month = df['month'].mode()[0]
      print('Most Popular Start month:', popular_month)
    # TO DO: display the most common day of week
   if(day == 'all'):
      popular_day = df['day_of_week'].mode()[0]
      print('Most Popular Start day:', popular_day)
    # TO DO: display the most common start hour
   popular_hour = df['hour'].mode()[0]
   print('Most Popular Start Hour:', popular_hour)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start stationvalue_counts().idxmax()
    Start_Stations = df['Start Station'].mode()[0]
    print('Most Popular Start Station:', Start_Stations)

    # TO DO: display most commonly used end station
    End_Stations = df['End Station'].mode()[0]
    print('Most Popular End Station:', End_Stations)

    # TO DO: display most frequent combination of start station and end station trip
    most_common_start_end_station = df[['Start Station', 'End Station']].mode().loc[0]
    print('most frequent combination of start station and end station trip:'+ most_common_start_end_station[0] + " "+ "to" +" "+ most_common_start_end_station[1])

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print("Total travel time: ", df['Trip Duration'].sum() )

    # TO DO: display mean travel time
    print("Average of the travel time: ", df['Trip Duration'].mean() )


def user_stats(df):
  """Displays statistics on bikeshare users."""
    # TO DO: Display counts of user types
  print("The counts of user type :" , df['User Type'].value_counts())

  # TO DO: Display counts of gender
  print("The counts of each gender :" , df['Gender'].value_counts())

  # TO DO: Display earliest, most recent, and most common year of birth
  print("The most common year of birth:" , df['Birth Year'].value_counts().idxmax())
  print("The most recent birth year:", df['Birth Year'].max())
  print("The most earliest birth year:", df['Birth Year'].min())

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df, month, day)
        station_stats(df)
        Answer= input("Do you want more information about the trip duration:").lower()
        if(Answer == 'yes'):
            trip_duration_stats(df)
        Answer2= input("Do you want more information about the user stats:").lower()
        if(Answer == 'yes'):
            user_stats(df)


        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
if __name__ == "__main__":
 	main()
