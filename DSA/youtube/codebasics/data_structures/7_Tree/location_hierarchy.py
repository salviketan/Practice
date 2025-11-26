class LocationTreeNode:
    def __init__(self, location: str):
        self.parent = None
        self.location = location
        self.childrens = []

    def add_child(self, child):
        child.parent = self
        self.childrens.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def print_tree(self, level_arg: int = 3):
        level = self.get_level()
        prefix = (" " * 4 * level + "|--") if level != 0 else ""
        print(prefix + self.location)
        if level >= level_arg:
            return
        for child in self.childrens:
            child.print_tree(level_arg)
        return ''
            
    def __str__(self):
        return str(self.location)
        

def build_management_tree():
    root = LocationTreeNode("Global")

    india = LocationTreeNode("India")

    gujarat = LocationTreeNode("Gujarat")
    gujarat.add_child(LocationTreeNode("Ahmedabad"))
    gujarat.add_child(LocationTreeNode("Baroda"))

    karnataka = LocationTreeNode("Karnataka")
    karnataka.add_child(LocationTreeNode("Bangluru"))
    karnataka.add_child(LocationTreeNode("Mysore"))

    india.add_child(gujarat)
    india.add_child(karnataka)
    
    usa = LocationTreeNode("USA")

    new_jersey = LocationTreeNode("New Jersey")
    new_jersey.add_child(LocationTreeNode("Princeton"))
    new_jersey.add_child(LocationTreeNode("Trenton"))

    california = LocationTreeNode("California")
    california.add_child(LocationTreeNode("San Francisco"))
    california.add_child(LocationTreeNode("Mountain View"))
    california.add_child(LocationTreeNode("Palo Alto"))

    usa.add_child(new_jersey)
    usa.add_child(california)

    root.add_child(india)
    root.add_child(usa)

    return root


if __name__ == "__main__":
    root = build_management_tree()
    print("Level: 1")
    root.print_tree(1)
    print()
    print("Level: 2")
    root.print_tree(2)
    print()
    print("Level: 3")
    root.print_tree(3)