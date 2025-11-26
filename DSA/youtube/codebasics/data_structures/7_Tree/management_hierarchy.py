class ManagementTreeNode:
    def __init__(self, name: str, designation: str):
        self.parent = None
        self.name = name
        self.designation = designation
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

    def print_tree(self, property_name: str):
        level = self.get_level()
        prefix = (" " * 4 * level + "|--") if level != 0 else ""
        if property_name == "name":
            print(prefix + self.name)
        if property_name == "designation":
            print(prefix + self.designation)
        if property_name == "both":
            print(f"{prefix}{self.name} ({self.designation})")
        for child in self.childrens:
            child.print_tree(property_name)
        return ''
            
    def __str__(self):
        return str(self.name + " " + self.designation)
        

def build_management_tree():
    # CTO Hierarchy
    cto = ManagementTreeNode("Chinmay","CTO")

    infra_head = (ManagementTreeNode("Vishwa","Infrastructure Head"))
    infra_head.add_child(ManagementTreeNode("Dhaval","Cloud Manager"))
    infra_head.add_child(ManagementTreeNode("Abhijit","App Manager"))

    cto.add_child(infra_head)
    cto.add_child(ManagementTreeNode("Aamir","Application Head"))

    # HR Hierarchy
    hr_head = ManagementTreeNode("Gels","HR Head")
    hr_head.add_child(ManagementTreeNode("Peter","Recruitment Manager"))
    hr_head.add_child(ManagementTreeNode("Waqas","Policy Manager"))

    ceo = ManagementTreeNode("Nilupul","CEO")
    ceo.add_child(cto)
    ceo.add_child(hr_head)

    return ceo


if __name__ == "__main__":
    ceo = build_management_tree()
    ceo.print_tree("name")
    print()
    ceo.print_tree("designation")
    print()
    ceo.print_tree("both")