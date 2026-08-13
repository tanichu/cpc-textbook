"""第2章の生成モデル図を描く。

PNG と PDF の両方を出力する。HTML でも LaTeX でも同じ図を使えるようにするため、
本文からは PNG を参照している（LaTeX は PNG をそのまま扱える）。

    python figures/make_cpc_pgm.py
"""

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch, Rectangle

plt.rcParams["font.family"] = ["Meiryo", "Yu Gothic", "DejaVu Sans"]
plt.rcParams["axes.unicode_minus"] = False

INK = "#333333"
SUB = "#555555"
FAINT = "#888888"
OBS_FILL = "#dcdcdc"

fig, ax = plt.subplots(figsize=(7.0, 4.6))
ax.set_xlim(0, 560)
ax.set_ylim(0, 360)
ax.invert_yaxis()
ax.axis("off")
ax.set_aspect("equal")


def node(x, y, label, sub=None, observed=False):
    ax.add_patch(
        Circle((x, y), 27, facecolor=OBS_FILL if observed else "white",
               edgecolor=INK, linewidth=1.6, zorder=3)
    )
    txt = f"${label}" + (f"_{{{sub}}}$" if sub else "$")
    ax.text(x, y, txt, ha="center", va="center", fontsize=17, zorder=4)


def arrow(x, y0, y1):
    ax.add_patch(
        FancyArrowPatch((x, y0), (x, y1), arrowstyle="-|>", mutation_scale=16,
                        linewidth=1.6, color=INK, shrinkA=0, shrinkB=0, zorder=2)
    )


# プレート（K 人ぶんの繰り返し）
ax.add_patch(
    Rectangle((120, 106), 360, 200, facecolor="none", edgecolor="#777777",
              linewidth=1.3, zorder=1)
)
ax.text(466, 292, "$K$", ha="right", va="center", fontsize=14, color=SUB)

# ノード
node(300, 48, "w")
node(300, 166, "z", "k")
node(300, 256, "x", "k", observed=True)

# 生成の矢印
arrow(300, 75, 137)
arrow(300, 193, 227)

# 因子の注記
ax.text(264, 26, "$p(w)$", ha="right", va="center", fontsize=13, color=SUB)
ax.text(340, 112, "$p(z_k \\mid w)$", ha="left", va="center", fontsize=13, color="#444444")
ax.text(340, 216, "$p(x_k \\mid z_k)$", ha="left", va="center", fontsize=13, color="#444444")

# 二つの経路
ax.text(268, 128, "トップダウン", ha="right", va="center", fontsize=11, color="#666666")
ax.text(268, 146, "記号が表現を方向づける", ha="right", va="center", fontsize=9.5, color=FAINT)
ax.text(268, 208, "ボトムアップ", ha="right", va="center", fontsize=11, color="#666666")
ax.text(268, 226, "表現が観測を説明する", ha="right", va="center", fontsize=9.5, color=FAINT)

# 凡例
ax.add_patch(Circle((132, 336), 9, facecolor="white", edgecolor=INK, linewidth=1.3))
ax.text(148, 336, "潜在変数（観測できない）", ha="left", va="center", fontsize=10, color="#444444")
ax.add_patch(Circle((330, 336), 9, facecolor=OBS_FILL, edgecolor=INK, linewidth=1.3))
ax.text(346, 336, "観測変数", ha="left", va="center", fontsize=10, color="#444444")

fig.tight_layout(pad=0.2)
for path, kw in [("figures/cpc-pgm.png", {"dpi": 220}), ("figures/cpc-pgm.pdf", {})]:
    fig.savefig(path, bbox_inches="tight", facecolor="white", **kw)
    print("wrote", path)
