import tiktoken
from pathlib import Path

ENCODINGS = tiktoken.list_encoding_names()
OUTPUT_DIR = Path(__file__).parent / "tokens"
OUTPUT_DIR.mkdir(exist_ok=True)

for name in ENCODINGS:
    print(f"Processing {name}...")
    enc = tiktoken.get_encoding(name)
    out_path = OUTPUT_DIR / f"{name}.txt"

    id_to_special = {v: k for k, v in enc._special_tokens.items()}

    with open(out_path, "w", encoding="utf-8") as f:
        for tid in range(enc.max_token_value + 1):
            if tid in id_to_special:
                display = f"<{id_to_special[tid]}>"
            else:
                try:
                    raw = enc.decode_single_token_bytes(tid)
                    try:
                        display = repr(raw.decode("utf-8"))
                    except UnicodeDecodeError:
                        display = repr(raw)
                except KeyError:
                    display = "<gap>"
            f.write(f"{tid:>6}  {display}\n")

    print(f"  {enc.max_token_value + 1} entries ({enc.n_vocab} tokens) -> {out_path.name}")

print("\nDone.")
