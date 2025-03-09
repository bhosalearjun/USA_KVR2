def example(a, b=10, *args, **kwargs):
    print(f"Positional: {a}, Default: {b}, Args: {args}, Kwargs: {kwargs}")

example(5, 20, 30, 40, x=50, y=60)
