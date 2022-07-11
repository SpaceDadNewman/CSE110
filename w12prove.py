
#variables
minimum = 1000
maximum = 0
count = 0
product = 0
spec_min = 1000
spec_max = 0
country_product = 0
other_count = 0
country_max = 0
country_min = 1000

input_year = int(input('Enter the year of interest: '))
input_country = input('Enter a country of interest: ')
with open("life-expectancy.csv") as life_file:
    line = life_file.readline()
    next(life_file, None)  # skip the headers
    for line in life_file:
        line_list = line.strip().split(',')
        country = line_list[0]
        country_code = line_list[1]
        year = int(line_list[2])
        expectancy = float(line_list[3])
        #max
        if expectancy > maximum:
            maximum = expectancy
            maximum_country = country
            maximum_year = year
        #min
        if expectancy < minimum:
            minimum = expectancy
            minimum_country = country
            minimum_year = year
        #max and min for a specified year
        if year == input_year:
            product += expectancy
            count += 1
            average = product / count
            #max
            if expectancy > spec_max:
                spec_max = expectancy
                spec_max_country = country
            #min
            if expectancy < spec_min:
                spec_min = expectancy
                spec_min_country = country

        #max and min for a specified country
        if country == input_country:
            country_product += expectancy
            other_count += 1
            country_average = country_product / other_count
            #max
            if expectancy > country_max:
                country_max = expectancy
            #min
            if expectancy < country_min:
                country_min = expectancy


    print(f'\nThe overall max life expectancy is: {maximum} from {maximum_country} in {maximum_year}')
    print(f'The overall min life expectancy is: {minimum} from {minimum_country} in {minimum_year}\n')
    print(f'For the year {input_year}:')
    print(f'The average life expectancy across all countries was {"{:.2f}".format(average)}')
    print(f'The max life expectancy was in {spec_max_country} with {spec_max}')
    print(f'The min life expectancy was in {spec_min_country} with {spec_min}')
    print(f'\nFor {input_country}:')
    print(f'The average life expectancy is {"{:.2f}".format(country_average)}, the min life expectancy is {country_min} and max life expectancy is {country_max}')