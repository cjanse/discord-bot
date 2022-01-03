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
        elif (weapon == "bow"):
            return random.randrange(3,8)
        elif (weapon == "flamethrower"):
            return random.randrange(4,10)
        elif (weapon == "sword"):
            return random.randrange(2,8)
        elif (weapon == "axe"):
            return random.randrange(2,8)
        elif (weapon == "miscellaneous"):
            return random.randrange(0,10)
        else:
            return random.randrange(0,5)
    
    def combatPrint(self, winner, loser):
        handsMessages = [winner.name + " punched " + loser.name + ".\n"]
        bowMessages = [winner.name + " shot an arrow at " + loser.name + ".\n"]
        flamethrowerMessages = [winner.name + " used a flamethrower to burn " + loser.name + ".\n"]
        swordMessages = [winner.name + " honorably defeated " + loser.name + " in a swordfight.\n"]
        axeMessages = [winner.name + " plunged an axe through " + loser.name + "\'s heart.\n"]
        miscellaneousMessages = [winner.name + " gave a look of disappointment to " + loser.name + ".\n"]
        if (winner.weapon == "hands"):
            self.gameString += handsMessages[random.randrange(0,len(handsMessages))]
        elif (winner.weapon == "bow"):
            self.gameString += bowMessages[random.randrange(0,len(bowMessages))]
        elif (winner.weapon == "flamethrower"):
            self.gameString += flamethrowerMessages[random.randrange(0,len(flamethrowerMessages))]
        elif (winner.weapon == "sword"):
            self.gameString += swordMessages[random.randrange(0,len(swordMessages))]
        elif (winner.weapon == "axe"):
            self.gameString += axeMessages[random.randrange(0,len(axeMessages))]
        elif (winner.weapon == "miscellaneous"):
            self.gameString += miscellaneousMessages[random.randrange(0,len(miscellaneousMessages))]
        else:
            self.gameString += winner.name + " killed " + loser.name + ".\n"
    
    def finalFight(self):
        self.gameString += "FINAL FIGHT:\n"
        
    
class tribute:
    def __init__(self, name, weapon):
        self.name = name
        self.weapon = weapon
    
    @staticmethod
    def generateWeapon():
        weapons = ["hands","bow","flamethrower","sword","axe","miscellaneous"]
        return weapons[random.randrange(0,len(weapons))]
    
#game = hungerGames()
#print(game.runGame(["Carter", "Skylar", "Chris"]))