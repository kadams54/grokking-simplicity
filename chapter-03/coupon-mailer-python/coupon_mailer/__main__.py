#!/usr/bin/env python3

import sys
from string import Template
from typing import TypedDict
from collections.abc import Iterable

from pydash import py_


class Person(TypedDict):
    email: str
    rec_count: int


class Coupon(TypedDict):
    coupon: str
    rank: str


class Email(TypedDict):
    to: str
    body: str


PERSONS_TABLE: list[Person] = [
    {"email": "john@coldmail.com", "rec_count": 2},
    {"email": "sam@pmail.co", "rec_count": 16},
    {"email": "linda1989@oal.com", "rec_count": 1},
    {"email": "jan1940@ahoy.com", "rec_count": 0},
    {"email": "mrbig@pmail.co", "rec_count": 25},
    {"email": "lol@lol.lol", "rec_count": 0},
]

COUPONS_TABLE: list[Coupon] = [
    {"coupon": "MAYDISCOUNT", "rank": "good"},
    {"coupon": "10PERCENT", "rank": "bad"},
    {"coupon": "PROMOTION45", "rank": "best"},
    {"coupon": "IHEARTYOU", "rank": "bad"},
    {"coupon": "GETADEAL", "rank": "best"},
    {"coupon": "ILIKEDISCOUNTS", "rank": "good"},
]

EMAIL_CONTENT = Template("Hello! Here are some coupons you might like: $codes")

# ======================================================================
# CALCULATIONS
# ======================================================================


def _create_email(coupons: Iterable[Coupon], p: Person) -> Email:
    codes = py_(coupons).pluck("coupon").join(", ").value()
    return {
        "to": p["email"],
        "body": EMAIL_CONTENT.substitute(codes=codes),
    }


create_email = py_.curry(_create_email)


def is_good(coupon: Coupon) -> bool:
    return coupon["rank"] == "good"


def is_best(coupon: Coupon) -> bool:
    return coupon["rank"] == "best"


def gets_good_coupons(person: Person) -> bool:
    return person["rec_count"] < 10


def gets_best_coupons(person: Person) -> bool:
    return person["rec_count"] >= 10


# ======================================================================
# ACTIONS
# ======================================================================


def send(email: Email) -> None:
    print(f"📧 Sending: {email}")


def fetch_persons() -> Iterable[Person]:
    return PERSONS_TABLE


def fetch_coupons() -> Iterable[Coupon]:
    return COUPONS_TABLE


def main() -> int:
    coupons = py_(fetch_coupons())
    persons = py_(fetch_persons())

    good_coupons = coupons.filter(is_good).value()
    create_good_email = create_email(good_coupons)
    good_emails = persons.filter(gets_good_coupons).map(create_good_email).value()

    best_coupons = coupons.filter(is_best).value()
    create_best_email = create_email(best_coupons)
    best_emails = persons.filter(gets_best_coupons).map(create_best_email).value()

    for email in [*good_emails, *best_emails]:
        send(email)
    return 0


if __name__ == "__main__":
    sys.exit(main())
