def main():
    todos = []

    while True:
        cmd = input("\n[a]dd  [l]ist  [d]one  [q]uit > ").strip().lower()

        if cmd == "a":
            task = input("Task: ").strip()
            if task:
                todos.append({"task": task, "done": False})
                print("Added.")
        elif cmd == "l":
            if not todos:
                print("No tasks yet.")
            for i, t in enumerate(todos, 1):
                mark = "✓" if t["done"] else " "
                print(f"{i:>2}. [{mark}] {t['task']}")
        elif cmd == "d":
            if not todos:
                print("Nothing to mark done.")
                continue
            try:
                idx = int(input("Task number: "))
                todos[idx - 1]["done"] = True
                print("Done.")
            except (ValueError, IndexError):
                print("Invalid number.")
        elif cmd == "q":
            break
        else:
            print("Unknown command.")

if __name__ == "__main__":
    main()
