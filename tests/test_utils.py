import pytest

from feather.utils.utils import decompose_text


@pytest.mark.parametrize("text, text_with_var, expected", [
    [
        "say hello to Wendy",
        "say {speech} to {interlocutor}",
        {
            "speech": "hello",
            "interlocutor": "Wendy"
        }
    ],
    [
        "say Hi there!",
        "say {speech}",
        {
            "speech": "Hi there!",
        }
    ],
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
