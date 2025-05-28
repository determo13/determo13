# determo13

This project provides a basic skeleton for an arbitrage trading app on Solana.
It demonstrates the overall structure, including a CLI and configuration, but
the trading logic is intentionally simplistic.  The scanner, executor and
wallet modules ship with minimal implementations so the application can run
without raising ``NotImplementedError`` while still leaving plenty of room for
real integration work.

## Usage

Run the CLI in test mode:

```bash
python app.py --mode test
```

By default the application uses a bundled dummy dataset.  To fetch live market
quotes via Jupiter's API in an environment that has Internet access, pass the
``--data-source live`` option:

```bash
python app.py --mode test --data-source live
```

The command-line interface and module stubs can be extended to integrate the
Jupiter aggregator API, Helius data sources, and real trade execution.
