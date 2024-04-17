import pandas as pd

#a
url = "https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/02_Filtering_%26_Sorting/Euro12/Euro_2012_stats_TEAM.csv"
df = pd.read_csv(url)

print("Данные успешно импортированы.")

#b
selected_columns = df[['Team', 'Yellow Cards', 'Red Cards']]
print(selected_columns)

#c
num_teams = df['Team'].nunique()
print("Количество команд, участвовавших в Euro2012:", num_teams)
#d
high_scorers = df[df['Goals'] > 6]
print("Команды, забившие более 6 голов:")
print(high_scorers[['Team', 'Goals']])