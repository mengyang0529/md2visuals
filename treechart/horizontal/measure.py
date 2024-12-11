from treechart.basics import *
from core.geometry import *

class MeasureLayout:
    def __init__(self):
        self.total_height_list = {}
        
    def measure_node(self, node, idx):
        # Determine basic size
        if node.level == 0:
            w, h = MAIN_TOPIC_BOX_WIDTH, MAIN_TOPIC_BOX_HEIGHT
        elif node.level == 1:
            w, h = SUB_TOPIC_BOX_WIDTH, SUB_TOPIC_BOX_HEIGHT
        else:
            w, h = DETAIL_BOX_WIDTH, DETAIL_BOX_HEIGHT
            
        node.required_width = w
        node.required_height = h
        node.is_direction = True

        total_height = 0

        # Recursive traversal to measure children
        if node.children:
            for c in node.children:
                self.measure_node(c, idx)  # Measure child nodes

            # Calculate total width and height for the current node based on its children
            total_height = sum(c.required_height + DETAIL_SPACING for c in node.children) - DETAIL_SPACING

        self.total_height_list[idx] = max(self.total_height_list[idx], total_height)
        

    def measure(self, root):
        # Start measuring from the root node
        for idx, node in enumerate(root.children):
            self.total_height_list[idx] = 0
            self.measure_node(node, idx)
            node.required_height = self.total_height_list[idx]
            
        return root  
