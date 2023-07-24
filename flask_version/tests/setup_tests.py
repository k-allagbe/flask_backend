from pathlib import Path

from dotenv import load_dotenv

dotenv_path = Path(__file__).parent.parent / ".env.testing"
load_dotenv(dotenv_path.resolve())
