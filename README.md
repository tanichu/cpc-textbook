# Collective Predictive Coding

**An Introduction to the Mathematical Theory of Symbol Emergence Systems**

Tadahiro Taniguchi (Kyoto University)

---

> ⚠️ **This book is being written. It is not a draft yet — not even a beta.**
> No chapter has been written. This repository currently holds only the plan:
> the aim of the book, its structure, and the core formulation.
> **Please do not cite, quote, or redistribute.**
>
> 現在執筆中です。ベータ版ですらありません。**引用・転載はお控えください。**

A book giving a systematic mathematical formulation of Collective Predictive Coding (CPC)
as a theory of **symbol emergence systems**. It is planned for eventual publication by
Springer; until then, public drafts are released here.

Companion volume: the Springer book *Symbol Emergence Systems*, which discusses what such
systems are; this book supplies their mathematics.

## Status

Two independent axes are tracked, so that drafting volume is never mistaken for correctness.

- **Writing volume** — ⬜ not started / ◽ outline only / ◨ partially written / ⬛ full draft
- **Verification** — 🤖 raw AI output (correctness not guaranteed) / 👀 visually checked / ✅ author-verified

**All chapters: ⬜–◽ and 🤖.**

## Comments

Corrections and suggestions are welcome, in English or Japanese.
See [CONTRIBUTING.md](CONTRIBUTING.md), or open an
[issue](https://github.com/tanichu/cpc-textbook/issues).

## License

Not yet decided. Until a license is announced, all rights are reserved.

## Building

The site is built with [Quarto](https://quarto.org/).

```bash
quarto render        # HTML + PDF into docs/
quarto preview       # live preview
```

`.github/workflows/build.yml` renders on every push, publishes the HTML to GitHub Pages
(once the repository is public and Pages is enabled), and attaches the PDF to the `latest`
release.
