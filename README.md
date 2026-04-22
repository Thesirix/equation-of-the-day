# Equation of the Day

> Showcase a beautiful math equation every day directly on your GitHub profile README — with its name, creator, and purpose. Perfect for students, scientists, and math enthusiasts.

---

## Equation of the Day

$$
\large \frac{dP}{dT} = \frac{L}{T \Delta V}
$$

Rudolf Clausius & Émile Clapeyron - **Clausius-Clapeyron Equation** (1834)

> [!NOTE]
> Characterizes a discontinuous phase transition between two phases of matter of a single constituent. [Read more](https://en.wikipedia.org/wiki/Clausius%E2%80%93Clapeyron_relation)

---

## How it works

This project automatically updates your GitHub README with a new mathematical equation every day. Here is the full pipeline:

### 1. `equations.json` — The equation database

All equations are stored in a single JSON file. Each entry follows this structure:

```json
{
  "name": "Equation Name",
  "author": "Mathematician Name",
  "year": 1900,
  "description": "What the equation means and where it is used.",
  "latex": "\\LaTeX source code",
  "url": "https://link-to-wikipedia-or-source"
}
```

### 2. `main.py` — The generation script

The script does four things:

1. Loads `equations.json`
2. Picks a **random equation** from the list
3. Renders it as a Markdown block with the LaTeX formula, author, name, year, description, and a link
4. Injects the result into `README.template.md` by replacing the `{{DAILY_EQUATION}}` placeholder, and writes the output to `README.md`

The rendered block looks like this:

```
$$
\large <latex>
$$

<Author> - **<Name>** (<Year>)

> [!NOTE]
> <Description> [Read more](<URL>)
```

### 3. `README.template.md` — The template

This file is the skeleton of the README. It contains static content (like this description) and the `{{DAILY_EQUATION}}` placeholder where the daily equation is injected. **Never edit `README.md` directly** — it is overwritten every day. Edit `README.template.md` instead.

### 4. `.github/workflows/update-equation.yml` — The automation

A GitHub Actions workflow runs the pipeline automatically:

| Trigger | When |
|---|---|
| Scheduled (`cron`) | Every day at **00:00 UTC** |
| `workflow_dispatch` | Manually, from the GitHub Actions tab |

The workflow:
1. Checks out the repository
2. Sets up Python 3
3. Runs `main.py`
4. Commits and pushes the updated `README.md` with the message `"Mise à jour de l'équation du jour"`

The workflow uses `permissions: contents: write` to allow the bot to push directly to the repository.

---

## Project structure

```
equation-of-the-day/
├── .github/
│   └── workflows/
│       └── update-equation.yml   # GitHub Actions automation
├── equations.json                # Database of all equations
├── main.py                       # Generation script
├── README.template.md            # Source template (edit this)
└── README.md                     # Auto-generated output (do not edit)
```

---

## Setup — use this on your own profile

1. **Fork** this repository
2. In your GitHub profile repository (`<username>/<username>`), add a daily trigger that calls this workflow — or copy the files directly into your profile repo
3. Make sure the workflow has **write permissions** (`Settings > Actions > General > Workflow permissions > Read and write`)
4. Trigger the workflow manually once (`Actions > Daily Equation Update > Run workflow`) to generate the first README
5. From then on, a new equation appears every day at midnight UTC

---

## Add your own equations

Open `equations.json` and add a new object to the array:

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

Use [LaTeX math syntax](https://en.wikibooks.org/wiki/LaTeX/Mathematics). The formula is rendered with `\large` sizing inside a `$$` display block.

---

## Tech stack

- **Python 3** — script logic
- **GitHub Actions** — scheduling and automation
- **LaTeX / MathJax** — equation rendering in Markdown
- **GitHub Markdown** — `> [!NOTE]` callout blocks

---

*Generated automatically — do not edit `README.md` directly.*
