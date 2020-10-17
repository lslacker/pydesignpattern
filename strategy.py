'''
Scenario:
   Abstract strategy class with a default set of behaviors
   Concrete strategy classes with new behaviors

'''

import types
class Strategy:
    def __init__(self, function=None):
        self.name = 'Default Strategy'

        if function:
            self.execute = types.MethodType(function, self)

    def execute(self):
        print(f'{self.name} is used'.format(self.name))


def strategy_one(self):
    print(f'{self.name} is used to execute method 1')

def strategy_two(self):
    print(f'{self.name} is used to execute method 2')


s0 = Strategy()
s0.execute()

s1 = Strategy(strategy_one)
s1.name = 'Strategy 1'
s1.execute()

s2 = Strategy(strategy_two)
s2.name = 'Strategy 2'
s2.execute()


