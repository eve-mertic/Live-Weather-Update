# Weather CLI

A tiny Python script that prints the current weather for any city, using the free [wttr.in](https://wttr.in) service. No API key needed.

## Requirements

- Python 3.6+
- `requests`

```bash
pip install requests
```

## Usage

```bash
python weather.py
```

```
Enter city name: Columbus
```

The script shows location, local time, conditions, temperature (°F/°C), feels-like temperature, humidity, and wind.

## Notes

- Network errors, timeouts (10 s), and bad responses are caught and reported as `Could not get weather: ...`.
- Missing fields in the response display as `N/A`.
- Requires an internet connection and depends on wttr.in being available.

## Author

Eve Mertic
