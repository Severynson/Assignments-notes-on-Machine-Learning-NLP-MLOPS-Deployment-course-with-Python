def merge_dicts_with_overlapping_keys(dicts):
    res = {}
    for dictionary in dicts:
        for key, value in dictionary.items():
            if key in res:
                res[key] += value
            else:
                res[key] = value
    return res