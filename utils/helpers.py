"""Optional formatting/display helpers for the video game recommender."""


def format_rating(rating):
    """Format a RAWG rating (0-5 float) as a star string, e.g. '4.2/5'."""
    if rating is None:
        return "N/A"
    return f"{rating:.1f}/5"


def format_release_date(released):
    """Return a human-friendly release date, falling back to 'Unreleased'."""
    return released or "Unreleased"


def genres_to_string(genres):
    """Join a list of genre names into a comma-separated string."""
    return ", ".join(genres) if genres else "N/A"
