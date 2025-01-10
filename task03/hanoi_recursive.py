def hanoi_recursive(n, source, target, auxiliary, towers):
    if n == 1:
        disk = towers[source].pop()
        towers[target].append(disk)
        print(f"Move disk {disk} from {source} to {target}")
        print_towers(towers)
        return

    hanoi_recursive(n - 1, source, auxiliary, target, towers)
    disk = towers[source].pop()
    towers[target].append(disk)
    print(f"Move disk {disk} from {source} to {target}")
    print_towers(towers)
    hanoi_recursive(n - 1, auxiliary, target, source, towers)

def print_towers(towers):
    print(" ".join(f"{name}: {stack}" for name, stack in towers.items()))
    print("-" * 40)

if __name__ == "__main__":
    amount = int(input("Enter disk amount: "))
    turrets = {
        "Source": list(range(amount, 0, -1)),
        "Target": [],
        "Auxiliary": []
    }
    print_towers(turrets)
    hanoi_recursive(amount, "Source", "Target", "Auxiliary", turrets)
