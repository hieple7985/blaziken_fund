#!/usr/bin/env python3

from dataclasses import dataclass

from .config import AppConfig
from .domain import PortfolioSnapshot
from .strategy import BlazikenStrategy
from .base_adapter import BaseChainAdapter


@dataclass
class BlazikenAgent:
    config: AppConfig
    adapter: BaseChainAdapter
    strategy: BlazikenStrategy = BlazikenStrategy()

    @classmethod
    def from_config(cls, config: AppConfig) -> "BlazikenAgent":
        adapter = BaseChainAdapter(config=config)
        return cls(config=config, adapter=adapter)

    def load_portfolio(self) -> PortfolioSnapshot:
        return self.adapter.load_portfolio_snapshot()

    def run_cycle(self) -> PortfolioSnapshot:
        snapshot = self.load_portfolio()
        return self.strategy.rebalance(snapshot)
