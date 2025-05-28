"""Wallet integration stubs."""

class Wallet:
    def __init__(self, keypair_path: str | None = None) -> None:
        self.keypair_path = keypair_path
        # TODO: load keypair and connect to Solana

    def get_balance(self) -> float:
        """Return wallet balance in SOL.

        This is a stub that would normally query the Solana RPC.
        """
        raise NotImplementedError("Wallet balance fetch not implemented")
