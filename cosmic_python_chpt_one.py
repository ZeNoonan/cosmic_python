"""Test test."""
# https://stackoverflow.com/questions/46192576/how-can-i-fix-flake8-d100-missing-docstring-error-in-atom-editor
from dataclasses import dataclass
from datetime import date
from typing import Optional

# customer places order: QTY: 1 x SKU (stock-keeping unit): Red Chair,
# QTY:1 x SKU:Blue Lamp
# with order reference: sale123

# purchasing dept orders small batches of stock from supplier
# QTY:10 x Red Chair and 20 x Blue Lamp with order ref: purch123

# need to allocate sales orders against purchase
# orders to determine 'available quantity' of stock
# rules: 1) Available QTY < sales order 2) can't allocate sales order twice

# also allocate to warehouse stock in preference to shipping stock

# test to determine allocation of batches from sales order

# https://wemake-python-stylegui.de/en/latest/pages/usage/violations/index.html
# https://www.flake8rules.com/
# https://github.com/cosmicpython/code/blob/chapter_01_domain_model/model.py


@dataclass(frozen=True)
class Orderline(object):
    """missing docstring in public class D101."""

    qty: int
    sku: str
    orderid: str


class Batch(object):  # explicit base class notation
    """missing docstring in public class D101."""

    def __init__(self, qty: int, ref: str, sku: str, eta: Optional[date]):
        """Missing docstring in public class D101.

        Args:
            qty: test
            ref: test
            sku: test
            eta: test
        """
        self.reference = ref
        self.available_quantity = qty
        self.sku = sku
        self.eta = eta

    def allocate(self, line: Orderline):
        """Missing docstring in public class.

        Args:
            line: test
        """
        self.available_quantity = self.available_quantity - line.qty


def test_allocate_order_against_batches():
    """Missing docstring in public class D101."""
    stock_hand = 20
    test_quantity = 18
    line = Orderline(qty=2, sku='SMALL-TABLE', orderid='Order-001')
    batch = Batch(
        qty=stock_hand, 
        sku='SMALL-TABLE',
        ref='Batch-001',
        eta=date.today(),
        )
    batch.allocate(line)
    # https://medium.com/@cjolowicz/hypermodern-python-3-linting-e2f15708da80
    # disable assert flag in test suite per article
    assert batch.available_quantity == test_quantity
