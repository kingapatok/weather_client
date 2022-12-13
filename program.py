


def main():
    # Show the header
    show_header()

    # Get the location request
    location_text = input("Where do yuo want to weather report (e.g. Portland, US)? ")
    print(f"You selected {location_text}")

    # Convert plaintext over to data we can use ---- czemu zwraca none
    location = convert_plaintext_location(location_text)
    print(f"Location = {location}")

    # Get report from the API
    # Report the weather
    print('-----------------------')
    print('Hello from weather main')
    print('-----------------------')


def convert_plaintext_location(location_text):
    if not location_text or not location_text.strip():
        return None

    location_text = location_text.lower().strip()
    parts = location_text.split(',')
    print(parts)


def show_header():
    print('-------------------')
    print('  WEATHER CLIENT')
    print('-------------------')
    print()


if __name__ == '__main__':
    main()