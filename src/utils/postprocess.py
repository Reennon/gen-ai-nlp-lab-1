import ast
import json
import re


def clean_incomplete_entries(data: str) -> str:
    pattern = r"\{[^}]*\}"  # Matches everything enclosed in {}

    # Find all matches of complete entries
    complete_entries = re.findall(pattern, data)

    # Join back into a single cleaned string
    cleaned_data = ', '.join(complete_entries)

    return cleaned_data


def filter_unique_dicts(dict_list):
    seen = set()
    unique_dicts = []

    for d in dict_list:
        # Convert dictionary to a frozenset of its items (immutable and hashable)
        items = frozenset(d.items())
        if items not in seen:
            seen.add(items)
            unique_dicts.append(d)

    return unique_dicts


def join_split_dicts(entities):
    some_list = []
    for entity_list in entities:
        some_list.extend(entity_list)

    return some_list


def postprocess(entities):
    result_dict_list = []
    for e in entities:
        e = clean_incomplete_entries(e)
        e = ast.literal_eval(e)
        e = list(e)
        e = filter_unique_dicts(e)
        result_dict_list.extend(e)

    result_dict_list = filter_unique_dicts(result_dict_list)

    return result_dict_list