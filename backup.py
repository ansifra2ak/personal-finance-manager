
import os
import shutil
from datetime import datetime
from storage import FILE_NAME

BACKUP_FOLDER = "backups"


def create_backup():
    if not os.path.exists(FILE_NAME):
        print("No expense file found to back up.")
        return

    os.makedirs(BACKUP_FOLDER, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_name = f"expenses_backup_{timestamp}.csv"
    backup_path = os.path.join(BACKUP_FOLDER, backup_name)

    shutil.copy2(FILE_NAME, backup_path)

    print(f"Backup created successfully: {backup_path}")


def restore_backup():
    if not os.path.exists(BACKUP_FOLDER):
        print("No backups available.")
        return

    backups = sorted(
        [
            file for file in os.listdir(BACKUP_FOLDER)
            if file.endswith(".csv")
        ],
        reverse=True
    )

    if not backups:
        print("No backups available.")
        return

    print("\nAvailable Backups:")

    for index, backup in enumerate(backups, start=1):
        print(f"{index}. {backup}")

    try:
        choice = int(input("Select backup number: "))

        if choice < 1 or choice > len(backups):
            print("Invalid backup number.")
            return

        selected_backup = os.path.join(
            BACKUP_FOLDER, backups[choice - 1]
        )

        confirmation = input(
            "This will replace current expenses. Continue? (yes/no): "
        ).strip().lower()

        if confirmation != "yes":
            print("Restore cancelled.")
            return

        shutil.copy2(selected_backup, FILE_NAME)
        print("Expenses restored successfully!")

    except ValueError:
        print("Please enter a valid number.")
    except OSError as error:
        print(f"Restore failed: {error}")
