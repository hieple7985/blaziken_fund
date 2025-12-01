#!/usr/bin/env python3

from dataclasses import dataclass
import os


@dataclass
class AppConfig:
    environment: str
    base_rpc_url: str

    @classmethod
    def from_env(cls) -> "AppConfig":
        return cls(
            environment=os.getenv("BLAZIKEN_ENV", "dev"),
            base_rpc_url=os.getenv("BASE_RPC_URL", ""),
        )
