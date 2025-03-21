# Python OOP Project

This project demonstrates the principles of Object-Oriented Programming (OOP) in Python through the creation of various classes representing real-world entities. The project includes classes for a `Smartphone`, `Vehicle`, and `Plane`, showcasing concepts such as encapsulation, inheritance, and polymorphism.

## Project Structure

```
python-oop-project
├── src
│   ├── entities
│   │   ├── __init__.py
│   │   ├── smartphone.py
│   │   ├── vehicle.py
│   │   └── plane.py
│   ├── main.py
└── README.md
```

## Classes Overview

### 1. `Smartphone`
- **Attributes**: 
  - `brand`: The brand of the smartphone.
  - `model`: The model of the smartphone.
  - `battery_life`: The battery life of the smartphone in hours.
- **Methods**:
  - `make_call()`: Simulates making a call.
  - `get_specs()`: Returns the specifications of the smartphone.

### 2. `Vehicle`
- **Attributes**:
  - `type`: The type of vehicle (e.g., car, bike).
- **Methods**:
  - `move()`: An abstract method that must be implemented by subclasses.

### 3. `Plane`
- Inherits from `Vehicle`.
- Implements the `move()` method to print "Flying" ✈️, demonstrating polymorphism.

## Running the Program

To run the program, navigate to the `src` directory and execute the `main.py` file. This will create instances of the `Smartphone` and `Plane`, showcasing their attributes and methods.

```bash
cd src
python main.py
```

## Conclusion

This project serves as a practical example of how to model real-world entities using OOP principles in Python. It highlights the importance of encapsulation, inheritance, and polymorphism in creating flexible and maintainable code.
