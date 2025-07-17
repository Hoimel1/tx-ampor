# EPIC 01 – Infra-Foundations (Container-Architektur)

**Status:** ✅ Abgeschlossen (17 Juli 2025)

## Erledigte Teilaufgaben

| CI-Key | Titel | Ergebnis |
|--------|-------|----------|
| INFRA-1 | Docker & NVIDIA Container Toolkit Installation | Docker 24.x + nvidia-container-toolkit 1.17.8 installiert; `nvidia` Runtime als Default konfiguriert. |
| INFRA-2 | Runtime-Config | `/etc/docker/daemon.json` enthält `"default-runtime": "nvidia"`. |
| INFRA-3 | GPU-Hello-World | `docker run --gpus all nvidia/cuda:12.4-base-ubuntu22.04 nvidia-smi` zeigt L4-GPU unter Treiber 550. |
| INFRA-4 | Lokale Registry | Registry-Container (`registry:2`) läuft auf Port 5000 mit `--restart=always`. |
| INFRA-5 | Test-Dockerfile | `docker/Dockerfile.test-gpu` baut ein Image, das `nvidia-smi` als CMD ausführt. |
| INFRA-6 | Registry Round-Trip | Image `localhost:5000/test-gpu:cuda12.4` erfolgreich gebaut, gepusht und gepullt; GPU inside Container sichtbar. |
| INFRA-7 | Hadolint-Config | `.hadolint.yaml` mit Basisregeln erstellt, Hadolint läuft ohne Fehler. |
| INFRA-8 | CI-Workflow | `.github/workflows/ci.yaml` führt Hadolint auf PRs und optionalen GPU-Test auf self-hosted Runnern aus. |

## Quality Gate G1

*Container erkennt GPU + Dockerfiles lint-clean*

```
$ docker run --rm --gpus all localhost:5000/test-gpu:cuda12.4 nvidia-smi | head -n 3
Thu Jul 17 09:56:22 2025       
+-----------------------------------------------------------------------------------------+
| NVIDIA-SMI 550.163.01             Driver Version: 550.163.01     CUDA Version: 12.4     |
```

Hadolint-Output: _keine Errors_, nur ggf. Warnings laut `.hadolint.yaml`-Policy.

---

Damit ist die Container-Basis stabil; Workflow-Schritte können sich ab jetzt auf reproduzierbare GPU-fähige Images und eine funktionierende Registry stützen. 