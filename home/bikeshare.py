import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
Months = ('january', 'february', 'march', 'april', 'may', 'june')
Weekdays = ('sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday',
            'saturday')

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
  
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
   
    # TO DO: get user input for month (all, january, february, ... , june)
   
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    
    while True:                
       
        # 1- inner while loop to get the valid city input
   
        while True:
            city = input("What cities do you want to search for: New York City, Chicago or Washington? Use commas to list the names.\n>").lower()
            validInputFlag = True
            
            if ',' not in city:
                if city.strip() in CITY_DATA.keys():
                    city = city.strip()
                    break;  
                else:
                    validInputFlag = False

            elif ',' in city:
                city = city.split(',')
                for index, item in enumerate(city):
                    if item.strip() not in CITY_DATA.keys():

                        validInputFlag = False
                        break;

                    else:
                        city[index] = item.strip()
           
            if not validInputFlag:
                print('Please enter valid city name !!!')
                continue;
            break;

        # 2- inner while loop to get the valid Months input
        while True:
            month = input("What months do you want to filter data on? Use commas to list the names or enter 'all' to get all months data.\n>").lower()
            validInputFlag = True
            
            if month == 'all':
                month = list(Months)
                break;

            elif ',' not in month:
                 if month in Months:
                    month = month.strip()
                    break;
                 else:
                    validInputFlag = False

            elif ',' in month:
                month = month.split(',')
                for index, item in enumerate(month):
                    if item.strip() not in Months:   
                        validInputFlag = False
                        break;       
                    else:
                        month[index] = item.strip()
           
            if not validInputFlag:
                  print('Please try again enter valid Month name !!!')
                  continue;    
                
            break;           
        
        # 3- inner while loop to get the valid Days input
        while True:
            
            day = input("What weekdays do you want to filter data on? Use commas to list the names or enter 'all' to get all day data.\n>").lower()
            validInputFlag = True
            
            if day == 'all':
                day = list(Weekdays)
                break;

            elif ',' not in day:
                if day in Weekdays:
                    day = day.strip()
                    break;
                else:
                    validInputFlag = False
            
            elif ',' in day:
                day = day.split(',')
                for index,item in enumerate(day):
                    if item.strip() not in Weekdays:
                        validInputFlag = False
                        break; 
                    else:
                        day[index]= item.strip()
                        
            if not validInputFlag:
                  print('Please try again enter valid Day name !!!')
                  continue;             
            break; 
            
            
        confFlag = input("\nPlease confirm that you would like to apply the following filter on the data."
                                  "\n\n Cityies: {}\n Months: {}\n Weekdays"
                                  ": {}\n\n [y] Yes\n [n] No\n\n>"
                                  .format(city, month, day))


        if confFlag == 'y' or 'yes' or 'Yes':
            break;
        else:
            print("ok, you can try again !")           
    print('-'*40)
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
        
    if type(city) is list:
            df = pd.concat(map(lambda city: pd.read_csv(CITY_DATA[city]), city),sort=True )            
            df = df.reindex(columns = ['City Name', 'Start Time', 'End Time', 'Trip Duration', 'Start Station',
                                       'End Station', 'User Type', 'Gender', 'Birth Year'])
    else:
            df = pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['Month'] = df['Start Time'].dt.month
    df['Weekday'] = df['Start Time'].dt.weekday_name
    df['Start Hour'] = df['Start Time'].dt.hour

    
    if type(month) is list:
        df = pd.concat(map(lambda month: df[df['Month'] == (Months.index(month)+1)], month))
    else:
        df = df[df['Month'] == (Months.index(month)+1)]


    if type(day) is list:
        df = pd.concat(map(lambda day: df[df['Weekday'] == (day.title())], day))
    else:
        df = df[df['Weekday'] == day.title()]   
        
   
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print('Most common month is :', df['Month'].mode()[0],'\n')
    
#pd.read.cxv
     
    # TO DO: display the most common day of week
    print('Most common day is :', df['Weekday'].mode()[0],'\n')


    # TO DO: display the most common start hour

    print('Most common Start Hour is :', df['Start Time'].mode()[0],'\n')

    
    print("\nThis took %s seconds." % (time.time() - start_time),'\n')
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('Most common Start Station is :', df['Start Station'].mode()[0],'\n')

    # TO DO: display most commonly used end station
    print('Most common End Station is :', df['End Station'].mode()[0],'\n')

    # TO DO: display most frequent combination of start station and end station trip
    df['Station combination'] = df['Start Station'] + ' ' + df['End Station'] 
    mostFreq = df['Station combination'].mode()[0]
    print('Most frequent combination of start station and end station tripis :', mostFreq,'\n')
    
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('The total travel time is: ',df['Trip Duration'].sum(), '\n')
        
    # TO DO: display mean travel time
    print('The mean travel time is: ', df['Trip Duration'].mean(), '\n')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
 #   userTypeCount = len(set(df['User Type']))
    print('Counts of user types is : ', df['User Type'].value_counts(), '\n')
    
    # TO DO: Display counts of gender
    try: 
       genderCount = df['Gender'].value_counts()
       print('Counts of Gender is : ', genderCount, '\n')

    except KeyError:
       print('No data found for the Gender')
    
    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        
        print('Earliest year of birth is: ',df['Birth Year'].min(),'\n')
        print('Most Recent year of birth is: ',df['Birth Year'].max(),'\n')
        print('Most Common year of birth is: ',df['Birth Year'].mode()[0],'\n')
    except KeyError:
        print('No data found for the Birth Year !')

    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    
def show_data(df):
      
    start_time = time.time()    
    start_loc = 0
    
    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n').lower()
    
    while (view_data == 'yes'):
        print(start_loc)
        print(df.iloc[start_loc:start_loc+5])
        start_loc += 5
        view_data = input("Do you wish to continue to show the next 5 rows?: please Enter yes or no\n").lower()
    
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
   
   

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        show_data(df)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
