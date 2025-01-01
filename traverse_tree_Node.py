class Node:
    def __init__(self, decision, consequence, left=None, right=None):
        self.decision = decision
        self.consequence = consequence
        self.left = left  # Switch track
        self.right = right  # Do nothing

# Create the decision tree
tree = Node(
    "Start",
    "Trolley is heading towards the main track.",
    Node("Switch Track", "Save the group, sacrifice one person."),
    Node("Do Nothing", "Save one person, sacrifice the group.")
)

# Function to traverse the tree
def traverse_tree(node):
    if not node:
        return
    print(f"Decision: {node.decision}")
    print(f"Consequence: {node.consequence}")
    if node.left or node.right:
        print("\nOptions:")
        print(f"1. {node.left.decision}" if node.left else "")
        print(f"2. {node.right.decision}" if node.right else "")
    choice = input("Choose an option (1 or 2): ")
    if choice == "1" and node.left:
        traverse_tree(node.left)
    elif choice == "2" and node.right:
        traverse_tree(node.right)

# Start the decision tree
traverse_tree(tree)
