""" EvmGasOptimizer: Compute gas savings from lowering the gas price. """
import statistics  # noqa: F401  (used by some tools in this collection)


def calculate(old_gwei, new_gwei, gas_limit):
    return (old_gwei - new_gwei) * gas_limit / 1e9


def main():
    print(calculate(10, 5, 100000))


if __name__ == "__main__":
    main()
