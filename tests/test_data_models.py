import pytest  # type: ignore
from pathlib import Path

from src.data_models import PeptideRecord, load_peptides


def test_load_peptides_default():
    records = load_peptides()
    # Stelle sicher, dass mindestens ein Record geladen wird
    assert len(records) > 0

    first = records[0]
    # Basis-Validität
    assert isinstance(first, PeptideRecord)
    assert first.sequence == first.sequence.upper()
    # sequence_length ist positiv
    assert first.sequence_length >= 1


def test_hc50_range_and_numeric(tmp_path: Path):
    # Minimal-Mock-CSV mit Grenzfällen
    csv_content = (
        "id,sequence,sequence_length,is_toxic,type,hc50_um\n"
        "TEST1,AAA,3,True,pep,<1\n"
        "TEST2,BBB,3,False,pep,>2000\n"
        "TEST3,CCC,3,True,pep,42.0\n"
    )
    csv_path = tmp_path / "test.csv"
    csv_path.write_text(csv_content, encoding="utf-8")

    records = load_peptides(csv_path)
    assert [r.hc50_um for r in records] == ["<1", ">2000", 42.0] 