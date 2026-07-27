def remove_duplicates(List):
    """Removes duplicates from a list while preserving the order."""
    seen = set()
    return [x for x in List if not (x in seen or seen.add(x))]

def sort_list(List):
    """Sorts a list in ascending order."""
    return sorted(List)