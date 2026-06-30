"""
DroneScan - Edge Deployment Bundler (skeleton)

Packages the quantized model + runtime into a deployable bundle for
edge targets (e.g. Jetson, Coral, Raspberry Pi). See docs/chapter11.
"""
import argparse


def build_bundle(target: str):
    """Build an edge deployment bundle for the given target device.

    TODO:
        - Quantize/optimize the model for the target (see docs/chapter5)
        - Package runtime dependencies
        - Output a self-contained bundle directory
    """
    raise NotImplementedError(f"Implement edge bundle builder for target={target} — see docs/chapter11")


def main():
    parser = argparse.ArgumentParser(description="Build a DroneScan edge deployment bundle")
    parser.add_argument("--target", required=True, choices=["jetson", "coral", "raspberry-pi", "generic"])
    args = parser.parse_args()
    build_bundle(args.target)


if __name__ == "__main__":
    main()
