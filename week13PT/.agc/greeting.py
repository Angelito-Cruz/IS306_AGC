def make_greeting(name):
    name = name.strip()

    if not name:
        raise ValueError("Name cannot be empty")

    return f"Hello, {name}!"