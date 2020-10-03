import json

from feather.generators.build_data import (
    build_combinations,
    build_dictionary,
    build_replacements
)


def test_that_build_data_builds_replacements():
    build_combinations.__globals__[
        "generated_replacements_file"] = "tests/mock_data/generated/generated_replacements.json"

    build_replacements()

    with open("tests/mock_data/generated/generated_replacements.json", "r") as fp:
        replacements = json.load(fp)

    assert replacements == {
        "telephone": "phone",
        "school": "university",
        "college": "university",
    }


def test_that_build_data_builds_combinations():
    source_file = "tests/mock_data/combinations.json"
    dest_file = "tests/mock_data/generated/combinations.json"

    build_combinations(source_file, dest_file)

    with open("tests/mock_data/generated/combinations.json", "r") as fp:
        combinations = json.load(fp)

    assert combinations == {
        "combinations": [
            "get up to",
            "get up",
            "get to",
            "get"
            ]
        }
