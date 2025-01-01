from graphviz import Digraph

# Create a new Digraph
dot = Digraph()

# Add nodes
dot.node('A', 'Start')
dot.node('B', 'Switch Track\n(Save group, sacrifice 1)')
dot.node('C', 'Do Nothing\n(Save 1, sacrifice group)')

# Add edges
dot.edge('A', 'B', 'Option 1')
dot.edge('A', 'C', 'Option 2')

# Render the tree
dot.render('trolley_problem_tree', format='png', cleanup=True)
print("Decision tree saved as trolley_problem_tree.png")
