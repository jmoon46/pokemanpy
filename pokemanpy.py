class Pokeman:
  def __init__(self, name, level, skills = [], types = [], attributes = {}, attributesLevelUp = {}):
    self.name = name
    self.level = level
    self.skills = skills
    self.types = types
    self.attributes = attributes
    self.attributesLevelUp = attributesLevelUp

  def useSkill(self, selectedSkillIndex, target = None):
    print(self.name + ' used ' + self.skills[selectedSkillIndex - 1].name)

    if (target != None):
      target.takeDamage(self.skills[selectedSkillIndex - 1], self)

  def takeDamage(self, skill, skillUser):
    modifier = 1

    # for each type (of user) check if the target pokemon type is in the strengths or weaknesses array of the skill (then change modifier to 2 or .5)
    if skill.attributeModifier == 'spec':
      finalDamage = (((((self.level * 2) + 2) * skill.power * (skillUser.attributes['attack'] / self.attributes['defense'])) / 50) + 2) * modifier
    elif skill.attributeModifier == 'phys':
      finalDamage = (((((self.level * 2) + 2) * skill.power * (skillUser.attributes['specialAttack'] / self.attributes['specialDefense'])) / 50) + 2) * modifier


    finalDamage = round(finalDamage)
    self.attributes["hp"] -= finalDamage

    if self.attributes["hp"] <= 0:
      print(self.name + " fainted!")
      return
  
    print(self.name + " took " + str(finalDamage) + " damage. " + self.name + " has " + str(self.attributes["hp"]) + " health left.")


  def learnSkill(self, newSkill, selectedIndexToReplace = None):
    if (len(self.skills) < 4):
      self.skills.append(newSkill)
      print(self.name + ' learned ' + newSkill.name + '!')
    else:
      replacedSkill = self.skills[selectedIndexToReplace - 1]
      self.skills[selectedIndexToReplace - 1] = newSkill
      print(
        self.name +
          ' forgot ' +
          replacedSkill.name +
          ', and learned ' +
          newSkill.name +
          '!'
      )

  def levelUp(self):
    self.level += 1
    print(self.name + " grew to level " + str(self.level) + "!")
    self.attributes['hp'] += self.attributesLevelUp['hp']
    self.attributes['attack'] += self.attributesLevelUp['attack']
    self.attributes['defense'] += self.attributesLevelUp['defense']
    self.attributes['specialAttack'] += self.attributesLevelUp['specialAttack']
    self.attributes['specialDefense'] += self.attributesLevelUp['specialDefense']
    self.attributes['speed'] += self.attributesLevelUp['speed']
    print(self.attributes)

  def setLevel(self, level):
    while self.level < level:
      self.levelUp()

    

class Skill:
  def __init__(self, name, type, power, accuracy, attributeModifier):
    self.name = name
    self.type = type
    self.power = power
    self.accuracy = accuracy
    self.attributeModifier = attributeModifier

class Type:
  def __init__(self, name, strengths = [], weaknesses = []):
    self.name = name
    self.strengths = strengths
    self.weaknesses = weaknesses

grass = Type('grass')
fire = Type('fire')
water = Type('water')
flying = Type('flying')
normal = Type('normal')
rock = Type('rock')
ground = Type('ground')

grass.strengths.extend([water, ground, rock])
grass.weaknesses.extend([fire, flying])
fire.strengths.extend([grass])
fire.weaknesses.extend([water, ground])
water.strengths.extend([fire, rock, ground])
water.weaknesses.extend([grass])
flying.strengths.extend([grass])
flying.weaknesses.extend([rock])
normal.strengths.extend([])
normal.weaknesses.extend([])
rock.strengths.extend([flying])
rock.weaknesses.extend([water, ground, grass])
ground.strengths.extend([fire, rock])
ground.weaknesses.extend([grass, water])

vineWhip = Skill('Vine Whip', grass, 35, 100, 'spec')
leechSeed = Skill('Leech Seed', grass, 0, 85, 'spec')
growl = Skill('Growl', normal, 0, 100, 'phys')
razorLeaf = Skill('Razor Leaf', grass, 55, 100, 'spec')
solarBeam = Skill('Solar Beam', grass, 150, 100, 'spec')
tackle = Skill('Tackle', normal, 35, 100, 'phys')
scratch = Skill('Scratch', normal, 40, 100, 'phys')

bulbasaur = Pokeman('Bulbasaur', 1, [vineWhip], [grass], {'hp': 16, 'attack': 4, 'defense': 6, 'specialAttack': 5, 'specialDefense': 4, 'speed': 3}, {'hp': 5, 'attack': 1, 'defense': 3, 'specialAttack': 2, 'specialDefense': 3, 'speed': 2})
squirtle = Pokeman('Squirtle', 1, [tackle], [water], {'hp': 17, 'attack': 2, 'defense': 6, 'specialAttack': 4, 'specialDefense': 5, 'speed': 5}, {'hp': 5, 'attack': 1, 'defense': 3, 'specialAttack': 2, 'specialDefense': 2, 'speed': 3})
charmander = Pokeman('Charmander', 1, [scratch], [fire], {'hp': 15, 'attack': 2, 'defense': 2, 'specialAttack': 6, 'specialDefense': 3, 'speed': 4})

bulbasaur.setLevel(5)
bulbasaur.learnSkill(leechSeed)
bulbasaur.learnSkill(growl)
bulbasaur.useSkill(3)
bulbasaur.learnSkill(razorLeaf)
bulbasaur.learnSkill(solarBeam, 3)

squirtle.setLevel(6)
bulbasaur.setLevel(10)
bulbasaur.useSkill(4, squirtle)