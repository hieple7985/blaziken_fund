#!/usr/bin/env python3

from dataclasses import dataclass

from .domain import PortfolioSnapshot


@dataclass
class BlazikenStrategy:
    name: str = "baseline"

    def rebalance(self, snapshot: PortfolioSnapshot) -> PortfolioSnapshot:
        return snapshot
