"""Wallet integration stubs."""

class Wallet:
    def __init__(self, keypair_path: str | None = None, initial_balance: float | None = None) -> None:
        self.keypair_path = keypair_path
        # In a real implementation we would load the keypair from the supplied
        # path and establish a connection to a Solana RPC endpoint.  For this
        # example we simply store a mock balance that can be queried by the
        # application.  Allowing ``initial_balance`` to be specified makes the
        # class a little easier to test or demonstrate without additional
        # infrastructure.
        self._balance = float(initial_balance) if initial_balance is not None else 100.0

    def get_balance(self) -> float:
        """Return wallet balance in SOL.

        The balance is a locally stored value and does not reflect real on-chain
        data.  It exists purely to provide a usable API surface for components
        that expect a wallet object.
        """
        return self._balance
