import os

# ------- Generated files

# Path for generated paths
generated_path = os.environ.get(
    "FEATHER_GENERATED_PATH", "data/generated")

# Map
generated_map_file = os.environ.get(
    "FEATHER_GENERATED_MAP_FILE", f"{generated_path}/map.json")

# Dictionaries
generated_action_file = os.environ.get(
    "FEATHER_GENERATED_ACTION_FILE", f"{generated_path}/actions.json")

generated_map_aliases_file = os.environ.get(
    "FEATHER_GENERATED_MAP_ALIASES_FILE", f"{generated_path}/map_aliases.json")

generated_dialog_file = os.environ.get(
    "FEATHER_GENERATED_DIALOG_FILE", f"{generated_path}/dialogs.json")

# Combinations
generated_dialog_combinations_file = os.environ.get(
    "FEATHER_GENERATED_DIALOG_COMBINATIONS_FILE",
    f"{generated_path}/dialog_combinations.json")

generated_move_combinations_file = os.environ.get(
    "FEATHER_GENERATED_MOVE_COMBINATIONS_FILE",
    f"{generated_path}/move_combinations.json")

# Replacements
generated_replacements_file = os.environ.get(
    "FEATHER_GENERATED_REPLACEMENTS_FILE", f"{generated_path}/replacements.json")

# ------- User files and paths

# Status
status_file = os.environ.get(
    "FEATHER_STATUS_FILE", "data/status/status.json")

# Word combinations
dialog_combinations_file = os.environ.get(
    "FEATHER_DIALOG_COMBINATIONS_FILE", "data/dialog/combinations.json")

move_combinations_file = os.environ.get(
    "FEATHER_MOVE_COMBINATIONS_FILE", "data/move/combinations.json")

# Word replacements
replacements_file = os.environ.get(
    "FEATHER_REPLACEMENTS_FILE", "data/replacements.json"
)

# Paths
speech_path = os.environ.get(
    "FEATHER_SPEECH_PATH", "data/dialog/speech")

action_path = os.environ.get(
    "FEATHER_ACTION_PATH", "data/action")

places_path = os.environ.get(
    "FEATHER_PLACES_PATH", "data/move/places")

map_path = os.environ.get(
    "FEATHER_MAP_PATH", "data/map")

# Introduction
intro_file = os.environ.get(
    "FEATHER_INTRO_FILE", "data/intro.json"
)
