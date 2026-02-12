from utils import *
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

console = Console()

def show_expenses(data):
    if not data:
        console.print("[red]Xarajat yo‘q[/red]")
        return

    table = Table(title="Xarajatlar")

    table.add_column("ID", style="cyan")
    table.add_column("Nomi", style="green")
    table.add_column("Summa", style="yellow")
    table.add_column("Kategoriya", style="magenta")

    total = 0

    for i, e in enumerate(data, 1):
        table.add_row(str(i), e["title"], str(e["amount"]), e["category"])
        total += e["amount"]

    console.print(table)
    console.print(f"[bold green]Jami: {total}$[/bold green]")

def category_stats(data):
    stats = {}
    for e in data:
        stats[e["category"]] = stats.get(e["category"], 0) + e["amount"]

    table = Table(title="Kategoriya bo‘yicha")

    table.add_column("Kategoriya", style="magenta")
    table.add_column("Summa", style="yellow")

    for k, v in stats.items():
        table.add_row(k, str(v))

    console.print(table)

def main():
    data = load_data()

    while True:
        console.print(Panel.fit("💰 EXPENSE TRACKER", style="bold blue"))

        console.print("1. Ko‘rish")
        console.print("2. Qo‘shish")
        console.print("3. Statistika")
        console.print("0. Chiqish")

        choice = input("Tanla: ")

        if choice == "1":
            show_expenses(data)

        elif choice == "2":
            title = input("Nomi: ")
            amount = float(input("Summa: "))
            category = input("Kategoriya: ")
            add_expense(data, title, amount, category)
            console.print("[green]Qo‘shildi![/green]")

        elif choice == "3":
            category_stats(data)

        elif choice == "0":
            break

        else:
            console.print("[red]Xato tanlov[/red]")

if __name__ == "__main__":
    main()
