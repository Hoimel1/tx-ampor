# EPIC 02 – Data Integrity & Versioning

**Status:** ✅ Abgeschlossen (17 Juli 2025)

## Erledigte Teilaufgaben

| CI-Key | Titel | Ergebnis |
|--------|-------|----------|
| DATA-1 | Core-Implementation | DVC initialisiert; CSV & FASTA nach `data/raw/` verschoben und mit DVC getrackt. |
| DATA-2 | Upgrades (Trajektorien + Schemas) | Pydantic-Modell `PeptideRecord`, Loader `load_peptides()`; Unit-Tests + Pytest-Job im CI. |
| DATA-3 | Quality Gate G2 | GitHub Action `dvc-status` stellt sicher, dass `dvc status -c` sauber ist. |
| DATA-4 | Dokumentation & Quellen | Dieses Dokument beschreibt Setup & Regeln. |

## Ordnerstruktur
```
├── data
│   └── raw
│       ├── dbaasp-tox.csv        # von DVC verwaltet
│       └── dbaasp-tox.fasta      # von DVC verwaltet
└── src
    └── data_models.py            # PeptideRecord + Loader
```

## Nutzung
```python
from src.data_models import load_peptides
records = load_peptides()  # List[PeptideRecord]
```

## Quality Gate G2
1. `dvc status -c` muss leer sein (CI prüft das).  
2. Alle Schema-Validierungen (Pytest) müssen bestehen.  
3. Datenänderungen erfolgen ausschließlich via `dvc add/move/remove` + Pull-Request.

---
Damit ist die Datenbasis versionssicher, validiert und CI-überwacht – bereit für Downstream-EPICs (Struktur­prognose etc.). 