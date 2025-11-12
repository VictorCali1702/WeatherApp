import requests

def get_weather(city):
	try:
		url = f'https://wttr.in/{city}?format=j1'
		response = requests.get(url)
		response.raise_for_status()
		data = response.json()

		# === Current Conditions ===
		current = data['current_condition'][0]
		temp = current['temp_C']
		feels_like = current['FeelsLikeC']
		humidity = current['humidity']
		desc = current['weatherDesc'][0]['value']

		print(f'\nCity: {city.capitalize()}')
		print(f'Temperature: {temp}°C')
		print(f'Perceived temperature: {feels_like}°C')
		print(f'Humidity: {humidity}%')
		print(f'Weather: {desc}\n')

		# === Weather Forecast for the next 3 days ===
		print("Weather Forecast for the next 3 days:")
		for day in data['weather'][:3]:
			date = day['date']
			avg_temp = day['avgtempC']
			min_temp = day['mintempC']
			max_temp = day['maxtempC']
			desc_day = day['hourly'][4]['weatherDesc'][0]['value']
			print(f'{date}: {desc_day} | {min_temp}°C - {max_temp}°C (average {avg_temp}°C)')
		print()

	except requests.exceptions.RequestException as e:
		print("Error connecting to API:", e)	
	except KeyError:
		print("Could not find information about temperature.")
	except ValueError:
		print("Error processing JSON response")

def enter_city():
	city = input("Enter your city to check the weather: ")
	get_weather(city)

while True:
	enter_city()
	again = input("Check another city? (yes/no): ").lower()
	if again != 'yes':
		print("\nThanks for checking the weather! ☀️")
		break
