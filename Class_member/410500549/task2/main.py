from ShapeFactory import ShapeFactory

shape = ShapeFactory.create_shape('Circle', 5)
print(f"面積: {shape.get_area()}")
print(f"圓周長: {shape.get_circumference()}")
