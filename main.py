from pathlib import Path

ENTRY = "Four stars: he invades my yard daily and still owes the cheese tax, but today he dropped a biscuit and surrendered to the fence."


def main() -> None:
    output = Path("/output/entry.txt")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(ENTRY + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
