# src/cli_app.py
import sys
import os
sys.path.append(os.path.dirname(__file__))

from kb_car_diag import run_engine_with_inputs, explain

def ask_choice(prompt, choices):
    s = f"{prompt} {choices}: "
    while True:
        ans = input(s).strip().lower()
        if ans in choices:
            return ans
        print(f"Please enter one of {choices}")

def main():
    print("=== Car No-Start Expert System (CLI) ===")
    ec = ask_choice("Does the engine crank?", {"yes", "no"})
    hd = ask_choice("Are the headlights dim?", {"yes", "no"})
    fg = ask_choice("Fuel gauge level?", {"empty", "low", "ok"})
    cn = ask_choice("Clicking noise when starting?", {"yes", "no"})
    temp = ask_choice("Ambient temperature?", {"cold", "normal", "hot"})

    hypos, trace = run_engine_with_inputs(ec, hd, fg, cn, temp)

    print("\n--- Reasoning trace ---")
    for step in trace:
        print("•", step)

    print("\n--- Diagnosis ---")
    # If multiple, show all (or pick first)
    for h in hypos:
        print(f"- {h}:")
        print(explain(h), "\n")

if __name__ == "__main__":
    main()
