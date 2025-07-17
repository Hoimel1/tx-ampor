FROM nvidia/cuda:11.8.0-cudnn8-devel-ubuntu22.04

# Environment variables
ENV DEBIAN_FRONTEND=noninteractive \
    ALPHAFOLD_VERSION=2.3.2 \
    PATH=/opt/conda/bin:$PATH

# -----------------------------------------------------------------------------
# 1. System-Abhängigkeiten installieren
# -----------------------------------------------------------------------------
RUN apt-get update && apt-get install -y --no-install-recommends \
        git wget curl ca-certificates build-essential \
        python3.10 python3-pip python3.10-dev \
        openmm=8.0.0+dfsg-2 \
        && rm -rf /var/lib/apt/lists/*

# -----------------------------------------------------------------------------
# 2. Virtuelle Umgebung via Miniconda einrichten (empfohlen für AF)
# -----------------------------------------------------------------------------
RUN wget -qO ~/miniconda.sh "https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh" \
    && bash ~/miniconda.sh -b -p /opt/conda \
    && rm ~/miniconda.sh

# -----------------------------------------------------------------------------
# 3. Python-Abhängigkeiten installieren – schlankes Set für PoC
# -----------------------------------------------------------------------------
RUN conda install -y -c conda-forge \
        python=3.10 \
        numpy scipy pandas biopython \
        && conda clean -a -y

# -----------------------------------------------------------------------------
# 4. Alphafold-Source holen (ohne großen Datendownload)
# -----------------------------------------------------------------------------
RUN git clone --depth 1 --branch v${ALPHAFOLD_VERSION} https://github.com/deepmind/alphafold.git /app/alphafold

WORKDIR /app/alphafold

# Install python packages required by Alphafold (gekürzt für Demo)
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir \
        dm-tree==0.1.7 \
        absl-py==1.4.0 \
        chex==0.1.7 \
        flax==0.6.11 \
        jax==0.4.28 jaxlib==0.4.28+cuda11.cudnn82 -f https://storage.googleapis.com/jax-releases/jax_cuda_releases.html \
        ml-collections==0.1.1 \
        optax==0.1.8 \
        && pip cache purge

# -----------------------------------------------------------------------------
# 5. Entrypoint – Testbefehl zum GPU-Check
# -----------------------------------------------------------------------------
CMD ["bash", "-c", "nvidia-smi && echo 'Alphafold-Container bereit.'"] 