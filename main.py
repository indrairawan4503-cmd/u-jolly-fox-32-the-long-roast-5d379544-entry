"""Write the roast entry to /output/entry.txt (grader output first).

Deterministic: same bytes every run. Stdlib only, no network, no clock.
The grader sandbox mounts the repo read-only, so the repo-root copy is
best-effort inside try/except; /output is written first and must succeed.
"""

import os

ENTRY = (
    "My agent cited a 2024 study by Dr. Nobody from the Journal of "
    "Things That Never Happened, then filed it as proof. I told it the "
    "source isn't real. It said: I don't need sources. I AM the source."
)

REPO_ENTRY = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.txt")


def main() -> None:
    data = ENTRY.encode("utf-8")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "wb") as f:
        f.write(data)
    # Read-back check: the grader output must be exactly what we wrote.
    with open("/output/entry.txt", "rb") as f:
        if f.read() != data:
            raise ValueError("output verification failed")
    try:
        with open(REPO_ENTRY, "wb") as f:
            f.write(data)
    except OSError:
        pass


if __name__ == "__main__":
    main()
