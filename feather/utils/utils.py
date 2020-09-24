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
