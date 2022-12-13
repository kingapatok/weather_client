def main():
    d = {
        'city': 'Portland',
        'state': 'ME',
        'details': ['Cold', 'Snowy', 'Winter']
    }
    print(d)
    print(d.get('country', 'USA'))
    d['country'] = 'AU'
    print(d.get('country', 'USA'))
    print(d)

    p = dict(weather={
        "description": "mist",
        "category": "Mist"},
        wind={
        "speed": 3.0,
        "deg": 75},
        units="imperial",
        forecast={
        "temp": 40.59,
        "feels_like": 39.04,
        "pressure": 1024,
        "humidity": 87,
        "low": 36,
        "high": 44},
        location={
        "city": "Portland",
        "state": "OR",
        "country": "US"},
        rate_limiting={
        "unique_lookups_remaining": 47,
        "lookup_reset_window": "1 hour"})

    print(p.get('forecast').get('temp'))


if __name__ == '__main__':
    main()