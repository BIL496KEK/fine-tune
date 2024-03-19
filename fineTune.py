from pathlib import Path
from openai import OpenAI

client = OpenAI(
    api_key="",
)

client.files.create(
    file=Path("spor_malzemeleri.jsonl"),
    purpose="fine-tune",
)
