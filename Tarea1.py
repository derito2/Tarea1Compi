## DIEGO RODRIGUEZ A00835032

from typing import List, Any
from collections import deque
from collections import OrderedDict

class Stack:
    def __init__(self):
        self._data: List[Any] = []

    def push(self, item):
        #Insertar elemento
        self._data.append(item)

    def pop(self):
        #Eliminar y retornar
        if self.is_empty():
            raise IndexError("Stack vacio")
        return self._data.pop()

    def peek(self):
        #Ver el maximo sin eliminar
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
        #Insertar al final
        self._data.append(item)

    def dequeue(self):
        #Eliminar del frente
        if self.is_empty():
            raise IndexError("Queue vacia")
        return self._data.popleft()

    def peek(self):
        #Ver el frente
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
        #Insertar o actualizar
        self._data[key] = value

    def get(self, key):
        #Obtener valor
        if key not in self._data:
            raise KeyError(f"Clave {key} no encontrada")
        return self._data[key]

    def remove(self, key):
        #Eliminar elemento
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
    


#Pruebas
def test_stack():
    print("Stack pruebas")
    s = Stack()

    assert s.is_empty()
    s.push(10)
    s.push(20)
    assert s.size() == 2
    assert s.peek() == 20
    assert s.pop() == 20
    assert s.pop() == 10
    assert s.is_empty()

    try:
        s.pop()
    except IndexError:
        print("Stack error correctamente manejado")

    print("Stack tests passed\n")


def test_queue():
    print("Pruebas Queu")
    q = Queue()

    assert q.is_empty()
    q.enqueue(1)
    q.enqueue(2)
    assert q.size() == 2
    assert q.peek() == 1
    assert q.dequeue() == 1
    assert q.dequeue() == 2
    assert q.is_empty()

    try:
        q.dequeue()
    except IndexError:
        print("Queue error correctamente manejado")

    print("Queue tests passed\n")

def test_hash_table():
    print("Pruebas Hash")
    h = OrderedHashTable()

    assert h.is_empty()
    h.put("a", 100)
    h.put("b", 200)

    assert h.get("a") == 100
    assert h.get("b") == 200

    h.put("a", 300)
    assert h.get("a") == 300

    assert h.contains("a")
    h.remove("a")
    assert not h.contains("a")

    assert h.keys() == ["b"]

    try:
        h.get("z")
    except KeyError:
        print("Hash error correctamente manejado")

    print("Hash Table tests passed\n")


if __name__ == "__main__":
    test_stack()
    test_queue()
    test_hash_table()
    print("pruebas exito")