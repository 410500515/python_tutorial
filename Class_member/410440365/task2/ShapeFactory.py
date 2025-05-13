from Shape import Square, Circle, EquilateralTriangle

# 工廠類別
class ShapeFactory:
    @staticmethod
    def create_shape(shape_type, side_length):
        if shape_type == 'Square':
            return Square(side_length)
        elif shape_type == 'Circle':
            return Circle(side_length)
        elif shape_type == 'EquilateralTriangle':
            return EquilateralTriangle(side_length)
        else:
            raise ValueError(f"Unknown shape type: {shape_type}")
