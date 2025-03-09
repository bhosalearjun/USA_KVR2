def greet(name, *messages):
    for msg in messages:
        print(f"{name}: {msg}")

greet("Alice", "Hello", "How are you?", "Goodbye!")
