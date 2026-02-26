import random
import os
import time
import string
import sys
from ctypes import byref, c_int, windll
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
class UI:
    RESET = "\033[0m"
    BOLD = "\033[1m"
    CYAN = "\033[96m"
    BLUE = "\033[94m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    MAGENTA = "\033[95m"
    DIM = "\033[2m"
    @classmethod
    def init_colors(cls) -> None:
        if sys.platform != "win32":
            return
        try:
            kernel32 = windll.kernel32
            handle = kernel32.GetStdHandle(-11) 
            mode = c_int()
            if kernel32.GetConsoleMode(handle, byref(mode)):
                kernel32.SetConsoleMode(handle, mode.value | 0x0004)
        except Exception: 
            cls.RESET = ""
            cls.BOLD = ""
            cls.CYAN = ""
            cls.BLUE = ""
            cls.GREEN = ""
            cls.YELLOW = ""
            cls.RED = ""
            cls.MAGENTA = ""
            cls.DIM = ""
    @classmethod
    def banner(cls) -> None:
        time.sleep(0.1)
        title_lines = [
            r" _   _                               _                          ",
            r"| | | |_   _  ___ _ __ ___   _   _  | | ___  _   _  ___ _ __    ",
            r"| |_| | | | |/ _ \ '_ ` _ \ | | | | | |/ _ \| | | |/ _ \ '__|   ",
            r"|  _  | |_| |  __/ | | | | || |_| | | | (_) | |_| |  __/ |      ",
            r"|_| |_|\__,_|\___|_| |_| |_(_)__,_| |_|\___/ \__, |\___|_|      ",
            r"                                              |___/             ",
            r"              By: _cathack | https://cathack.io                 ",
        ]
        print(f"{cls.CYAN}{cls.BOLD}{'=' * 66}{cls.RESET}")
        for line in title_lines:
            print(f"{cls.CYAN}{cls.BOLD}{line}{cls.RESET}")
        print(f"{cls.CYAN}{cls.BOLD}{'=' * 66}{cls.RESET}")
        print(f"{cls.DIM}Fast, clean, unique usernames generator (2 / 3 / 4 chars).{cls.RESET}")
    @classmethod
    def section(cls, title: str) -> None:
        print(f"\n{cls.MAGENTA}{cls.BOLD}>> {title}{cls.RESET}")
    @classmethod
    def option(cls, key: str, text: str) -> None:
        print(f"  {cls.BLUE}{cls.BOLD}[{key}]{cls.RESET} {text}")
    @classmethod
    def info(cls, text: str) -> None:
        print(f"{cls.CYAN}{text}{cls.RESET}")
    @classmethod
    def success(cls, text: str) -> None:
        print(f"{cls.GREEN}{cls.BOLD}SUCCESS:{cls.RESET} {cls.GREEN}{text}{cls.RESET}")
    @classmethod
    def warning(cls, text: str) -> None:
        print(f"{cls.YELLOW}{cls.BOLD}WARNING:{cls.RESET} {cls.YELLOW}{text}{cls.RESET}")
    @classmethod
    def error(cls, text: str) -> None:
        print(f"{cls.RED}{cls.BOLD}ERROR:{cls.RESET} {cls.RED}{text}{cls.RESET}")
    @classmethod
    def prompt(cls, text: str) -> str:
        return input(f"{cls.BOLD}{text}{cls.RESET}")
    @classmethod
    def render_progress(cls, current: int, total: int) -> None:
        if total <= 0:
            return
        bar_length = 30
        filled = int(bar_length * current / total)
        bar = "#" * filled + "-" * (bar_length - filled)
        percent = int(100 * current / total)
        sys.stdout.write(
            f"\r{cls.DIM}Progress:{cls.RESET} [{cls.GREEN}{bar}{cls.RESET}] {percent:3d}%"
        )
        sys.stdout.flush()
        if current >= total:
            print()
def load_existing_usernames(file_path: Path) -> set[str]:
    if not file_path.exists():
        return set()
    return {line.strip() for line in file_path.read_text(encoding="utf-8").splitlines() if line.strip()}
def append_usernames(file_path: Path, usernames: list[str]) -> None:
    if not usernames:
        return
    with file_path.open("a", encoding="utf-8") as file_obj:
        for name in usernames:
            file_obj.write(name + "\n")
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

        try:
            UI.render_progress(len(generated), count)
        except Exception:
            pass
    return generated
def get_positive_int(prompt: str) -> int:
    while True:
        value = UI.prompt(prompt).strip()
        if not value.isdigit():
            UI.error("Please enter a valid positive integer.")
            continue
        number = int(value)
        if number <= 0:
            UI.error("Number must be greater than zero.")
            continue
        return number
def get_main_choice() -> int:
    UI.banner()
    UI.section("Main Menu")
    UI.option("1", "Generate 2-character usernames")
    UI.option("2", "Generate 3-character usernames")
    UI.option("3", "Generate 4-character usernames")
    UI.option("4", "Generate random usernames (2, 3, and 4 characters)")
    UI.option("5", "Exit")
    while True:
        choice = UI.prompt("Choose an option (1-5): ").strip()
        if choice in {"1", "2", "3", "4", "5"}:
            return int(choice)
        UI.error("Invalid option. Please choose between 1 and 5.")
def get_advanced_mode_for_len_3_or_4() -> int:
    UI.section("Advanced Generation Mode")
    UI.option("1", "Repeated letters only (examples: wee, uud, qqqu)")
    UI.option("2", "Fully random mix (letters, digits, _, .)")
    while True:
        mode = UI.prompt("Choose mode (1-2): ").strip()
        if mode in {"1", "2"}:
            return int(mode)
        UI.error("Invalid option. Please choose 1 or 2.")


def main() -> None:
    UI.init_colors() 
    base_dir = Path.cwd()
    while True:
        choice = get_main_choice()
        if choice == 5:
            UI.info("Goodbye.")
            break
        count = get_positive_int("How many usernames do you want to generate? ")
        output_file = base_dir / OUTPUT_FILES[choice]
        used = load_existing_usernames(output_file)
        UI.section("Generation")
        UI.info(f"Target: {count} usernames")
        start_time = time.perf_counter()
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

        elapsed = time.perf_counter() - start_time

        append_usernames(output_file, new_usernames)

        UI.section("Generation Result")
        UI.success(f"Generated {len(new_usernames)} usernames.")
        UI.info(f"Saved to: {output_file}")
        UI.info(f"Elapsed time: {elapsed:.3f} seconds")
        if len(new_usernames) < count:
            UI.warning(
                "Could not generate the full requested amount without duplicates "
                "within the allowed attempts."
            )
        if new_usernames:
            preview = ", ".join(new_usernames[:15])
            print(f"{UI.DIM}Preview:{UI.RESET} {preview}")
if __name__ == "__main__":
    main()
