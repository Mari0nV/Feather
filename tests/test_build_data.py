import json
from mock import call
import os

from feather.generators.build_data import (
    build_combinations,
    build_data,
    build_dictionary,
    build_replacements
)


def test_that_build_data_builds_all(mocker):
    mock_build_dictionary = mocker.Mock()
    mock_build_combinations = mocker.Mock()
    mock_build_replacements = mocker.Mock()
    mock_build_map_data = mocker.Mock()

    mocker.patch(
        "feather.generators.build_data.build_dictionary",
        mock_build_dictionary)
    mocker.patch(
        "feather.generators.build_data.build_combinations",
        mock_build_combinations)
    mocker.patch(
        "feather.generators.build_data.build_replacements",
        mock_build_replacements)
    mocker.patch(
        "feather.generators.build_data.build_map_data",
        mock_build_map_data)

    build_data()

    mock_build_replacements.assert_called_once()
    mock_build_map_data.assert_called_once()

    mock_build_combinations.assert_has_calls([
        call(
            os.environ["FEATHER_MOVE_COMBINATIONS_FILE"],
            os.environ["FEATHER_GENERATED_MOVE_COMBINATIONS_FILE"]),
        call(
            os.environ["FEATHER_DIALOG_COMBINATIONS_FILE"],
            os.environ["FEATHER_GENERATED_DIALOG_COMBINATIONS_FILE"])])

    mock_build_dictionary.assert_has_calls([
        call(
            ["tests/mock_data/speech/hello.json"],
            os.environ["FEATHER_GENERATED_DIALOG_FILE"]),
        call(
            ["tests/mock_data/action/action.json",
             "tests/mock_data/action/action2.json"],
            os.environ["FEATHER_GENERATED_ACTION_FILE"])])


def test_that_build_data_builds_replacements(generated_folder):
    build_combinations.__globals__[
        "generated_replacements_file"] = \
            "tests/mock_data/generated/generated_replacements.json"

    build_replacements()

    with open("tests/mock_data/generated/generated_replacements.json", "r") as fp:
        replacements = json.load(fp)

    assert replacements == {
        "telephone": "phone",
        "school": "university",
        "college": "university",
    }


def test_that_build_data_builds_combinations(generated_folder):
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


def test_that_build_data_builds_dictionary(generated_folder):
    source_files = [
        "tests/mock_data/action/action.json",
        "tests/mock_data/action/action2.json"]
    dest_file = "tests/mock_data/generated/actions.json"

    build_dictionary(source_files, dest_file)

    with open("tests/mock_data/generated/actions.json", "r") as fp:
        dictionary = json.load(fp)

    assert dictionary == {
        "make action": "action",
        "do action": "action",
        "make second action": "action2",
        "do second action": "action2"
    }
