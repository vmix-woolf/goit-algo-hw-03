from stack import Stack


def hanoi_tower(n):
    source = Stack()
    target = Stack()
    auxiliary = Stack()

    for disk in range(n, 0, -1):  # create disks from larger to smaller
        source.push(disk)

    total_moves = 2 ** n - 1

    if n % 2 == 0:
        target, auxiliary = auxiliary, target

    # Iterative decision
    for move in range(1, total_moves + 1):
        if move % 3 == 1:
            move_between(source, target, "Source", "Target")
        elif move % 3 == 2:
            move_between(source, auxiliary, "Source", "Auxiliary")
        elif move % 3 == 0:
            move_between(auxiliary, target, "Auxiliary", "Target")

        print_stacks(source, auxiliary, target)

def print_stacks(source, auxiliary, target):
    print("Source:", source.stack, "Auxiliary:", auxiliary.stack, "Target:", target.stack)
    print("-" * 40)

def move_between(from_stack, to_stack, from_name, to_name):
    if from_stack.is_empty():
        disk = to_stack.pop()
        from_stack.push(disk)
        print(f"Move disk {disk} from {to_name} to {from_name}")
    elif to_stack.is_empty():
        disk = from_stack.pop()
        to_stack.push(disk)
        print(f"Move disk {disk} from {from_name} to {to_name}")
    elif from_stack.peek() > to_stack.peek():
        disk = to_stack.pop()
        from_stack.push(disk)
        print(f"Move disk {disk} from {to_name} to {from_name}")
    else:
        disk = from_stack.pop()
        to_stack.push(disk)
        print(f"Move disk {disk} from {from_name} to {to_name}")


if __name__ == "__main__":
    amount = int(input("Enter disk amount: "))
    hanoi_tower(amount)