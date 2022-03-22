"""Main module of the game."""

import game

# City

lviv = game.City("Lviv")
ivano_frankivsk = game.City("Ivano-Frankivsk")
ternopil = game.City("Ternopil")
lutsk = game.City("Lutsk")
rivne = game.City("Rivne")
zhytomyr = game.City("Zhytomyr")
vinnytsia = game.City("Vinnytsia")
odesa = game.City("Odesa")
mykolayiv = game.City("Mykolayiv")
kherson = game.City("Kherson")
kyiv = game.City("Kyiv")
minsk = game.City("Misnk")
moscov = game.City("Moscov")
cherkasy = game.City("Cherkasy")
simferopol = game.City("Simferopol")
zaporizhzhia = game.City("Zaporizhzhia")
dnipro = game.City("Dnipro")
kropyvnytskyi = game.City("Kropyvnytskyi")
donetsk = game.City("Donetsk")
luhansk = game.City("Luhansk")
sumy = game.City("Sumy")
poltava = game.City("Poltava")
uzhhorod = game.City("Uzhhorod")
khmelnytskyi = game.City("Khmelnytskyi")
chernivtsi = game.City("Chernivtsi")
chernihiv = game.City("Chernihiv")
kharkiv = game.City("Kharkiv")
altai_republic = game.City("Altai Republic")


minsk.link_city(moscov, "east")
minsk.link_city(kyiv, "south")

moscov.link_city(kyiv, "west")
moscov.link_city(altai_republic, "east")
moscov.link_city(minsk, "north")
altai_republic.link_city(moscov, "west")

lviv.link_city(ternopil, "east")
lviv.link_city(ivano_frankivsk, "south")

ternopil.link_city(lviv, "west")
ternopil.link_city(ivano_frankivsk, "south")
ternopil.link_city(khmelnytskyi, "east")

ivano_frankivsk.link_city(lviv, "west")
ivano_frankivsk.link_city(ternopil, "north")

khmelnytskyi.link_city(ternopil, "west")
khmelnytskyi.link_city(vinnytsia, "east")

vinnytsia.link_city(khmelnytskyi, "west")
vinnytsia.link_city(odesa, "south")
vinnytsia.link_city(kyiv, "north")

kyiv.link_city(chernihiv, "north")
kyiv.link_city(vinnytsia, "south")

chernihiv.link_city(minsk, "north")
chernihiv.link_city(sumy, "east")

sumy.link_city(chernihiv, "west")
sumy.link_city(kharkiv, "south")

kharkiv.link_city(sumy, "north")
kharkiv.link_city(luhansk, "east")
kharkiv.link_city(donetsk, "south")
kharkiv.link_city(dnipro, "west")

luhansk.link_city(kharkiv, "west")
luhansk.link_city(donetsk, "south")
luhansk.link_city(moscov, "north")

donetsk.link_city(kharkiv, "north")
donetsk.link_city(luhansk, "east")
donetsk.link_city(dnipro, "west")
donetsk.link_city(zaporizhzhia, "south")

dnipro.link_city(kharkiv, "north")
dnipro.link_city(donetsk, "east")
dnipro.link_city(zaporizhzhia, "south")

zaporizhzhia.link_city(donetsk, "east")
zaporizhzhia.link_city(dnipro, "north")
zaporizhzhia.link_city(kherson, "south")

kherson.link_city(mykolayiv, "west")
kherson.link_city(dnipro, "north")
kherson.link_city(zaporizhzhia, "east")

mykolayiv.link_city(kherson, "east")
mykolayiv.link_city(odesa, "west")
mykolayiv.link_city(dnipro, "north")

odesa.link_city(vinnytsia, "north")
odesa.link_city(mykolayiv, "east")

# Friends

volunteer = game.Friend(
    "Volunteer", "The person is driven to help Ukraine at any cost")
volunteer.set_conversation("Glory to Ukraine!")
refugee = game.Friend(
    "Refugee", "Her small bakery was destroyed by russian troops")
refugee.set_conversation("Thank you for helping our country.")
grandma = game.Friend("Grandma", "True Ukrainian grandma")
grandma.set_conversation("Dear, are you eating well?")
biden = game.Friend("Biden", "President of America")
biden.set_conversation("Behaviour of Russia violates any norms.")
zelenskyy = game.Friend("Zelenskyy", "President of Ukraine")
zelenskyy.set_conversation("Together to the victory!")
gypsy = game.Friend("Gypsy", "Best tractor owner")
gypsy.set_conversation("Do you believe in destiny?")

# Items

tomato_jar = game.Item("tomato jar")  # drone - grandma
tomato_jar.set_description("A  jar with concervated tomatoes.")
bayraktar = game.Item("bayraktar")  # troop - volunteer
bayraktar.set_description(
    "An aerial vehicle capable of remotely controlled or autonomous flight operation.")
javelin = game.Item("javelin")  # helicopter - zelenskyy
javelin.set_description(
    "The system takes attack against armored vehicles, buildings, helicopters.")
tractor = game.Item("tractor")  # tank - gypsy
tractor.set_description("A motor vehicle used on farms for pulling machinery.")
salo_bullets = game.Item("salo bullets")  # kadyrov - //
salo_bullets.set_description("Bullets soaked with traditional Ukrainian salo.")
tryzub = game.Item("tryzub")  # putin //
tryzub.set_description(
    "The coat of arms of Ukraine is a blue shield with a gold trident.")
sanctions = game.Item("sanctions")  # zombies - elona_musk
sanctions.set_description(
    "Commercial and financial penalties applied by one or more countries against a state.")
beetles_poison = game.Item("beetles poison")  # luckshenko  //
beetles_poison.set_description(
    "The poison acts on the nervous systems of insects to kill them rapidly.")
palyanytsia = game.Item("palyanytsia")  # saboteur - refugee
palyanytsia.set_description(
    "Ukrainian hearth-baked bread, made mostly of wheat flour.")

# Enemies

drone = game.Enemy("Z drone", "")
drone.set_weakness(tomato_jar)
helicopter = game.Enemy("Z helicopter", "")
helicopter.set_weakness(javelin)
tank = game.Enemy("Z tank", "russian soldier left it to find some fuel")
tank.set_weakness(tractor)
troop = game.Enemy("Z troop", "russian troop parked vehicles in one place")
troop.set_weakness(bayraktar)
putin = game.Boss("putin", "Bloody dictator")
putin.set_weakness(tryzub)
lukashenko = game.Boss("lukashenko", "Colorado potato beetle")
lukashenko.set_weakness(beetles_poison)
kadyrov = game.Boss("kadyrov", "don don")
kadyrov.set_weakness(salo_bullets)
zombies = game.Enemy("russian zombies", "apolitical biomass")
zombies.set_weakness(sanctions)
saboteur = game.Enemy("civilian", "a suspicious person")
saboteur.set_weakness(palyanytsia)


altai_republic.set_enemy(putin)
minsk.set_enemy(lukashenko)
luhansk.set_enemy(kadyrov)
donetsk.set_enemy(troop)
moscov.set_enemy(zombies)
sumy.set_enemy(tank)
kharkiv.set_enemy(helicopter)
chernihiv.set_enemy(drone)
vinnytsia.set_enemy(saboteur)

lviv.set_friend(volunteer)
ivano_frankivsk.set_friend(grandma)
ternopil.set_friend(refugee)
kyiv.set_friend(zelenskyy)
odesa.set_friend(gypsy)
kherson.set_friend(biden)

volunteer.set_item(bayraktar)
grandma.set_item(tomato_jar)
refugee.set_item(palyanytsia)
zelenskyy.set_item(javelin)
gypsy.set_item(tractor)
biden.set_item(sanctions)

khmelnytskyi.set_item(salo_bullets)
mykolayiv.set_item(tryzub)
dnipro.set_item(beetles_poison)

player = game.Player("Peter", 100)

# game cycle

current_city = lviv
backpack = []


while player.is_dead() is False:

    print("\n")
    current_city.get_details()

    inhabitant = current_city.get_enemy()
    if inhabitant is not None:
        inhabitant.describe()
        inhabitant.get_status()

    friend = current_city.get_friend()
    if friend is not None:
        friend.describe()

    item = current_city.get_item()
    if item is not None:
        item.describe()

    command = input("> ")

    if command in ["north", "south", "east", "west"]:
        # Move in the given direction
        try:
            current_city = current_city.move(command)
        except KeyError:
            print("There is no cities in the direction.")
    elif command == "talk":
        # Talk to a friend
        if friend is not None:
            friend.talk()
            gift = friend.get_item()
            print(f"I have a gift for you! It is a {gift.item}.")
            print(gift.description)
            print("You put the " + gift.get_name() + " in your backpack")
            backpack.append(gift.get_name())
            current_city.set_item(None)
            current_city.set_friend(None)
    elif command == "fight":
        if inhabitant is not None:
            # Fight with the inhabitant, if there is one
            print("What will you fight with?")
            print(backpack)
            fight_with = input()

            # Do I have this item?
            if fight_with in backpack:

                if inhabitant.fight(fight_with):
                    # What happens if you win?
                    print("Hooray, you won the fight!")
                    backpack.remove(fight_with)
                    current_city.enemy = None
                    defeated = inhabitant.get_defeated()
                    if defeated == 9:
                        print("Congratulations, you have vanquished the enemy horde!")
                        print("Glory to Ukraine!")
                        player.damage(100)
                    else:
                        print(f"Enemies left: {9-defeated}")
                else:
                    # What happens if you lose?
                    print("Oh dear, you lost the fight.")
                    if (player.health - inhabitant.attack) <= 0:
                        print("That's the end of the game")
                    player.damage(inhabitant.attack)
                    if player.my_health() > 0:
                        print(f"Your health: {player.my_health()}"
            else:
                print("You don't have a " + fight_with)
        else:
            print("There is no one here to fight with")
    elif command == "take":
        if item is not None:
            print("You put the " + item.get_name() + " in your backpack")
            backpack.append(item.get_name())
            current_city.set_item(None)
        else:
            print("There's nothing here to take!")
    else:
        print("I don't know how to " + command)
