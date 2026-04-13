import csv

# Still trying to fix stats and write report
while True:
    with open("sa_census.csv") as f:
        reader = csv.DictReader(f)
        menu = 0
        print("-" * 30)
        menu = input(" View All | Filter by Language | Stats | Write Report | Exit :").title().strip()
        print("-" * 30)
        if menu == "View All":
            for row in reader:
                print(f"{row['name']}: population: {row['population']} Area_km2: {row['area_km2']} Main Language: {row['main_language']} GDP per capita: {row['gdp_per_capita']}")
        elif menu == "Filter By Language":
            while True:
                print("-" * 30)
                Lang_sel = input("Which language do you want to see? (Zulu,Afrikaans,Xhosa,Sotho,Sepedi,Swazi,Tswana): ").title().strip()
                if Lang_sel == "Zulu":
                    print("-" * 30)
                    language = [p for p in reader if p["main_language"] == "Zulu"]
                    for row in language:
                        print(f"{row['name']}: population: {row['population']} Area_km2: {row['area_km2']} Main Language: {row['main_language']} GDP per capita: {row['gdp_per_capita']}")
                    break
                elif Lang_sel == "Afrikaans":
                    print("-" * 30)
                    language = [p for p in reader if p["main_language"] == "Afrikaans"]
                    for row in language:
                        print(f"{row['name']}: population: {row['population']} Area_km2: {row['area_km2']} Main Language: {row['main_language']} GDP per capita: {row['gdp_per_capita']}")
                    break
                elif Lang_sel == "Xhosa":
                    print("-" * 30)
                    language = [p for p in reader if p["main_language"] == "Xhosa"]
                    for row in language:
                        print(f"{row['name']}: population: {row['population']} Area_km2: {row['area_km2']} Main Language: {row['main_language']} GDP per capita: {row['gdp_per_capita']}")
                    break
                elif Lang_sel == "Sotho":
                    print("-" * 30)
                    language = [p for p in reader if p["main_language"] == "Sotho"]
                    for row in language:
                        print(f"{row['name']}: population: {row['population']} Area_km2: {row['area_km2']} Main Language: {row['main_language']} GDP per capita: {row['gdp_per_capita']}")
                    break
                elif Lang_sel == "Sepedi":
                    print("-" * 30)
                    language = [p for p in reader if p["main_language"] == "Sepedi"]
                    for row in language:
                        print(f"{row['name']}: population: {row['population']} Area_km2: {row['area_km2']} Main Language: {row['main_language']} GDP per capita: {row['gdp_per_capita']}")
                    break
                elif Lang_sel == "Swazi":
                    print("-" * 30)
                    language = [p for p in reader if p["main_language"] == "Swazi"]
                    for row in language:
                        print(f"{row['name']}: population: {row['population']} Area_km2: {row['area_km2']} Main Language: {row['main_language']} GDP per capita: {row['gdp_per_capita']}")
                    break
                elif Lang_sel == "Tswana":
                    print("-" * 30)
                    language = [p for p in reader if p["main_language"] == "Tswana"]
                    for row in language:
                        print(f"{row['name']}: population: {row['population']} Area_km2: {row['area_km2']} Main Language: {row['main_language']} GDP per capita: {row['gdp_per_capita']}")
                    break
                else:
                    print("-" * 30)
                    print("It does not have that. please try again.")
        elif menu == "Stats":
            while True:
                total_pop = 0
                stat_type = input(" Total Population | Average Area | Most/Least populated province | Population Density Ranking").title().strip()
                if stat_type == "Total Population":
                    for row in reader:
                        total_pop += int(row["population"])
                    print("-" * 30)
                    print(f"Total population: {total_pop}")
                    break
                elif stat_type == "Average Area":
                    for row in reader:
                        total_pop += int(row["population"])
                        number_province = 9
                        average_pop = total_pop/number_province
                    print("-" * 30)
                    print(f"Average population: {round(average_pop,2)}")
                    break
                elif stat_type == "Most Populated Province" or "Least Populated Province":
                    for row in reader:
                        population_high = row["population"][0]
                        population_low = row["population"][0]
                        if row > population_high:
                            row = population_high
                        if row < population_low:
                            row = population_low
                        while True:
                            menu_2 = input("Confirm if you want the Most or Least").title().strip()
                            if menu_2 == "Most":
                                print(population_high)
                                break
                            elif menu_2 == "Least":
                                print(population_low)
                                break
                            else:
                                print("Invalid responses")
                elif stat_type == "Population Density Ranking":
                    for i, (name, d) in enumerate(["density_ranking"], 1):
                        print(f"  {i}. {name}: {d:.1f}/km²")
                        break
                else:
                    print("invalid input")
        elif menu == "Write Report":
            for row in reader:
                with open('output.csv', 'w', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerows(print(f"{row['name']}: population: {row['population']} Area_km2: {row['area_km2']} Main Language: {row['main_language']} GDP per capita: {row['gdp_per_capita']}"))
        elif menu == "Exit":
            print("Exitting...")
            break
        else:
            print("invalid response")