import requests
import os

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
		wind = current['windspeedKmph']
		desc = current['weatherDesc'][0]['value']

		# Emoji for weather
		emoji = ''
		if 'rain' in desc.lower():
			emoji = '🌧️'
		elif 'cloud' in desc.lower():
			emoji = '☁️'
		elif 'sun' in desc.lower():
			emoji = '☀️'
		elif 'snow' in desc.lower():
			emoji = '❄️'

		print(f'\n🌇City: {city.capitalize()}')
		print(f'🌡️ Temperature: {temp}°C (Perceived temperature {feels_like}°C)')
		print(f'💧 Humidity: {humidity}%')
		print(f'💨 Wind: {wind} km/h')
		print(f'🌦️ Weather: {desc} {emoji}\n')

		# === The Weather Forecast for the next 3 days ===
		print("📅 Weather Forecast for the next 3 days:")
		for day in data['weather'][:3]:
			date = day['date']
			avg_temp = day['avgtempC']
			min_temp = day['mintempC']
			max_temp = day['maxtempC']
			desc_day = day['hourly'][4]['weatherDesc'][0]['value']
			emoji_day = ''
			if 'rain' in desc_day.lower():
				emoji_day = '🌧️'
			elif 'cloud' in desc_day.lower():
				emoji_day = '☁️'
			elif 'sun' in desc_day.lower() or 'clear' in desc_day.lower():
				emoji_day = '☀️'
			elif 'snow' in desc_day.lower():
				emoji_day = '❄️'

			print(f'📅 {date}: {desc_day} | 🌡️ {min_temp}°C - {max_temp}°C (average {avg_temp}°C)')
		print()

		# === Saving the report to a file ===
		filename = f'weather_{city}.txt'
		with open(filename, 'w', encoding='utf-8') as f:
			f.write(f'Weather for {city.capitalize()}:\n')
			f.write(f'🌡️ Temperature: {temp}°C (Perceived temperature {feels_like}°C)\n')
			f.write(f'💧 Humidity: {humidity}%\n')
			f.write(f'💨 Wind: {wind} km/h\n')
			f.write(f'🌦️ Weather: {desc} {emoji}\n\n')
			f.write('📅 The Weather Forecast for the next 3 days:\n')
			for day in data['weather'][:3]:
				date = day['date']
				avg_temp = day['avgtempC']
				min_temp = day['mintempC']
				max_temp = day['maxtempC']
				desc_day = day['hourly'][4]['weatherDesc'][0]['value']
				f.write(f'📅 {date}: {desc_day} | 🌡️ {min_temp}°C - {max_temp}°C (average {avg_temp}°C)\n')

		print(f'📁 The report was saved to: {filename}')


	except requests.exceptions.RequestException as e:
		print("Error connecting to API:", e)	
	except KeyError:
		print("Could not find information about temperature.")
	except ValueError:
		print("Error processing JSON response")

# Interactive Menu
def menu():
	while True:
		print('\n=== The Weather App ===')
		print('1. Check the weather in your City.')
		print('2. Exit')
		choice = input("Choose the choice (1/2): ")

		if choice == '1':
			city = input("Enter your city to check the weather: ")
			get_weather(city)
		elif choice == '2':
			print('\nThanks for using the App! ☀️')
			return
		else:
			print("Invalid Option. Try again ☀️")

if __name__ == "__main__":
	menu()