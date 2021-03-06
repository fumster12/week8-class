class Node:

  def __init__(self):
    self.data = None
    self.next = None


class GroceryList:

  def __init__(self):
    self.root = None

  # This version would insert new items
  # at the head of the list.
  #
  # def add(self, name_of_food):
  #   new_node = Node()
  #   new_node.data = name_of_food

  #   if self.root is None:
  #     self.root = new_node
  #   else:
  #     new_node.next = self.root
  #     self.root = new_node

  # This version adds new items to
  # the end of the list.
  def add(self, name_of_food):
    new_node = Node()
    new_node.data = name_of_food

    if self.root is None:
      self.root = new_node
    else:
      current_node = self.root
      while current_node.next != None:
        current_node = current_node.next

      current_node.next = new_node

  def find(self, data):
    node = self.root
    while node != None and node.data != data:
      node = node.next

    return node != None


  def at():
    pass

  def display(self, node):
    if node != None:
      print(node.data)
      self.display(node.next)

  def display_reverse(self, node):
    if node.next != None:
      self.display_reverse(node.next)
      print(node.data)

  def sort():
    pass

groceries = GroceryList()
groceries.add("cookies")
groceries.add("ice cream")
groceries.add("pizza")
groceries.display(groceries.root)

print("-------")
groceries.display_reverse(groceries.root)

if groceries.find("cookies"):
  print("This is a good list!")
else:
  print("You should buy some cookies!")











# print(groceries.at(1))  # => "ice cream"

# groceries2 = GroceryList()
# groceries2.add("broccoli")
# groceries2.add("apples")





