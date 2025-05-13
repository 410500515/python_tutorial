from shape import Square, Circle, EquilateralTriangle

class ShapeFactory:
    @staticmethod
    def create_shape(shape_type, side):
        shape_type = shape_type.lower()
        if shape_type == 'square':
            return Square(side)
        elif shape_type == 'circle':
            return Circle(side)
        elif shape_type == 'equilateraltriangle':
            return EquilateralTriangle(side)
        else:
            raise ValueError(f"Unknown shape type: {shape_type}")

