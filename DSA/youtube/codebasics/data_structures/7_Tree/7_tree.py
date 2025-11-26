class TreeNode:
    def __init__(self, data):
        self.parent = None
        self.data = data
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

    def print_tree(self):
        level = self.get_level()
        prefix = (" " * 4 * level + "|--") if level != 0 else ""
        print(prefix + self.data)
        for child in self.childrens:
            child.print_tree()
        return ''
            
    def __str__(self):
        return str(self.data)
        

def build_product_tree():
    root = TreeNode("Electronics")

    laptop = TreeNode("Laptops")
    laptop.add_child(TreeNode("Mac"))
    laptop.add_child(TreeNode("Surface"))
    laptop.add_child(TreeNode("Thinkpad"))

    cellphone = TreeNode("Cell Phones")
    cellphone.add_child(TreeNode("Iphone"))
    cellphone.add_child(TreeNode("Pixel"))
    cellphone.add_child(TreeNode("Moto"))

    tv = TreeNode("Televisions")
    tv.add_child(TreeNode("Samsung"))
    tv.add_child(TreeNode("LG"))
    tv.add_child(TreeNode("Sony"))

    root.add_child(laptop)
    root.add_child(cellphone)
    root.add_child(tv)

    return root


if __name__ == "__main__":
    root = build_product_tree()
    print(root.print_tree())