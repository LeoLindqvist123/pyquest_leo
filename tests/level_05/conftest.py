import pytest

from dungeon.shop import Listing, NotEnoughGoldError, OutOfStockError, Shop
from dungeon.hero import Hero
from dungeon.inventory import Inventory, Item

@pytest.fixture
def hero():
    hero = Hero("Leo")
    return hero

@pytest.fixture
def backpack():
    backpack = Inventory()
    return backpack

@pytest.fixture
def rich_hero(hero):
    hero.gold = 1000
    return hero

@pytest.fixture
def shop():
    blacksmith_s = Item("Sword", 5, 7)
    blacksmith_a = Item("Armor", 10, 9)
    food = Item("fläsk", 2, 1)
    return Shop([
        Listing(blacksmith_s, 35, 25),
        Listing(blacksmith_a, 55, 45),
        Listing(food, 5, 1)
    ])

@pytest.fixture
def full_backpack():
    full_backpack = Inventory(max_weight=4)
    return full_backpack