from deepselect.category import Category
from deepselect.categorizer.categorizer import Categorizer


class BehaviorCategorizer(Categorizer):
    def __init__(self, colors=None):
        self.categories = dict()
        self.colors = colors if colors is not None else default_colors()

        self.set_category(type(None), name="No behavior specified", color='black')


    def set_category(self, behavior_class, category=None, name=None, color=None):
        if category is None:
            if name is None:
                name = behavior_class.__name__
            
            if color is None:
                color = self.colors.pop(0)
            
            category = Category(name, color)
        
        self.categories[behavior_class] = category

    
    def get_category_of(self, element):
        behavior_class = type(element.behavior)

        if behavior_class not in self.categories:
            self.set_category(behavior_class)
        
        return self.categories[behavior_class]



def default_colors():
    return ['tab:red', 'tab:blue', 'tab:orange', 'tab:purple', 'tab:green', 'tab:pink', 'tab:olive', 'tab:brown', 'tab:cyan']
