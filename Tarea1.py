## DIEGO RODRIGUEZ A00835032

from typing import List, Any
from collections import deque


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