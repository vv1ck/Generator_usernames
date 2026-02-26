import random
import string
from pathlib import Path


LETTERS = string.ascii_lowercase
DIGITS = string.digits
START_END_CHARS = LETTERS + DIGITS + "_"
MIDDLE_CHARS = LETTERS + DIGITS + "_."
OUTPUT_FILES = {
    1: "usernames_2_chars.txt",
    2: "usernames_3_chars.txt",
    3: "usernames_4_chars.txt",
    4: "usernames_random_2_3_4.txt",
}
def load_existing_usernames(file_path: Path) -> set[str]:
    if not file_path.exists():
        return set()
    return {line.strip() for line in file_path.read_text(encoding="utf-8").splitlines() if line.strip()}
def append_usernames(file_path: Path, usernames: list[str]) -> None:
    if not usernames:
        return
    with file_path.open("a", encoding="utf-8") as f:
        for name in usernames:
            f.write(name + "\n")
def generate_mixed_username(length: int) -> str:
    if length < 2:
        raise ValueError("Length must be >= 2.")
    first = random.choice(START_END_CHARS)
    middle = "".join(random.choice(MIDDLE_CHARS) for _ in range(length - 2))
    last = random.choice(START_END_CHARS)
    return first + middle + last
def generate_repeated_letters_username(length: int) -> str:
    if length < 2:
        raise ValueError("Length must be >= 2.")
    while True:
        candidate = "".join(random.choice(LETTERS) for _ in range(length)) 
        if len(set(candidate)) < length:
            return candidate
def generate_usernames(
    count: int,
    used: set[str],
    chooser,
    max_attempts_factor: int = 50,
) -> list[str]:
    generated: list[str] = []
    attempts = 0
    max_attempts = max(10000, count * max_attempts_factor)

    while len(generated) < count and attempts < max_attempts:
        attempts += 1
        candidate = chooser()
        if candidate in used:
            continue
        used.add(candidate)
        generated.append(candidate)

    return generated
def get_positive_int(prompt: str) -> int:
    while True:
        value = input(prompt).strip()
        if not value.isdigit():
            print("Please enter a valid positive integer.")
            continue
        number = int(value)
        if number <= 0:
            print("Number must be greater than zero.")
            continue
        return number
def get_main_choice() -> int:
    print("\n=== Username Generator ===")
    print("1) Generate 2-character usernames")
    print("2) Generate 3-character usernames")
    print("3) Generate 4-character usernames")
    print("4) Generate random usernames (2, 3, and 4 characters)")
    print("5) Exit")
    while True:
        choice = input("Choose an option (1-5): ").strip()
        if choice in {"1", "2", "3", "4", "5"}:
            return int(choice)
        print("Invalid option. Please choose between 1 and 5.")
def get_advanced_mode_for_len_3_or_4() -> int:
    print("\nAdvanced generation mode:")
    print("1) Repeated letters only (examples: wee, uud, qqqu)")
    print("2) Fully random mix (letters, digits, _, .)")
    while True:
        mode = input("Choose mode (1-2): ").strip()
        if mode in {"1", "2"}:
            return int(mode)
        print("Invalid option. Please choose 1 or 2.")
def main() -> None:
    base_dir = Path(__file__).resolve().parent
    while True:
        choice = get_main_choice()
        if choice == 5:
            print("Goodbye.")
            break
        count = get_positive_int("How many usernames do you want to generate? ")
        output_file = base_dir / OUTPUT_FILES[choice]
        used = load_existing_usernames(output_file)
        if choice == 1:
            new_usernames = generate_usernames(
                count=count,
                used=used,
                chooser=lambda: generate_mixed_username(2),
            )
        elif choice == 2:
            mode = get_advanced_mode_for_len_3_or_4()
            if mode == 1:
                new_usernames = generate_usernames(
                    count=count,
                    used=used,
                    chooser=lambda: generate_repeated_letters_username(3),
                )
            else:
                new_usernames = generate_usernames(
                    count=count,
                    used=used,
                    chooser=lambda: generate_mixed_username(3),
                )
        elif choice == 3:
            mode = get_advanced_mode_for_len_3_or_4()
            if mode == 1:
                new_usernames = generate_usernames(
                    count=count,
                    used=used,
                    chooser=lambda: generate_repeated_letters_username(4),
                )
            else:
                new_usernames = generate_usernames(
                    count=count,
                    used=used,
                    chooser=lambda: generate_mixed_username(4),
                )
        else:
            new_usernames = generate_usernames(
                count=count,
                used=used,
                chooser=lambda: generate_mixed_username(random.choice((2, 3, 4))),
            )
        append_usernames(output_file, new_usernames)
        print(f"\nGenerated {len(new_usernames)} usernames.")
        print(f"Saved to: {output_file.name}")
        if len(new_usernames) < count:
            print(
                "Warning: Could not generate the full requested amount without duplicates "
                "within the allowed attempts."
            )
        if new_usernames:
            preview = ", ".join(new_usernames[:15])
            print(f"Preview: {preview}")
if __name__ == "__main__":
    main()
