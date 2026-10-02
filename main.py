"""Графики функций и диаграммы (matplotlib).

Запуск:  python main.py
Картинки сохраняются в папку output/ и показываются на экране.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.gridspec import GridSpec

OUT = Path(__file__).parent / "output"
OUT.mkdir(exist_ok=True)

plt.rcParams["figure.figsize"] = (7, 5)
plt.rcParams["axes.grid"] = True


def finish(ax, title, xlabel="x", ylabel="y"):
    """Подписывает график и оси."""
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.axhline(0, color="black", linewidth=0.8)
    ax.axvline(0, color="black", linewidth=0.8)


# ---------- функции: каждая рисует на переданной оси ax ----------

def linear(ax, k=2):
    x = np.linspace(-10, 10, 400)
    ax.plot(x, k * x, color="tab:blue", label=f"y = {k}x")
    finish(ax, "Линейная функция y = kx (k = 2)")
    ax.legend()


def square(ax):
    x = np.linspace(-10, 10, 400)
    ax.plot(x, x**2, color="tab:orange", label="y = x²")
    finish(ax, "Парабола y = x²")
    ax.legend()


def cube(ax):
    x = np.linspace(-5, 5, 400)
    ax.plot(x, x**3, color="tab:green", label="y = x³")
    finish(ax, "Кубическая парабола y = x³")
    ax.legend()


def hyperbola(ax, k=4):
    x1 = np.linspace(-10, -0.1, 400)
    x2 = np.linspace(0.1, 10, 400)
    ax.plot(x1, k / x1, color="tab:red", label=f"y = {k}/x")
    ax.plot(x2, k / x2, color="tab:red")  # две ветви, без соединяющей линии
    ax.set_ylim(-20, 20)
    finish(ax, "Гипербола y = k/x (k = 4)")
    ax.legend()


def exponent(ax):
    x = np.linspace(-3, 3, 400)
    ax.plot(x, np.exp(x), color="tab:purple", label="y = eˣ")
    finish(ax, "Экспонента y = eˣ")
    ax.legend()


def sine(ax):
    x = np.linspace(-2 * np.pi, 2 * np.pi, 800)
    ax.plot(x, np.sin(x), color="tab:blue", label="y = sin x")
    finish(ax, "Синусоида y = sin x")
    ax.legend()


def tangent(ax):
    x = np.linspace(-2 * np.pi, 2 * np.pi, 2000)
    y = np.tan(x)
    y[np.abs(y) > 10] = np.nan  # разрывы в асимптотах
    ax.plot(x, y, color="tab:orange", label="y = tg x")
    ax.set_ylim(-10, 10)
    finish(ax, "Тангенс y = tg x")
    ax.legend()


def cotangent(ax):
    x = np.linspace(-2 * np.pi, 2 * np.pi, 2000)
    with np.errstate(divide="ignore"):
        y = 1 / np.tan(x)
    y[np.abs(y) > 10] = np.nan
    ax.plot(x, y, color="tab:green", label="y = ctg x")
    ax.set_ylim(-10, 10)
    finish(ax, "Котангенс y = ctg x")
    ax.legend()


def tanh(ax):
    x = np.linspace(-5, 5, 400)
    ax.plot(x, np.tanh(x), color="tab:red", label="y = th x")
    finish(ax, "Гиперболический тангенс y = th x")
    ax.legend()


def ln(ax):
    x = np.linspace(0.01, 10, 400)
    ax.plot(x, np.log(x), color="tab:brown", label="y = ln x")
    finish(ax, "Натуральный логарифм y = ln x")
    ax.legend()


def normal(ax, mu=0, sigma=1):
    x = np.linspace(-5, 5, 400)
    y = np.exp(-((x - mu) ** 2) / (2 * sigma**2)) / (sigma * np.sqrt(2 * np.pi))
    ax.plot(x, y, color="tab:blue", label=f"μ = {mu}, σ = {sigma}")
    ax.fill_between(x, y, alpha=0.2)
    finish(ax, "Нормальное распределение", "x", "плотность вероятности f(x)")
    ax.legend()


def barh(ax):
    langs = ["Python", "JavaScript", "Java", "C++", "Go"]
    values = [32, 27, 18, 14, 9]
    ax.barh(langs, values, color="tab:cyan")
    for i, v in enumerate(values):
        ax.text(v + 0.3, i, str(v), va="center")
    ax.set_title("Горизонтальная гистограмма")
    ax.set_xlabel("Популярность языков, %")
    ax.set_ylabel("Язык программирования")


def pie(ax):
    labels = ["Python", "JavaScript", "Java", "C++", "Go"]
    values = [32, 27, 18, 14, 9]
    ax.pie(values, labels=labels, autopct="%1.1f%%", startangle=90)
    ax.set_title("Круговая диаграмма")
    ax.grid(False)


# (имя файла, функция)
SINGLE = [
    ("01_linear", linear),
    ("02_square", square),
    ("03_cube", cube),
    ("04_hyperbola", hyperbola),
    ("05_exp", exponent),
    ("06_sin", sine),
    ("07_tg", tangent),
    ("08_ctg", cotangent),
    ("09_th", tanh),
    ("10_ln", ln),
    ("11_normal", normal),
    ("12_barh", barh),
    ("13_pie", pie),
]


def save_single():
    for name, func in SINGLE:
        fig, ax = plt.subplots()
        func(ax)
        fig.tight_layout()
        fig.savefig(OUT / f"{name}.png", dpi=120)


def canvas_6():
    """Полотно 2x3 = 6 графиков (№1-6, plt.subplots)."""
    fig, axes = plt.subplots(2, 3, figsize=(16, 9))
    for ax, func in zip(axes.flat, [linear, square, cube, hyperbola, exponent, sine]):
        func(ax)
    fig.suptitle("Полотно из 6 графиков (№1-6)", fontsize=16)
    fig.tight_layout()
    fig.savefig(OUT / "14_canvas_6.png", dpi=120)


def canvas_7():
    """Полотно из 7 графиков (№7-13): первый занимает 2 секции (GridSpec 2x4)."""
    fig = plt.figure(figsize=(18, 9))
    gs = GridSpec(2, 4, figure=fig)
    # tg x растянут на 2 ячейки по горизонтали
    tangent(fig.add_subplot(gs[0, 0:2]))
    others = [
        (gs[0, 2], cotangent),
        (gs[0, 3], tanh),
        (gs[1, 0], ln),
        (gs[1, 1], normal),
        (gs[1, 2], barh),
        (gs[1, 3], pie),
    ]
    for pos, func in others:
        func(fig.add_subplot(pos))
    fig.suptitle("Полотно из 7 графиков (№7-13, первый занимает 2 секции)", fontsize=16)
    fig.tight_layout()
    fig.savefig(OUT / "15_canvas_7.png", dpi=120)


if __name__ == "__main__":
    save_single()
    canvas_6()
    canvas_7()
    print(f"Готово, графики в папке: {OUT}")
    plt.show()
