"""Write a stream of close approaches to CSV or to JSON.

This module exports two functions: `write_to_csv` and `write_to_json`, each of
which accept an `results` stream of close approaches and a path to which to
write the data.

These functions are invoked by the main module with the output of the `limit`
function and the filename supplied by the user at the command line. The file's
extension determines which of these functions is used.

You'll edit this file in Part 4.
"""
import csv
import json


def write_to_csv(results, filename):
    """Write an iterable of `CloseApproach` objects to a CSV file.

    The precise output specification is in `README.md`. Roughly, each output row
    corresponds to the information in a single close approach from the `results`
    stream and its associated near-Earth object.

    :param results: An iterable of `CloseApproach` objects.
    :param filename: A Path-like object pointing to where the data should be saved.
    """
    fieldnames = (
        'datetime_utc', 'distance_au', 'velocity_km_s',
        'designation', 'name', 'diameter_km', 'potentially_hazardous'
    )

    close_approaches = list(results)

    # Open a file in write mode and create a CSV writer
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # Write the headers to the CSV
        writer.writeheader()

        # Write each CloseApproach object to the CSV
        for ca in close_approaches:
            row = {
                'datetime_utc': ca.time_str,
                'distance_au': ca.distance,
                'velocity_km_s': ca.velocity,
                'designation': ca.neo.designation,
                'name': (ca.neo.name if ca.neo.name else ''),
                'diameter_km': (ca.neo.diameter if ca.neo.diameter else 'nan'),
                'potentially_hazardous': ca.neo.hazardous if ca.neo.hazardous else 'False'
                }
            writer.writerow(row)


def write_to_json(results, filename):
    """Write an iterable of `CloseApproach` objects to a JSON file.

    The precise output specification is in `README.md`. Roughly, the output is a
    list containing dictionaries, each mapping `CloseApproach` attributes to
    their values and the 'neo' key mapping to a dictionary of the associated
    NEO's attributes.

    :param results: An iterable of `CloseApproach` objects.
    :param filename: A Path-like object pointing to where the data should be saved.
    """
    # TODO: Write the results to a JSON file, following the specification in the instructions.

    close_approaches = list(results)

    # Open a file in write mode and create a JSON writer
    with open(filename, 'w') as jsonfile:
        # Write each CloseApproach object to the JSON
        for ca in close_approaches:
            row = {
                'datetime_utc': ca.time_str,
                'distance_au': ca.distance,
                'velocity_km_s': ca.velocity,
                'neo': {
                    'designation': ca.neo.designation,
                    'name': (ca.neo.name if ca.neo.name else ''),
                    'diameter_km': (ca.neo.diameter if ca.neo.diameter else 'nan'),
                    'potentially_hazardous': ca.neo.hazardous 
                    # 'potentially_hazardous': True if ca.neo.hazardous else False
                    }
                }
            json.dump(row, jsonfile, indent=2)

'''The `datetime_utc` value should be a string formatted with `datetime_to_str` from the `helpers` module; 
the `distance_au` and `velocity_km_s` values should be floats; the `designation` and `name` 
should be strings (if the `name` is missing, it must be the empty string); 
the `diameter_km` should be a float (if the `diameter_km` is missing, it should be the JSON value `NaN`, which Python's `json` 
loader successfully rehydrates as `float('nan')`); 
and `potentially_hazardous` should be a boolean (i.e. the JSON literals `false` or `true`, not the strings `'False'` nor `'True'`).'''