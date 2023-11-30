def castspell(hero, mana, spell):

    if mana <= heroes[hero]['MP']:
        heroes[hero]['MP'] -= mana
        print(f"{hero} has successfully cast {spell} and now has {heroes[hero]['MP']} MP!")
    else:
        print(f"{hero} does not have enough MP to cast {spell}!")


def takedamage(hero, damage, attacker):
    if damage >= heroes[hero]['HP']:
        print(f"{hero} has been killed by {attacker}!")
        del heroes[hero]
    else:
        heroes[hero]['HP'] = heroes[hero]['HP'] - damage
        print(f"{hero} was hit for {damage} HP by {attacker} and now has {heroes[hero]['HP']} HP left!")


def recharge(hero, amount):
    current_mp = heroes[hero]['MP']
    heroes[hero]['MP'] += amount
    if heroes[hero]['MP'] > 200:
        diff = abs(current_mp - 200)
        heroes[hero]['MP'] = 200
        print(f"{hero} recharged for {diff} MP!")
    else:
        print(f'{hero} recharged for {amount} MP!')


def heal(hero, amount):
    current_hp = heroes[hero]['HP']
    heroes[hero]['HP'] += amount
    if heroes[hero]['HP'] > 100:
        diff = abs(current_hp - 100)
        heroes[hero]['HP'] = 100
        print(f"{hero} healed for {diff} HP!")
    else:
        print(f'{hero} healed for {amount} HP!')


number_of_heroes = int(input())

heroes = {}

for i in range(number_of_heroes):
    info = input().split()

    hero = info[0]
    hp = int(info[1])
    mana = int(info[2])

    if hero not in heroes.keys():
        heroes[hero] = {'HP': 0, 'MP': 0}
    heroes[hero]['HP'] = hp
    heroes[hero]['MP'] = mana


while True:
    command = input()
    if command == 'End':
        break

    command_split = command.split(' - ')

    act = command_split[0]
    hero_name = command_split[1]

    if act == 'CastSpell':
        mana_needed = int(command_split[2])
        spell_name = command_split[3]
        castspell(hero_name, mana_needed, spell_name)
    elif act == 'TakeDamage':
        damage = int(command_split[2])
        attacker = command_split[3]
        takedamage(hero_name, damage, attacker)
    elif act == 'Recharge':
        amount = int(command_split[2])
        recharge(hero_name, amount)
    elif act == 'Heal':
        amount = int(command_split[2])
        heal(hero_name, amount)


for item, value in heroes.items():
    print(f'{item}')
    print(f"  HP: {heroes[item]['HP']}")
    print(f'  MP: {heroes[item]["MP"]}')
