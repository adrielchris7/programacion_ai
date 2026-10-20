"""Export the figures explored in the notebook."""

from pathlib import Path
import json

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parent


def main():
    passengers = pd.read_csv(ROOT.parent / "sesion-02-pandas/outputs/passengers_prepared.csv")
    image_dir = ROOT.parent / "sesion-03-pytorch/outputs"
    images = np.load(image_dir / "images.npy", allow_pickle=False)
    labels = np.load(image_dir / "labels.npy", allow_pickle=False)
    report = json.loads((image_dir / "report.json").read_text())
    output_dir = ROOT / "outputs"
    output_dir.mkdir(exist_ok=True)

    # ---------------------------------------------------------
    # Ejercicio 1: Histograma con bins=20
    # ---------------------------------------------------------
    ages = passengers["Age"].dropna()
    fig, ax = plt.subplots(figsize=(7, 4), layout="constrained")
    ax.hist(ages, bins=20, color="#245E87", edgecolor="white")
    ax.set(title=f"Recorded ages (n={len(ages)})", xlabel="Age (years)", ylabel="Passengers")
    fig.savefig(output_dir / "ages.png", dpi=150)
    plt.close(fig)

    # ---------------------------------------------------------
    # Ejercicio 2: Edades ausentes por clase
    # ---------------------------------------------------------
    summary_missing = passengers.groupby("Pclass")["age_missing"].agg(["mean", "size"])
    fig, ax = plt.subplots(figsize=(7, 4), layout="constrained")
    names = [f"Class {i} (n={n})" for i, n in summary_missing["size"].items()]
    ax.bar(names, summary_missing["mean"] * 100, color="#245E87")
    ax.set(
        title="Missing ages percentage by passenger class",
        ylabel="Missing Ages (%)",
        ylim=(0, 100)
    )
    fig.savefig(output_dir / "missing_ages.png", dpi=150)
    plt.close(fig)

    # ---------------------------------------------------------
    # 3. Imágenes de CIFAR-10
    # ---------------------------------------------------------
    fig, axes = plt.subplots(2, 4, figsize=(8, 4), layout="constrained")
    for index, ax in enumerate(axes.flat):
        ax.axis("off")
        if index < len(images):
            ax.imshow(images[index].transpose(1, 2, 0), interpolation="nearest")
            ax.set_title(report["classes"][int(labels[index])])
    fig.suptitle(f"CIFAR-10: first {min(8, len(images))} exported images")
    fig.savefig(output_dir / "cifar_grid.png", dpi=150)
    plt.close(fig)

    print(f"Figures saved to {output_dir}")


if __name__ == "__main__":
    main()