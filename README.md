<div align="center">

# Equation of the Day

**A new mathematical equation appears on your GitHub profile every single day.**
Name, author, year, and purpose. Automatically. No manual work.

[![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat-square&logo=python)](https://python.org)
[![GitHub Actions](https://img.shields.io/badge/Automation-GitHub_Actions-black?style=flat-square&logo=githubactions)](https://github.com/features/actions)
[![LaTeX](https://img.shields.io/badge/Format-LaTeX-orange?style=flat-square)](https://www.latex-project.org/)
[![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)](LICENSE)

</div>

## Equation of the Day

$$
\large q_e q_m = \frac{n h}{2}
$$

Paul Dirac - **Dirac Quantization Condition** (1931)

> [!NOTE]
> States that the mere existence of a single magnetic monopole anywhere in the universe would imply that all electric charge is quantized. [Read more](https://en.wikipedia.org/wiki/Magnetic_monopole)

## How it works

The project has three layers:

```
equations.json        database of all equations
main.py               picks one at random, renders it, writes README.md
README.template.md    static skeleton with a $$
\large q_e q_m = \frac{n h}{2}
$$

Paul Dirac - **Dirac Quantization Condition** (1931)

> [!NOTE]
> States that the mere existence of a single magnetic monopole anywhere in the universe would imply that all electric charge is quantized. [Read more](https://en.wikipedia.org/wiki/Magnetic_monopole)
 placeholder
```

Every day at midnight UTC, GitHub Actions runs `main.py`. The script loads `equations.json`, picks a random entry, formats it as a Markdown block, replaces `$$
\large q_e q_m = \frac{n h}{2}

$$

Paul Dirac - **Dirac Quantization Condition** (1931)

> [!NOTE]
> States that the mere existence of a single magnetic monopole anywhere in the universe would imply that all electric charge is quantized. [Read more](https://en.wikipedia.org/wiki/Magnetic_monopole)
` in the template, and commits the result to `README.md`.

The rendered block looks like this:

```
$$

\large <latex>

$$

<Author> - **<Name>** (<Year>)

> [!NOTE]
> <Description> [Read more](<URL>)
```

## Equation format

Each entry in `equations.json` follows this structure:

```json
{
  "name": "Equation Name",
  "author": "Mathematician Name",
  "year": 1900,
  "description": "What the equation means and where it is used.",
  "latex": "\\LaTeX source code",
  "url": "https://en.wikipedia.org/wiki/..."
}
```

## Project structure

```
equation-of-the-day/
├── .github/
│   └── workflows/
│       └── update-equation.yml
├── equations.json
├── main.py
├── README.template.md
└── README.md
```

## Workflow

The GitHub Actions workflow triggers in two ways:

| Trigger | When |
|---|---|
| Scheduled | Every day at 00:00 UTC |
| `workflow_dispatch` | Manually from the Actions tab |

It checks out the repo, runs `main.py`, then commits and pushes `README.md`. The workflow requires `permissions: contents: write` to push without a personal token.

## Setup on your own profile

1. Fork this repository
2. Go to `Settings > Actions > General > Workflow permissions` and enable **Read and write**
3. Trigger the workflow once manually from the **Actions** tab to generate the first README
4. From then on, a new equation appears every day automatically

## Add your own equations

Open `equations.json` and append a new object to the array:

```json
{
  "name": "Your Equation Name",
  "author": "Author Full Name",
  "year": 2024,
  "description": "A short explanation of what the equation does.",
  "latex": "E = mc^2",
  "url": "https://en.wikipedia.org/wiki/..."
}
```

Use standard [LaTeX math syntax](https://en.wikibooks.org/wiki/LaTeX/Mathematics). The formula is wrapped in `\large` and rendered inside a `$$` display block, which GitHub renders natively.

## Requirements

- Python 3.x (no third-party packages)
- A GitHub repository with Actions enabled

## License

MIT. Do whatever you want, a star is always appreciated ⭐ and feel free to add new equations!


$$
