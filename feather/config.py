import os


status_file = os.environ.get(
    "FEATHER_STATUS_FILE", "data/status/status.json")

map_file = os.environ.get(
    "FEATHER_MAP_FILE", "data/map/map.json")

action_file = os.environ.get(
    "FEATHER_ACTION_FILE", "data/generated/action_dictionary.json")

dialog_file = os.environ.get(
    "FEATHER_DIALOG_FILE", "data/generated/dialog_dictionary.json")

replacements_file = os.environ.get(
    "FEATHER_REPLACEMENTS_FILE", "data/generated/replacements.json")
