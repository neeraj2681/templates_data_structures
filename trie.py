class Trie:

    def __init__(self):
        self.mapper = {}

    def insert(self, word: str) -> None:
        jar = self.mapper
        for item in word:
            if (item in jar):
                jar = jar.get(item)
                continue
            jar.update({item : {'is_word': False}})
            jar = jar.get(item)
        jar.update({'is_word': True})
        

    def search(self, word: str) -> bool:
        jar = self.mapper
        for item in word:
            if (item in jar):
                jar = jar.get(item)
                continue
            else:
                return False
        return jar.get('is_word')
        

    def startsWith(self, prefix: str) -> bool:
        jar = self.mapper
        for item in prefix:
            if(item in jar):
                jar = jar.get(item)
            else:
                return False
        return True

        
