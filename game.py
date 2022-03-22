"""Module with game classes."""


class City:
    """Stores a data about the city."""
    defeated = []

    def __init__(self, name, enemy=None, friend=None, item=None):
        """
        Receives data about the city.
        >>> lviv = City("Lviv")
        >>> lviv.name
        'Lviv'
        """
        self.name = name
        self.enemy = enemy
        self.friend = friend
        self.item = item
        self.direct = {}

    def link_city(self, linked_city, direction):
        """Links two cities by a direction."""
        self.direct[direction] = linked_city

    def set_enemy(self, enemy):
        """Sets an enemy to the city."""
        self.enemy = enemy
        enemy.city = self

    def set_friend(self, friend):
        """Sets a friend to the city."""
        self.friend = friend

    def set_item(self, item):
        """Sets an item to the city."""
        self.item = item

    def get_details(self):
        """Provides a description of the city."""
        print(self.name)
        print("--------------------")
        for item in self.direct.items():
            print(f"{item[1].name} is in the {item[0]}")

    def get_enemy(self):
        """Returns an enemt of the city."""
        return self.enemy

    def get_friend(self):
        """Returns a friend of the city."""
        return self.friend

    def get_item(self):
        """
        Returns an item of the city.
        >>> lviv = City("Lviv Hall")
        >>> lviv.set_item(Item("cheese"))
        >>> lviv.item.item == lviv.get_item().item
        True
        """
        return self.item

    def move(self, direction):
        """
        Returns a city linked to a current one at a given direction.
        >>> lviv = City("Lviv")
        >>> lviv.link_city(City("Ternopil"), "east")
        >>> lviv.move("east").name
        'Ternopil'
        """
        return self.direct[direction]


class Person:
    """Basement class for enemies and friends"""

    def __init__(self, name, description, conversation=None, city=None):
        """
        Receives a data about the person."
        >>> kate = Person("Kate", "A small girl")
        >>> kate.description
        'A small girl'
        """
        self.name = name
        self.description = description
        self.conversation = conversation
        self.city = city

    def set_conversation(self, conversation):
        """Sets a conversation for the person."""
        self.conversation = conversation

    def describe(self):
        """Prints a description of the person."""
        print(f"{self.name} is here!\n{self.description}")

    def talk(self):
        """Prints a conversation of the person."""
        print(self.conversation)


class Enemy(Person):
    """Stores a data about an enemy."""

    def __init__(self, name, description, conversation=None, weakness=None, city=None):
        """
        Receives input data of the enemy.
        >>> tabitha = Enemy("Tabitha", "An enormous spider with countless eyes and furry legs.")
        >>> tabitha.name
        'Tabitha'
        >>> tabitha.description
        'An enormous spider with countless eyes and furry legs.'
        """
        super().__init__(name, description, conversation, city)
        self.weakness = weakness
        self.attack = 30

    def set_weakness(self, weakness):
        """
        Defines a weakness of the enemy.
        >>> tabitha = Enemy("Tabitha", "An enormous spider with countless eyes and furry legs.")
        >>> tabitha.set_weakness(Item("book"))
        >>> tabitha.weakness
        'book'
        """
        self.weakness = weakness.item

    def fight(self, fight_with):
        """
        Checks whether the fight_with is a a weakness of the enemy.
        >>> tabitha = Enemy("Tabitha", "An enormous spider with countless eyes and furry legs.")
        >>> tabitha.set_weakness(Item("book"))
        >>> tabitha.fight('cheese')
        False
        >>> tabitha.fight('book')
        True
        """
        return fight_with == self.weakness

    def get_defeated(self):
        """Returns an amount of defeated enemies."""
        self.city.defeated.append(self.name)
        return len(self.city.defeated)


class Boss(Enemy):
    """The most dangerous enemy."""

    def __init__(self, name, description, conversation=None, weakness=None, city=None):
        """
        Receives information about the boss.
        >>> putin = Boss("putin", "A bloody dictator")
        >>> putin.attack
        100
        """
        super().__init__(name, description, conversation, weakness, city)
        self.attack = 100


class Friend(Person):
    """A possitive character that helps protagonist."""

    def __init__(self, name, description, conversation=None, city=None, gift=None):
        """
        Receives data about the friend
        >>> grandma = Friend("Grangma", "True Ukrainian grandma")
        >>> grandma.description
        'True Ukrainian grandma'
        """
        super().__init__(name, description, conversation, city)
        self.gift = gift

    def set_item(self, gift):
        """
        Sets an item for the friend.
        """
        self.gift = gift

    def get_item(self):
        """
        Returns a gift of the friend.
        >>> grandma = Friend("Grangma", "True Ukrainian grandma")
        >>> grandma.set_item(Item("tomato jar"))
        >>> grandma.get_item().item
        'tomato jar'
        """
        return self.gift


class Item:
    """Stores a data about an item."""

    def __init__(self, item, description=None):
        """
        Receives input data of the item.
        >>> book1 = Item("book")
        >>> book1.item
        'book'
        """
        self.item = item
        self.description = description

    def set_description(self, description):
        """
        Sets a description for the item.
        >>> book1 = Item("book")
        >>> book1.set_description("A really good book entitled 'Knitting for dummies'")
        >>> book1.description
        "A really good book entitled 'Knitting for dummies'"
        """
        self.description = description

    def describe(self):
        """Prints description of an item."""
        print(f"The [{self.item}] is here - {self.description}")

    def get_name(self):
        """
        Returns a name of the item.
        >>> book1 = Item("book")
        >>> book1.item == book1.get_name()
        True
        """
        return self.item


class Player:
    """Current player."""

    def __init__(self, name, health: int):
        """
        Receive information about the player.
        >>> player =  Player("Peter", 100)
        >>> player.name
        'Peter'
        >>> player.health
        100
        """
        self.name = name
        self.health = health

    def is_dead(self):
        """Returns True if the player is dead."""
        return self.health <= 0

    def my_health(self):
        """Returnts health level of the player."""
        return self.health

    def damage(self, damage):
        """Changes health of the player after an attack."""
        self.health -= damage


if __name__ == "__main__":
    import doctest
    doctest.testmod()
