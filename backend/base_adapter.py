#!/usr/bin/env python3

from dataclasses import dataclass

from .config import AppConfig
from .domain import PortfolioSnapshot


@dataclass
class BaseChainAdapter:
    config: AppConfig

    def load_portfolio_snapshot(self) -> PortfolioSnapshot:
        return PortfolioSnapshot()
