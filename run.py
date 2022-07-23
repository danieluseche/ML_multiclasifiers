import sys
import numpy as np
import pandas as pd 

data_file = "diabetic_data.csv"

data = pd.read_csv(data_file, header = 0)

# A quien le da mas diabetes? 
# print('Razas:')
# races = set(data['race'])
# for race in races:
#     c = len(list(filter(lambda x: x == race, data['race'])))
#     print(f'{race}: {c}')
# print()
# A los blancos que tienen dinero para comprar chucherias

# print('sexo:')
# sexs = set(data['gender'])
# for sex in sexs:
#     c = len(list(filter(lambda x: x == sex, data['gender'])))
#     print(f'{sex}: {c}')

def print_problem():
    for col in data.columns[49:]:
        posible_values = set(data[col])
        print(f'- {col} {posible_values}')
        for value in posible_values:
            c = len(list(filter(lambda x: x == value, data[col])))
            print(f'  - {value}: {c}')
        print(80*'*')

def main(col):
    print()
    posible_values = set(data[col])
    print(f'- **{col}** {posible_values}')
    for value in posible_values:
        c = len(list(filter(lambda x: x == value, data[col])))
        print(f'  - {value}: {c}')
    print('---')

if __name__=='__main__':
    main(sys.argv[1])

