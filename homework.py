#  Необходимо реализовать метод разворота односвязного списка 

def printSinglyLinkedList(node):
  if node != None:
    printSinglyLinkedList(node['next'])
    print(node['value'])
list = {
  'value': 1,
  'next': {
    'value': 2,
    'next': {
      'value': 3,
      'next': {
        'value': 4,
        'next': None,
      },
    },
  },
}
printSinglyLinkedList(list)

# Реализовать сортировку пузырьком для двухсвязного списка
from random import randint
 
def bubble(array):
    for i in range(n-1):
        for j in range(n-i-1):
            if array[j] > array[j+1]:
                buff = array[j]
                array[j] = array[j+1]
                array[j+1] = buff
 
n = 8
list = []
for i in range(n):
    list.append(randint(1, 99))
 
print(list)
bubble(list)
print(list)
