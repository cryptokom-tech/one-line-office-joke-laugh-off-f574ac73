import os

JOKE = "I suggested removing our office suggestion box. It won employee of the month."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE)
    with open(path, encoding="utf-8") as f:
        written = f.read()
    assert written == JOKE
    assert 1 <= len(written) <= 200
    assert written.strip()
    assert "\n" not in written


if __name__ == "__main__":
    main()
