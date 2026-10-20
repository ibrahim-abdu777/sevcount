"""Count lines containing severity-like words."""


def count_severe(lines):
    words = {"error", "fatal", "critical", "alert"}
    return sum(1 for line in lines if any(w in line.lower() for w in words))


def count_file(path):
    with open(path, "r", encoding="utf-8", errors="replace") as handle:
        return count_severe(handle)
