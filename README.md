class Character:
    def __init__(self, xp, st, mp):

        self.xp = xp
        self.st = st
        self.mp = mp

    def getInfo(self):
       
        return f"Character Info:\nExperience: {self.xp}\nStrength: {self.st}\nMana: {self.mp}"
