#!/usr/bin/env python3

import atheris
import sys
import fuzz_helpers

with atheris.instrument_imports(include=['pynmea2']):
    import pynmea2


def TestOneInput(data):
    fdp = fuzz_helpers.EnhancedFuzzedDataProvider(data)
    try:
        if fdp.ConsumeBool():
            should_check = fdp.ConsumeBool()
            msg = pynmea2.parse(fdp.ConsumeRemainingString(), check=should_check)
            repr(msg)
        else:
            data = fuzz_helpers.build_fuzz_tuple(fdp, [str])
            str(pynmea2.GGA('GP', 'GGA', data))
    except pynmea2.ParseError:
        return -1


def main():
    atheris.Setup(sys.argv, TestOneInput)
    atheris.Fuzz()


if __name__ == "__main__":
    main()
