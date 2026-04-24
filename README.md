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
\large \begin{pmatrix} \nu_e \\ \nu_\mu \\ \nu_\tau \end{pmatrix} = U_{\text{PMNS}} \begin{pmatrix} \nu_1 \\ \nu_2 \\ \nu_3 \end{pmatrix}
$$

Bruno Pontecorvo, Maki, Nakagawa, & Sakata - **PMNS Matrix (Neutrino Mixing)** (1962)

> [!NOTE]
> A unitary mixing matrix which contains information on the mismatch between quantum states of neutrinos when they are created and when they interact. [Read more](https://en.wikipedia.org/wiki/Pontecorvo%E2%80%93Maki%E2%80%93Nakagawa%E2%80%93Sakata_matrix)



## How it works

The project has three layers:

```
equations.json        database of all equations
main.py               picks one at random, renders it, writes README.md
README.template.md    static skeleton with a DAILY_EQUATION placeholder
```

Every day at midnight UTC, GitHub Actions runs `main.py`. The script loads `equations.json`, picks a random entry, formats it as a Markdown block, injects it into the template placeholder, and commits the result to `README.md`.

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

| Trigger             | When                          |
| ------------------- | ----------------------------- |
| Scheduled           | Every day at 00:00 UTC        |
| `workflow_dispatch` | Manually from the Actions tab |

It checks out the repo, runs `main.py`, then commits and pushes `README.md`. The workflow requires `permissions: contents: write` to push without a personal token.

## Use it on your profile

There are two ways depending on what you want.

### Option A - Fork this repo

If you want the full project (equation database, `main.py`, template):

1. Fork this repository
2. Go to `Settings > Actions > General > Workflow permissions` and enable **Read and write**
3. Trigger the workflow once manually from the **Actions** tab
4. A new equation appears every day automatically

### Option B - Embed it in an existing repo

If you already have a profile README (or any other repo) and just want to inject a daily equation into it, without forking anything:

**Step 1** - Add the following markers in your `README.md` where you want the equation to appear:

```md
<!-- EQUATION_START -->
<!-- EQUATION_END -->
```

The workflow injects the equation between these markers every day. The markers stay permanently so the equation updates without any rebuild.

**Step 2** - Create `.github/workflows/equation.yml` in your repo with the following workflow:

```yaml
name: "🧮 Equation of the Day"

on:
  schedule:
    - cron: "0 0 * * *"
  workflow_dispatch:

jobs:
  equation:
    name: "🧮 Equation of the Day"
    permissions: write-all
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          ref: main

      - uses: actions/checkout@v4
        with:
          repository: Thesirix/equation-of-the-day
          path: _equation_src

      - name: Inject daily equation
        run: |
          python3 << 'EOF'
          import json, random, re

          with open('_equation_src/equations.json', 'r', encoding='utf-8') as f:
              equations = json.load(f)

          eq = random.choice(equations)
          d = '$'

          block = (
              d*2 + "\n"
              + "\\large " + eq['latex'] + "\n"
              + d*2 + "\n\n"
              + eq['author'] + " - **" + eq['name'] + "** (" + str(eq['year']) + ")\n"
              + "> [!NOTE]\n"
              + "> " + eq['description'] + " [Read more](" + eq['url'] + ")\n"
          )

          START = '<!-- EQUATION_START -->'
          END   = '<!-- EQUATION_END -->'

          with open('README.md', 'r', encoding='utf-8') as f:
              readme = f.read()

          replacement = START + '\n' + block + END
          updated = re.sub(
              re.escape(START) + r'.*?' + re.escape(END),
              lambda m: replacement,
              readme,
              flags=re.DOTALL,
          )

          with open('README.md', 'w', encoding='utf-8') as f:
              f.write(updated)
          EOF

      - name: Commit & push
        run: |
          git config user.name "github-actions"
          git config user.email "github-actions@github.com"
          git add README.md
          if git diff --cached --exit-code; then
            echo "No changes."
          else
            git commit -m "🧮 Update equation of the day"
            git pull --rebase origin main
            git push origin main
          fi
```

**Step 3** - Go to `Settings > Actions > General > Workflow permissions` in your repo and enable **Read and write**

**Step 4** - Trigger the workflow once manually from the **Actions** tab

The workflow clones this repo as a data source, picks a random equation, and injects it into your README. No fork needed, no local Python required.

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
