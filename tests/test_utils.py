import pytest

from feather.utils.utils import (
    choose_best_decomposition,
    decompose_text,
    remove_punctuation
)


@pytest.mark.parametrize("text, text_with_var, expected", [
    [
        "say hello to Wendy", "say {speech} to {interlocutor}",
        {"speech": "hello", "interlocutor": "Wendy"}
    ],
    [
        "say Hi there!", "say {speech}",
        {"speech": "Hi there!"}
    ],
    [
        "say \"Hi there!\"", "say \"{speech}\"",
        {"speech": "Hi there!"}
    ],
    [
        "say hello to Wendy", "say to {interlocutor} {speech}",
        None
    ]
])
def test_that_decompose_text_returns_correct_dictionary(
    text, text_with_var, expected
        ):
    assert decompose_text(text, text_with_var) == expected


def test_that_decompose_text_raises_on_bad_variables():
    text = "say hello to Wendy"
    text_with_var = "say {*$`} to {interlocutor}"

    with pytest.raises(AssertionError):
        decompose_text(text, text_with_var)


@pytest.mark.parametrize("text, texts, expected", [
    [
        "say hello to Wendy", [
            "say {speech} to {interlocutor}",
            "say {speech}",
            "say to {interlocutor} {speech}"
        ],
        {"speech": "hello", "interlocutor": "Wendy"}
    ],
    [
        "say Hi there!", [
            "say {speech}",
            "say to {interlocutor} that {speech}"
        ],
        {"speech": "Hi there!"}
    ],
    [
        "say \"Hi there!\"", [
            "say {speech}",
            "say \"{speech}\""
        ],
        {"speech": "Hi there!"}
    ],
    [
        "say to Wendy that she rocks", [
            "say {speech}",
            "say to {interlocutor} {speech}",
            "say to {interlocutor} that {speech}"
        ],
        {"speech": "she rocks", "interlocutor": "Wendy"}
    ],
    [
        "not a dialog", ["say {speech}"], {}
    ]
])
def test_that_best_decomposition_is_choosen(
    text, texts, expected
        ):
    assert choose_best_decomposition(text, texts) == expected


def test_that_punctuation_is_removed_from_text():
    text = "?hello, my! \"dear\" friend;."

    assert remove_punctuation(text) == "hello my dear friend"