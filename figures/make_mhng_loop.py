"""第3章の名付けゲームの一巡を描く。

PNG と PDF の両方を出力する。本文からは PNG を参照している。

    python figures/make_mhng_loop.py

内部表現どうしを線で結ばない。境界を越えるのは語の候補 w だけである、
という一点が図の主張なので、$z_A$ と $z_B$ のあいだに矢印を引かないこと。
"""

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch, FancyBboxPatch, Rectangle

plt.rcParams["font.family"] = ["Meiryo", "Yu Gothic", "DejaVu Sans"]
plt.rcParams["axes.unicode_minus"] = False

INK = "#333333"
SUB = "#555555"
FAINT = "#888888"
PANEL = "#777777"

fig, ax = plt.subplots(figsize=(7.6, 4.6))
ax.set_xlim(0, 660)
ax.set_ylim(0, 400)
ax.invert_yaxis()
ax.axis("off")
ax.set_aspect("equal")

# エージェントの枠
for x0, title in [(20, "エージェントA（発話者）"), (370, "エージェントB（聞き手）")]:
    ax.add_patch(
        Rectangle((x0, 62), 270, 246, facecolor="none", edgecolor=PANEL,
                  linewidth=1.3, zorder=1)
    )
    ax.text(x0 + 135, 82, title, ha="center", va="center", fontsize=11.5, color=SUB)

# 内部と外部を隔てる線。越えるのは語だけである
ax.plot([330, 330], [40, 330], linestyle=(0, (4, 4)), linewidth=1.4, color="#999999",
        zorder=1)
ax.text(311, 232, "内部表現はこの線を越えない", ha="center", va="center", fontsize=10,
        color=FAINT, rotation=90)

# 内部表現。どちらも私的である
for x, label in [(120, "z_A"), (580, "z_B")]:
    ax.add_patch(
        Circle((x, 208), 27, facecolor="white", edgecolor=INK, linewidth=1.6, zorder=3)
    )
    ax.text(x, 208, f"${label}$", ha="center", va="center", fontsize=17, zorder=4)
    ax.text(x, 250, "私的な内部表現", ha="center", va="center", fontsize=10, color=SUB)
    ax.text(x, 268, "（自分の観測からつくる）", ha="center", va="center", fontsize=9,
            color=FAINT)

# 提案される語の候補。線の上に置く
ax.add_patch(
    FancyBboxPatch((306, 106), 48, 34, boxstyle="round,pad=2,rounding_size=6",
                   facecolor="white", edgecolor=INK, linewidth=1.6, zorder=5)
)
ax.text(330, 123, "$w$", ha="center", va="center", fontsize=17, zorder=6)

# ① 自分の内部表現から語の候補を出す
ax.add_patch(
    FancyArrowPatch((120, 208), (306, 128), arrowstyle="-|>", mutation_scale=15,
                    linewidth=1.6, color=INK, shrinkA=29, shrinkB=6, zorder=2)
)
ax.text(196, 150, "① 語の候補を提案する", ha="center", va="center", fontsize=10.5,
        color="#444444")

# ② 語だけが相手に届く
ax.add_patch(
    FancyArrowPatch((354, 123), (444, 141), arrowstyle="-|>", mutation_scale=15,
                    linewidth=1.6, color=INK, shrinkA=6, shrinkB=6, zorder=2)
)

# 判断の箱
ax.add_patch(
    FancyBboxPatch((444, 118), 186, 48, boxstyle="round,pad=3,rounding_size=8",
                   facecolor="#f4f4f4", edgecolor=INK, linewidth=1.4, zorder=3)
)
ax.text(537, 133, "② 自分の $z_B$ に照らして", ha="center", va="center", fontsize=9.8,
        color="#333333", zorder=4)
ax.text(537, 152, "③ 受諾するか棄却するか決める", ha="center", va="center", fontsize=9.8,
        color="#333333", zorder=4)

# 判断に使うのは自分の内部表現だけである
ax.add_patch(
    FancyArrowPatch((580, 208), (580, 166), arrowstyle="-|>", mutation_scale=15,
                    linewidth=1.6, color=INK, shrinkA=29, shrinkB=2, zorder=2)
)

# ④ 役割交替
ax.add_patch(
    FancyArrowPatch((520, 334), (140, 334), arrowstyle="-|>", mutation_scale=16,
                    linewidth=1.6, color=SUB, shrinkA=0, shrinkB=0,
                    connectionstyle="arc3,rad=-0.12", zorder=2)
)
ax.text(330, 388, "④ 役割を交替して、対象を変えながら繰り返す", ha="center", va="center",
        fontsize=11, color=SUB)

fig.tight_layout(pad=0.2)
for path, kw in [("figures/mhng-loop.png", {"dpi": 220}), ("figures/mhng-loop.pdf", {})]:
    fig.savefig(path, bbox_inches="tight", facecolor="white", **kw)
    print("wrote", path)
