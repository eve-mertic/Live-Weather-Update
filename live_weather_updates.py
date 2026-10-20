import requests

# Author: Eve Mertic :)

def weather(city):
    try:
        res = requests.get(
            f"https://wttr.in/{city}",
            params={"format": "j1"},
            headers={"User-Agent": "curl/8.0"},
            timeout=10,
        )
        res.raise_for_status()
        data = res.json()
    except (requests.RequestException, ValueError) as e:
        print("Could not get weather:", e)
        return

    def first(items, key="value", default="N/A"):

        try:
            return items[0][key]
        except (IndexError, KeyError, TypeError):
            return default

    area = data.get("nearest_area", [{}])[0]
    cur = data.get("current_condition", [{}])[0]

    location = ", ".join([
        first(area.get("areaName", [])),
        first(area.get("region", [])),
        first(area.get("country", [])),
    ])

    time = cur.get("localObsDateTime") or cur.get("observation_time", "N/A")

    print("Searching...\n")
    print(f"Location:    {location}")
    print(f"Time:        {time}")
    print(f"Conditions:  {first(cur.get('weatherDesc', []))}")
    print(f"Temperature: {cur.get('temp_F', 'N/A')}°F / {cur.get('temp_C', 'N/A')}°C")
    print(f"Feels like:  {cur.get('FeelsLikeF', 'N/A')}°F / {cur.get('FeelsLikeC', 'N/A')}°C")
    print(f"Humidity:    {cur.get('humidity', 'N/A')}%")
    print(f"Wind:        {cur.get('windspeedMiles', 'N/A')} mph {cur.get('winddir16Point', '')}")

weather(input("Enter city name: "))