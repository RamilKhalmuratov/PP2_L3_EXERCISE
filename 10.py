class MyShape:
    def __init__(self, color="blue", is_filled=True):
        self.color = color
        self.is_filled = is_filled

    def __str__(self):
        filled_status = "filled" if self.is_filled else "not filled"
        return f"MyShape(color={self.color}, is_filled={filled_status})"

    def getArea(self):
        return 0

# Example usage
shape = MyShape()
print(shape)
print("Area:", shape.getArea())

custom_shape = MyShape(color="red", is_filled=False)
print(custom_shape)
print("Area:", custom_shape.getArea())