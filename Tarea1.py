## DIEGO RODRIGUEZ A00835032

from typing import List, Any
from collections import deque
from collections import OrderedDict

class Stack:
    def __init__(self):
        self._data: List[Any] = []

    def push(self, item):
        """Insertar elemento"""
        self._data.append(item)

    def pop(self):
        """Eliminar y retornar"""
        if self.is_empty():
            raise IndexError("Stack vacio")
        return self._data.pop()

    def peek(self):
        """Ver el maximo sin eliminar"""
        if self.is_empty():
            raise IndexError("Stack vacio")
        return self._data[-1]

    def is_empty(self):
        return len(self._data) == 0

    def size(self):
        return len(self._data)

    def __repr__(self):
        return f"Stack({self._data})"
    


class Queue:
    def __init__(self):
        self._data = deque()

    def enqueue(self, item):
        """Insertar al final"""
        self._data.append(item)

    def dequeue(self):
        """Eliminar del frente"""
        if self.is_empty():
            raise IndexError("Queue vacia")
        return self._data.popleft()

    def peek(self):
        """Ver el frente"""
        if self.is_empty():
            raise IndexError("Queue vacia")
        return self._data[0]

    def is_empty(self):
        return len(self._data) == 0

    def size(self):
        return len(self._data)

    def __repr__(self):
        return f"Queue({list(self._data)})"
    



class OrderedHashTable:
    def __init__(self):
        self._data = OrderedDict()

    def put(self, key, value):
        """Insertar o actualizar"""
        self._data[key] = value

    def get(self, key):
        """Obtener valor"""
        if key not in self._data:
            raise KeyError(f"Clave {key} no encontrada")
        return self._data[key]

    def remove(self, key):
        """Eliminar elemento"""
        if key not in self._data:
            raise KeyError(f"Clave {key} no encontrada")
        del self._data[key]

    def contains(self, key):
        return key in self._data

    def keys(self):
        return list(self._data.keys())

    def values(self):
        return list(self._data.values())

    def items(self):
        return list(self._data.items())

    def size(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def __repr__(self):
        return f"OrderedHashTable({self._data})"