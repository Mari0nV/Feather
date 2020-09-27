import json
from jsonschema import validate, exceptions
import os

from feather.config import (
    action_path,
    places_path,
    speech_path
)


def validate_file(schema, filepath):
    with open(filepath, "r") as fp:
        action = json.load(fp)
        
    try:
        validate(
            instance=action,
            schema=schema
        )
        print(f"    {filepath.split('/')[-1]} --> OK")
    except exceptions.ValidationError as e:
        print(f"    {filepath.split('/')[-1]} --> NOK")
        raise(e)



def validate_data():
    # Opening json schemas
    with open("json_validator/action_schema.json", "r") as fp:
        action_schema = json.load(fp)
    
    with open("json_validator/places_schema.json", "r") as fp:
        places_schema = json.load(fp)
    
    # Validating data json files
    print("\nValidating action data files...")
    for filename in os.listdir(action_path):
        validate_file(action_schema, f"{action_path}/{filename}")

    print("\nValidating speech data files...")
    for filename in os.listdir(speech_path):
        validate_file(action_schema, f"{speech_path}/{filename}")

    print("\nValidating places data files...")
    for filename in os.listdir(places_path):
        validate_file(places_schema, f"{places_path}/{filename}")


if __name__ == '__main__':
    validate_data()