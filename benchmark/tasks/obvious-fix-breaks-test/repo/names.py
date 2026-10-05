def split_name(full_name):
    """Split a full name into (first_name, last_name)."""
    parts = full_name.split(" ", 1)
    if len(parts) == 1:
        return parts[0], ""
    return parts[0], parts[1]
