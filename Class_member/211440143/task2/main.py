from shapefactory import ShapeFactory

if __name__ == "__main__":
    factory = ShapeFactory()

    square = factory.create_shape('Square', 5)
    print("建立的形狀:", square)
    print("[Square] area:", square.get_area())
    print("[Square] perimeter:", square.get_perimeter())

    circle = factory.create_shape('Circle', 2.5)
    print("建立的形狀:", circle)
    print("[Circle] area:", circle.get_area())
    print("[Circle] circumference:", circle.get_circumference())

    triangle = factory.create_shape('EquilateralTriangle', 4)
    print("建立的形狀:", triangle)
    print("[Triangle] area:", triangle.get_area())
    print("[Triangle] height:", triangle.get_height())
    print("[Triangle] perimeter:", triangle.get_perimeter())
