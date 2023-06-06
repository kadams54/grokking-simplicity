#!/usr/bin/env python3

import sys
from string import Template
from typing import Callable, TypedDict
from collections.abc import Iterable


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


def create_email(coupons: Iterable[Coupon]) -> Callable[[Person], Email]:
    codes = ", ".join((c["coupon"] for c in coupons))

    def mapper(p: Person) -> Email:
        return {
            "to": p["email"],
            "body": EMAIL_CONTENT.substitute(codes=", ".join(codes)),
        }

    return mapper


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


def main() -> int:
    good_coupons = filter(is_good, COUPONS_TABLE)
    create_good_email = create_email(good_coupons)
    people_getting_good_coupons = filter(gets_good_coupons, PERSONS_TABLE)
    good_emails = map(create_good_email, people_getting_good_coupons)

    best_coupons = filter(is_best, COUPONS_TABLE)
    create_best_email = create_email(best_coupons)
    people_getting_best_coupons = filter(gets_best_coupons, PERSONS_TABLE)
    best_emails = map(create_best_email, people_getting_best_coupons)

    for email in [*good_emails, *best_emails]:
        send(email)
    return 0


if __name__ == "__main__":
    sys.exit(main())
