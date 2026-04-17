import geometry_utils

print("Available shapes: circle, rectangle, triangle")
print("Available calculations: _area, _perimeter (e.g., circle_area)")

operations = {
    "circle_area": geometry_utils.circle_area,
    "circle_perimeter": geometry_utils.circle_perimeter,
    "rectangle_area": geometry_utils.rectangle_area,
    "rectangle_perimeter": geometry_utils.rectangle_perimeter,
    "triangle_area": geometry_utils.triangle_area,
}

operation = input("Enter the operation you want to perform: ").strip().lower()

if operation not in operations:
    print("Invalid operation.")
else:
    if "circle" in operation:
        radius = float(input("Enter radius: "))
        result = operations[operation](radius)

    elif "rectangle" in operation:
        width = float(input("Enter width: "))
        height = float(input("Enter height: "))
        result = operations[operation](width, height)

    elif "triangle" in operation:
        base = float(input("Enter base: "))
        height = float(input("Enter height: "))
        result = operations[operation](base, height)

    if result is not None:
        print(f"Result: {result}")