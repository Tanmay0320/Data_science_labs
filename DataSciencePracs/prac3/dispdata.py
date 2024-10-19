def read_csv_into_dict(filename):
    data_dict = {}
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if line:
                key, value = line.split(',')
                data_dict[key.strip()] = value.strip()
    return data_dict

def average_calories(data, start_date, end_date):
    total_calories = 0
    count = 0

    for date, calories in data.items():
        if start_date <= date <= end_date:
            total_calories += calories
            count += 1
    
    if count == 0:
        return None  
    else:
        average_calories = total_calories / count
        return average_calories
    
def standard_deviation(data, start_date, end_date):
    count = 0

    mean_calories = average_calories(data)
    
    sum_squared_diff = 0
    
    for date, calories in data.items():
        if start_date <= date <= end_date:
            sum_squared_diff += (calories - mean_calories) ** 2
    
    variance = sum_squared_diff / count
    
    standard_deviation = variance ** 0.5
    
    return standard_deviation

def display_dates_and_highest_calories(data_dict, start_date, end_date):
    aggregate_dict = {}
    
    for date, calories in data_dict.items():
        if start_date <= date <= end_date:
            if date in aggregate_dict:
                aggregate_dict[date] += calories
            else:
                aggregate_dict[date] = calories

    max_calories = 0
    max_calories_date = None
    for date, total_calories in aggregate_dict.items():
        if total_calories > max_calories:
            max_calories = total_calories
            max_calories_date = date

    if max_calories_date is not None:
        print(f"Date: {max_calories_date}, Highest Calories: {max_calories}")
        
def display_dates_and_highest_calories(data_dict, start_date, end_date):
    max_calories = 0
    max_calories_date = None

    for date in sorted(data_dict.keys()): 
        if start_date <= date <= end_date:
            calories = data_dict[date]
            print(f"Date: {date}, Calories: {calories}")

            if calories > max_calories:
                max_calories = calories
                max_calories_date = date
    
    if max_calories_date is not None:
        print(f"\nDate with the highest calories: {max_calories_date}, Calories: {max_calories}")