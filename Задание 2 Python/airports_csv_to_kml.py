import csv
import simplekml


def read_airports_csv(csv_path):
    """Функция считывает данные из csv файла и возвращает их в виде словаря."""

    airports_data = {}

    with open(csv_path, encoding='utf-8', errors='replace') as f:
        reader = csv.DictReader(f)

        for row in reader:
            airport = {
                'name': row['name'],
                'iata': row['iata'],
                'latitude': row['latitude'],
                'longitude': row['longitude'],
                'altitude': row['altitude'],
            }

            if row['country'] not in airports_data:
                airports_data[row['country']] = []
            airports_data[row['country']].append(airport)

    return airports_data


def save_airports_to_kml(airports_data, kml_path):
    """Сохраняет данные аэропортов в kml файл. """

    icon_url = 'http://maps.google.com/mapfiles/ms/micons/green.png'
    point_style = simplekml.Style()
    point_style.iconstyle.icon.href = icon_url

    kml = simplekml.Kml()

    for country, airports in sorted(airports_data.items()):
        folder = kml.newfolder(name=country)

        for airport in airports:
            point = folder.newpoint(
                name=airport['iata'],
                coords=[
                    (
                        airport['longitude'],
                        airport['latitude'],
                        airport['altitude']
                    )
                ],
                description=airport['name']
            )
            point.style = point_style

    kml.save(kml_path)


if __name__ == '__main__':
    airports_data = read_airports_csv('Python.csv')
    save_airports_to_kml(airports_data, 'airports.kml')
