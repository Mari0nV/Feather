import re


def decompose_text(text, text_with_var):
    """
        Returns the values of variables inside text_with_var retrieved from text, in
        the form of a dictionary.
        Example:
            if text = "say hello there to Wendy" and
               text_with_var = "say {speech} to {interlocutor}",
            the return value will be:
            {
                "speech": "hello there",
                "interlocutor": "Wendy"
            }
        If no mapping is possible, this function returns None
    """
    variables = re.findall('{([^}]+)}', text_with_var)
    assert all(var.isidentifier() for var in variables)

    for variable in variables:
        text_with_var = text_with_var.replace('{' + variable + '}', f'(?P<{variable}>.*)')

    matches = re.match(text_with_var, text)

    if matches:
        return matches.groupdict()


def choose_best_decomposition(text, texts):
    """
        In a group of texts containing variables into brackets, this function chooses
        the best decomposition for a normal text, and returns it.
        Example:
            if text = "say hello to Wendy" and
               texts = ["say {speech} to {interlocutor}, "say {speech}],
            the return value will be:
            {
                "speech": "hello there",
                "interlocutor": "Wendy"
            }
    """
    final_match = {
        "match": {},
        "text_with_var": ""
    }
    for text_with_var in texts:
        match = decompose_text(text, text_with_var)
        if match:
            if len(final_match) < len(match):
                final_match["match"] = match
                final_match["text_with_var"] = text_with_var
            elif re.sub('{([^}]+)}', '', text_with_var) > \
                    re.sub('{([^}]+)}', '', final_match["text_with_var"]):
                final_match["match"] = match
                final_match["text_with_var"] = text_with_var

    return final_match["match"]


def remove_punctuation(text):
    punctuation = ["\"", ".", "?", "!"]

    return text.strip("".join(punctuation))
