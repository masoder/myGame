# define the Warrior class
class Warrior:
    name = ""
    kind = ""
    level = 1
    wealth = 0
    health = 100.0
    defence = 1

class Monster:
    kind = ""
    level = 0
    health = 0
    defence = 0

def fight(fighter1, fighter2):
    print "%s is going to fight a %s" % (fighter1.name, fighter2.kind) 
    print "%s is a level %d %s" % (fighter1.name, fighter1.level, fighter1.kind)
    print "%s is a level %d monster" % (fighter2.kind, fighter2.level)
    print "%s has health %d, and %s has health %d" % (fighter1.name, fighter1.health, fighter2.kind, fighter2.health)
    choice = raw_input("Are you sure: ")
    if "y" in choice or "Y" in choice:
        print "Fight!"
        while fighter1.health>0 and fighter2.health>0:
            damageA = fighter1.level 
            damageB = fighter2.level 
            fighter1.health -= damageB
            fighter2.health -= damageA
            
        if fighter1.health>0:
            print "%s is victorious!" % fighter1.name    
        elif fighter2.health>0:
            print "%s won" % fighter2.kind
        else:
            print "Both are dead"
        
    
    else:
        print "Run away"

Hero = Warrior()
Hero.name = "Martin"
Hero.kind = "Barbarian"

bear = Monster()
bear.kind = "Bear"
bear.level = 2
bear.health = 50.0
bear.defence = 2

fight(Hero, bear)


    