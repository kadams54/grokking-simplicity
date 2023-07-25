import sys
from typing import TypedDict, TypeVar

from .external import get_buy_buttons_dom, set_cart_total_dom, set_tax_dom


class Item(TypedDict):
    name: str
    price: float


T = TypeVar("T")
Cart = list[Item]
shopping_cart: Cart = []


def add_item_to_cart(name: str, price: float) -> None:
    global shopping_cart
    item = make_cart_item(name, price)
    shopping_cart = add_item(shopping_cart, item)
    total = calc_total(shopping_cart)
    set_cart_total_dom(total)
    update_shipping_icons(shopping_cart)
    update_tax_dom(total)


def update_shipping_icons(cart: Cart) -> None:
    buttons = get_buy_buttons_dom()
    for button in buttons:
        item = button.item
        new_cart = add_item(cart, item)
        if gets_free_shipping(new_cart):
            button.show_free_shipping_icon()
        else:
            button.hide_free_shipping_icon()


def update_tax_dom(total: float) -> None:
    set_tax_dom(calc_tax(total))


def add_element_last(array: list[T], item: T) -> list[T]:
    new_array = array[:]
    new_array.append(item)
    return new_array


def add_item(cart: Cart, item: Item) -> Cart:
    return add_element_last(cart, item)


def make_cart_item(name: str, price: float) -> Item:
    return {"name": name, "price": price}


def calc_total(cart: Cart) -> float:
    total = 0
    for item in cart:
        total += item.price
    return total


def gets_free_shipping(cart: Cart) -> bool:
    return calc_total(cart) >= 20


def calc_tax(amount: float) -> float:
    return amount * 0.10


def main() -> int:
    return 0


if __name__ == "__main__":
    sys.exit(main())
