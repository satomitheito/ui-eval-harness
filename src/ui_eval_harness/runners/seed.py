# Seed example tasks/goldens (stub)
from pathlib import Path

def main():
    tasks = Path("prompts/tasks")
    tasks.mkdir(parents=True, exist_ok=True)
    sample = tasks / "t_001.yaml"
    sample.write_text("""id: t_001
category: forms
brief: Two-column signup with email, password, OAuth buttons; responsive down to 360px.
acceptance:
  - Exactly one email and one password input
  - OAuth buttons for Google and GitHub
  - Two columns at >=1024px; single column <640px
complexity: 2
""", encoding="utf-8")
    print(f"Seeded {sample}")

if __name__ == "__main__":
    main()
