#!/usr/bin/env python3

class Shoe:
    def __init__(self,  brand, size,  condition="New"):
        self._brand = brand
        self._size = size
        self._condition = condition

    @property
    def brand(self):
        return self._brand
    
    @property
    def size(self):
        return self._size
    
 
    @size.setter
    def size(self, new_size):
      if new_size is not type(int):
          print("size must be an integer")
      else:
          self._size = new_size

    @property
    def condition(self):
       return self._condition 

    def cobble(self):
        self._condition = "New"
        print("Your shoe is as good as new!")

   