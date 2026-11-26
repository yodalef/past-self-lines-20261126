LINE1 = "Do not trust the deploy button on a Friday at 6:58 PM, no matter how green the tests look."
LINE2 = "That one click cost you a whole weekend, the on-call team's patience, and your faith in the word 'minor'."


def validated_text() -> str:
    text = LINE1.strip() + "\n" + LINE2.strip()
    assert text.count("\n") == 1, "entry must be exactly two lines"
    assert 1 <= len(text) <= 280, f"two lines must total 1-280 characters, got {len(text)}"
    return text


def main() -> None:
    import os
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(validated_text() + "\n")
    print(validated_text())


if __name__ == "__main__":
    main()
