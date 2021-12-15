import random

class hungerGames:
    def runGame(self, tributes):
        self.tributes = []
        self.gameString = ''
        for x in range(len(tributes)):
            self.tributes.append(tribute(tributes[x],tribute.generateWeapon()))
        while (len(self.tributes) > 1):
            if (len(self.tributes) == 2):
                self.finalFight()
            index = random.randrange(0, len(self.tributes))
            otherIndex = random.randrange(0, len(self.tributes))
            while (index == otherIndex):
                index = random.randrange(0, len(self.tributes))
            fightStrength1 = self.battleStrength(self.tributes[index].weapon)
            fightStrength2 = self.battleStrength(self.tributes[otherIndex].weapon)
            if (fightStrength1 > fightStrength2):
                self.combatPrint(self.tributes[index], self.tributes[otherIndex])
                self.tributes.pop(otherIndex)
            elif (fightStrength2 > fightStrength1):
                self.combatPrint(self.tributes[otherIndex], self.tributes[index])
                self.tributes.pop(index)
        if (len(self.tributes) == 1):
            self.gameString += self.tributes[0].name + ' is the winner!\n'
        return self.gameString

        
    def battleStrength(self, weapon):
        if (weapon == "hands"):
            return random.randrange(0,5)
    
    def combatPrint(self, winner, loser):
        if (winner.weapon == "hands"):
            self.gameString += winner.name + " killed " + loser.name + ".\n"
    
    def finalFight(self):
        self.gameString += "FINAL FIGHT:\n"
        
    
class tribute:
    def __init__(self, name, weapon):
        self.name = name
        self.weapon = weapon
    
    @staticmethod
    def generateWeapon():
        return "hands"
    
#game = hungerGames()
#print(game.runGame(["Carter", "Skylar", "Chris"]))