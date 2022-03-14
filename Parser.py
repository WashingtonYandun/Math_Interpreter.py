class Parser:
    def __init__(self, tokens):
        self.tokens = iter(tokens)
        self.move()

    def move(self):
        try:
            self.current_token = next(self.tokens)
        except StopIteration:
            self.current_token = None

    def parse(self):
        '''
        if self.current_token == None:
            return None

        res = self.__repr__()

        if self.current_token != None:
            pass
        '''

        return 0
