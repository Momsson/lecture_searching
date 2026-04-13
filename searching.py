import json
import random
import time
import matplotlib.pyplot as plt

# READ DATA
def read_data(filename, field):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)
    except:
        return None

    return data.get(field, None)


# LINEAR SEARCH
def linear_search(sequence, target):
    positions = [] #1

    for index, value in enumerate(sequence): #n
        if value == target: #n
            positions.append(index) # nejlepsi(0) vs nejhorsi pripad (n)

    return {
        "positions": positions,
        "count": len(positions)
    } #1
# Narocnost 3n + 2 nejhorsi
# Narocnost 2n + 2 nejlepsi

# BINARY SEARCH
def binary_search(sequence, target):
    left = 0 #1
    right = len(sequence) - 1 #1

    while left <= right: #n alebo 1
        mid = (left + right) // 2 #n alebo 1

        if sequence[mid] == target: #n alebo 1
            return mid #1
        elif sequence[mid] < target: #n
            left = mid + 1 #n
        else: #n
            right = mid - 1 #n

    return None #1
# 7n + 2 nejhorsi (neexistujuca)
# 6 nejlepsi

# PATTERN SEARCH (DNA)

def pattern_search(sequence, pattern):
    positions = []
    n = len(sequence)
    m = len(pattern)

    for i in range(n - m + 1):
        if sequence[i:i+m] == pattern:
            positions.append(i)

    return positions

# GENERATOR DAT

def generate_sequence(size):
    return [random.randint(0, size) for _ in range(size)]


# MERENI CASU
def measure_time(func, data, target, repeat=5):
    times = []

    for _ in range(repeat):
        start = time.perf_counter()
        func(data, target)
        end = time.perf_counter()
        times.append(end - start)

    return sum(times) / len(times)

# MAIN
def main():
    print("=" * 50)
    print("NAČÍTÁNÍ DAT")
    print("=" * 50)

    data = read_data("sequential.json", "unordered_numbers")
    dna_sequence = read_data("sequential.json", "dna_sequence")

    print("Číselná data:", data)
    print("DNA sekvence:", dna_sequence)

    target = 0
    print("\nHledané číslo:", target)

    print("\n" + "_" * 50)
    print("LINEÁRNÍ VYHLEDÁVÁNÍ")
    print("=" * 50)

    result = linear_search(data, target)
    print(result)

    print("\n" + "_" * 50)
    print("BINÁRNÍ VYHLEDÁVÁNÍ")
    print("=" * 50)

    if data is None:
        print("Chyba dat")
        return

    sorted_data = sorted(data)
    index = binary_search(sorted_data, target)

    print("Index:", index)

    print("\n" + "_" * 50)
    print("PATTERN SEARCH (DNA)")
    print("=" * 50)

    pattern = "ATA"
    print("Hledaný vzor:", pattern)

    if dna_sequence is not None:
        positions = pattern_search(dna_sequence, pattern)
        print("Pozice výskytu:", positions)
    else:
        print("DNA sekvence nenalezena")


    # POROVNÁNÍ ALGORITMŮ

    print("\n" + "_" * 50)
    print("POROVNÁNÍ RYCHLOSTI")
    print("=" * 50)

    sizes = [100, 500, 1000, 5000, 10000]

    linear_times = []
    binary_times = []
    set_times = []

    for size in sizes:
        seq = generate_sequence(size)

        t1 = measure_time(linear_search, seq, target)
        linear_times.append(t1)

        sorted_seq = sorted(seq)
        t2 = measure_time(binary_search, sorted_seq, target)
        binary_times.append(t2)

        s = set(seq)
        t3 = measure_time(lambda d, x: x in d, s, target)
        set_times.append(t3)

        print(f"{size}: linear={t1:.8f}, binary={t2:.8f}, set={t3:.8f}")

    # GRAF
    plt.figure()

    plt.plot(sizes, linear_times, label="Linear search")
    plt.plot(sizes, binary_times, label="Binary search")
    plt.plot(sizes, set_times, label="Set")

    plt.xlabel("Velikost vstupu (n)")
    plt.ylabel("Čas (s)")
    plt.title("Porovnání algoritmů vyhledávání")

    plt.legend()
    plt.grid()

    plt.show()


if __name__ == "__main__":
    main()