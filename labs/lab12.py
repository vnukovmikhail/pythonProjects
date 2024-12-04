class Country:
    def __init__(self, name, capital, continent, area, population):
        self.name = name
        self.capital = capital
        self.continent = continent
        self.area = area
        self.population = population

    def __str__(self):
        return f"{self.name} - capital: {self.capital}, continent: {self.continent}, area: {self.area}, population: {self.population}"

n = int(input("input country count: "))
countries = []

for _ in range(n):
    name = input("country's name: ")
    capital = input("country's capital: ")
    continent = input("country's continent: ")
    area = float(input("country's area: "))
    population = int(input("country's population: "))
    country = Country(name, capital, continent, area, population)
    countries.append(country)

# 1.
capital_input = input("Enter capital to search for country: ")
country_found = next((c for c in countries if c.capital.lower() == capital_input.lower()), None)
if country_found:
    print(f"a country with such a capital: {country_found.name}")
else:
    print("no country with such a capital was found.")

# 2.
largest_area_country = countries[0]
for country in countries:
    if country.area > largest_area_country.area:
        largest_area_country = country
print(f"country with the largest area: {largest_area_country.name}, continent: {largest_area_country.continent}, capital: {largest_area_country.capital}, area: {largest_area_country.area}")

# 3.
least_population_country = countries[0]
for country in countries:
    if country.population < least_population_country.population:
        least_population_country = country
print(f"country with the least population: {least_population_country.name}, capital: {least_population_country.capital}, population: {least_population_country.population}")
