#!/usr/bin/env python3

from dataclasses import dataclass, field
from typing import List


@dataclass
class CardAsset:
    asset_id: str
    name: str
    symbol: str
    offchain_price: float = 0.0
    onchain_price: float = 0.0


@dataclass
class PortfolioPosition:
    asset: CardAsset
    quantity: float

    @property
    def value_offchain(self) -> float:
        return self.quantity * self.asset.offchain_price

    @property
    def value_onchain(self) -> float:
        return self.quantity * self.asset.onchain_price


@dataclass
class PortfolioSnapshot:
    positions: List[PortfolioPosition] = field(default_factory=list)

    @property
    def total_offchain_value(self) -> float:
        return sum(position.value_offchain for position in self.positions)

    @property
    def total_onchain_value(self) -> float:
        return sum(position.value_onchain for position in self.positions)

    @property
    def total_value(self) -> float:
        if self.total_onchain_value > 0:
            return self.total_onchain_value
        return self.total_offchain_value
