import os

# Status
status_file = os.environ.get(
    "FEATHER_STATUS_FILE", "data/status/status.json")

# Map
map_file = os.environ.get(
    "FEATHER_MAP_FILE", "data/map/map.json")

# Dictionaries
action_dictionary_file = os.environ.get(
    "FEATHER_ACTION_DICTIONARY_FILE", "data/generated/action_dictionary.json")

# Combinations
dialog_combinations_file = os.environ.get(
    "FEATHER_DIALOG_COMBINATIONS_FILE", "data/generated/dialog_combinations.json")

move_combinations_file = os.environ.get(
    "FEATHER_MOVE_COMBINATIONS_FILE", "data/generated/move_combinations.json")

# Replacements
replacements_file = os.environ.get(
    "FEATHER_REPLACEMENTS_FILE", "data/generated/replacements.json")

# Paths
speech_path = os.environ.get(
    "FEATHER_SPEECH_PATH", "data/dialog/speech")

action_path = os.environ.get(
    "FEATHER_ACTION_PATH", "data/action")

# Introduction
intro_file = os.environ.get(
    "FEATHER_INTRO_FILE", "data/intro.json"
)