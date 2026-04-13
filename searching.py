import json
import random
import time
import matplotlib.pyplot as plt


# =========================
# READ DATA
# =========================
def read_data(filename, field):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)
    except:
        return None

    return data.get(field, None)


# =========================
# LINEAR SEARCH
# =========================
def linear_search(sequence, target):
    positions = []

    for index, value in enumerate(sequence):
        if value == target:
            positions.append(index)

    return {
        "positions": positions,
        "count": len(positions)
    }


# =========================
# BINARY SEARCH
# =========================
def binary_search(sequence, target):
    left = 0
    right = len(sequence) - 1

    while left <= right:
        mid = (left + right) // 2

        if sequence[mid] == target:
            return mid
        elif sequence[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return None


# =========================
# GENERATOR DAT
# =========================
def generate_sequence(size):
    return [random.randint(0, size) for _ in range(size)]


# =========================
# MERENI CASU
# =========================
def measure_time(func, data, target, repeat=5):
    times = []

    for _ in range(repeat):
        start = time.perf_counter()
        func(data, target)
        end = time.perf_counter()
        times.append(end - start)

    return sum(times) / len(times)


# =========================
# MAIN
# =========================
def main():
    print("=" * 50)
    print("NAČÍTÁNÍ DAT")
    print("=" * 50)

    data = read_data("sequential.json", "unordered_numbers")
    print("Data:", data)

    target = 5
    print("Hledane cisslo:", target)

    print("\n" + "=" * 50)
    print("LINEÁRNÍ VYHLEDÁVÁNÍ")
    print("=" * 50)

    result = linear_search(data, target)
    print(result)

    print("\n" + "=" * 50)
    print("BINÁRNÍ VYHLEDÁVÁNÍ")
    print("=" * 50)

    if data is None:
        print("Chyba dat")
        return

    sorted_data = sorted(data)
    index = binary_search(sorted_data, target)

    print("Seřazená data:", sorted_data)
    print("Index:", index)

    # =========================
    # POROVNÁNÍ ALGORITMŮ
    # =========================
    print("\n" + "=" * 50)
    print("POROVNÁNÍ RYCHLOSTI")
    print("=" * 50)

    sizes = [100, 500, 1000, 5000, 10000]

    linear_times = []
    binary_times = []
    set_times = []

    for size in sizes:
        seq = generate_sequence(size)

        # linear
        t1 = measure_time(linear_search, seq, target)
        linear_times.append(t1)

        # binary (musí být seřazený)
        sorted_seq = sorted(seq)
        t2 = measure_time(binary_search, sorted_seq, target)
        binary_times.append(t2)

        # set
        s = set(seq)
        t3 = measure_time(lambda d, x: x in d, s, target)
        set_times.append(t3)

        print(f"Velikost {size}: linear={t1:.6f}, binary={t2:.6f}, set={t3:.6f}")

    # =========================
    # GRAF
    # =========================
    plt.figure()

    plt.plot(sizes, linear_times, label="Linear search")
    plt.plot(sizes, binary_times, label="Binary search")
    plt.plot(sizes, set_times, label="Set")

    plt.xlabel("Velikost vstupu (n)")
    plt.ylabel("Čas (s)")
    plt.title("Porovnání vyhledávacích algoritmů")

    plt.legend()
    plt.grid()

    plt.show()


if __name__ == "__main__":
    main()