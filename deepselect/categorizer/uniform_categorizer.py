from deepselect.categorizer.categorizer import Categorizer


class UniformCategorizer(Categorizer):
    def __init__(self, category):
        self.category = category

    
    def get_category_of(self, element):
        return self.category
