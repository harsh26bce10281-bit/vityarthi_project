import os
import pickle


def load_inventory(filename):
    """Load inventory data from a pickle file."""
    if not os.path.exists(filename):
        return {}

    try:
        with open(filename, "rb") as file:
            data = pickle.load(file)

        if isinstance(data, dict):
            return data

    except (EOFError, pickle.PickleError, OSError):
        pass

    return {}


def save_inventory(filename, inventory):
    """Save inventory data to a pickle file."""
    directory = os.path.dirname(filename)

    if directory:
        os.makedirs(directory, exist_ok=True)

    with open(filename, "wb") as file:
        pickle.dump(inventory, file)
