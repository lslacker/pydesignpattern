'''
Recursive data structure
menu > sub-menu > sub-sub-menu

component
child
composite
'''
import abc

class Component(metaclass=abc.ABCMeta):

    def __init__(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def component_function(self):
        pass


class Child(Component): # inheris from the abstract class, Component

    def __init__(self, *args, **kwargs):
        Component.__init__(self, *args, **kwargs)
        self.name = args[0]

        # This is where we store the name of your child item!
    def component_function(self):
        #Print the name of your child item here!
        print(f'{self.name}')


class Composite(Component):

    def __init__(self, *args, **kwargs):
        Component.__init__(self, *args, **kwargs)

        # This is where we store the name of the composite item!
        self.name = args[0]


        # This is where we keep our child items
        self.children = []

    def append_child(self, child):
        self.children.append(child)

    def remove_child(self, child):
        self.children.remove(child)

    def component_function(self):
        print(f'{self.name}')

        for child in self.children:
            child.component_function()

sub1 = Composite('submenu1')
sub11 = Child('sub_submenu1')
sub12 = Child('sub_submenu2')

sub1.append_child(sub11)
sub1.append_child(sub12)

top = Composite('top menu')

sub2 = Child('submenu2')

top.append_child(sub1)
top.append_child(sub2)

top.component_function()
