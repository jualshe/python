nested_list = [['HTML', 'Hypertext Markup Language forms the structure of webpages'],
               ['CSS' , 'Cascading Style Sheets give pages style'],
               ['Python', 'Python is a programming language'],
               ['Lists', 'Lists are a data structure that let you organize information']]

first_concept = nested_list[0]
first_title = first_concept[0]
first_description = first_concept[1]
print (nested_list[0][0])

#             Name    Capital  Populations (millions)
countries = [['China','Beijing',1350],
             ['India','Delhi',1210],
             ['Romania','Bucharest',21.],
             ['United States','Washington',307]]
india_capital=countries[1][1]
print india_capital

population_of_china = countries[0][2]
population_of_romania = countries[2][2]
multiple = population_of_china/population_of_romania

print multiple