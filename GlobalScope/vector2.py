from dataclasses import dataclass
from math import sqrt, atan2, degrees


@dataclass()
class Vector2:
    
    """
    A versatile Vector2 class for 2D vector operations.

    Features:
    - Represents 2D vectors with x and y components.
    - Supports basic vector operations such as addition, subtraction, multiplication, and division.
    - Provides functions for calculating the dot product, length, and angle of the vector.
    - Allows vector serialization and deserialization to/from string format.
    - Supports moving the vector to a specified position.
    - Implements comparison operators for equality, less than, greater than, and greater than or equal to.

    Parameters:
    - `x` (int): The x-component of the vector.
    - `y` (int): The y-component of the vector.

    Usage:
    ```
    # Creating a Vector2 instance
    v1 = Vector2(2, 3)

    # Performing vector operations
    v2 = v1 + Vector2(1, 2)
    v3 = v1 - Vector2(1, 2)
    v4 = v1 * 2
    v5 = v1 / 2

    # Calculating dot product and length
    dot_product = v1.dot(Vector2(1, 1))
    vector_length = v1.length()

    # Normalizing the vector
    normalized_v1 = v1.normalized()

    # Calculating the angle with the positive y-axis
    angle = v1.angle()

    # Serializing and deserializing the vector
    v_str = v1.serialize()
    deserialized_v = Vector2.deserialize(v_str)

    # Moving the vector to a new position
    v1.move_to(Vector2(4, 5))

    # Comparing vectors
    are_equal = (v1 == v2)
    is_less_than = (v1 < v2)
    is_greater_than = (v1 > v2)
    is_greater_equal = (v1 >= v2)
    ```
    
    """
    
    x: int = 0
    y: int = 0
    
    

    def __str__(self):
        """
        Returns a string representation of the Vector2 object.
        """
        return f"Vector2({self.x}, {self.y})"


    def __add__(self, other):
        """
        Performs vector addition and returns a new Vector2 object.
        """
        return Vector2(self.x + other.x, self.y + other.y)


    def __sub__(self, value):
        """
        Performs vector subtraction and returns a new Vector2 object.
        """
        if type(value) is type(self):
            return Vector2(self.x - value.x, self.y - value.y)


    def __mul__(self, value):
        """
        Performs scalar multiplication and returns a new Vector2 object.
        """
        if isinstance(value, int):
            return Vector2(self.x * value, self.y * value)
        
        elif isinstance(value, float):
            return Vector2(self.x * value, self.y * value)
        
        elif type(value) is type(self):
            return Vector2(self.x * value.x, self.y - value.y)


    def __truediv__(self, value):
        """
        Performs scalar division and returns a new Vector2 object.
        """
        if isinstance(value, int):
            if value == 0:
                return self
            
            else:
                return Vector2(self.x / value, self.y / value)


    def dot(self, vector):
        """
        Calculates the dot product of two vectors.
        """
        return (self.x * vector.x) + (self.y * vector.y)


    def length(self):
        """
        Returns the length of the Vector.
        """
        length = sqrt(self.x ** 2 + self.y ** 2)
        length = round(length, 1)
        return length 


    def normalized(self):
        """
        Returns a normalized version of the vector.
        """
        length = self.length()
        
        if length == 0:
            return Vector2(0, 0)
            
        else:
            return Vector2(round(self.x / length, 1), round(self.y / length, 1))


    def angle(self):
        """
        Calculates the angle in degrees between the vector and the positive y-axis.
        """
        _angle = degrees(atan2(self.x, self.y))
        
        return round(_angle, 1)


    def serialize(self):
        """
        Serializes the Vector2 object to a string.
        """
        return f"({self.x}, {self.y})"


    @classmethod
    def deserialize(cls, vector_str: str):
        """
        Deserializes a string back into a new Vector2 instance.
        """
        if vector_str[0] == "(" and vector_str[-1] == ")" and vector_str.count("(") == 1 and vector_str.count(")") == 1 and vector_str.count(",") == 1:
            vector_str = vector_str.strip("()")
            cls.x, cls.y = map(int, vector_str.split(","))
            return Vector2(cls.x, cls.y)
        
        else:
            print("Invalid vector string")


    def move_to(self, pos: 'Vector2'):
        """
        Moves the Vector2 object to the specified position.
        """
        self.x = pos.x
        self.y = pos.y 
        
    def __eq__(self, vector: 'Vector2'):
        """
            Checks is this vector is equal to the other
        """
        if self.x == vector.x and self.y == vector.y:
            return True
  
        else:
            return False
    
    
    def __lt__(self, vector: 'Vector2'):
        """
            Checks of this vector is less than the other
        """
        if self.x < vector.x:
            return True

        elif self.x == vector.x:
            if self.y < vector.y:
                return True
    		
            else:
                return False
    	
        else:
            return False
    
    
    def __ge__(self, vector):
        """
            Check if a Vector is greater or equals to this
        """
        if self.x >= vector.x:
            return True

        else:
            return False
