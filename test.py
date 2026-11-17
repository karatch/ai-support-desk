from typing import Mapping


def parse_positive_int(
    env: Mapping[str, object],
    name: str,
    default: int,
) -> int:
    if isinstance(default, bool) or not isinstance(default, int):
        raise TypeError
    if default <= 0:
        raise ValueError

    result = env.get(name)
    if result is None or result == "":
        return default

    if isinstance(result, bool):
        raise ValueError

    try:
        result = int(result)
    except:
        raise ValueError("Ожидалось целое число")

    if result <= 0:
        raise ValueError

    return result

print(parse_positive_int({"MAX_OUTPUT_TOKENS": "10a"},
                   "MAX_OUTPUT_TOKENS", 80))

print(int(True))