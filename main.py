import json
import random

# 1. Load equations
with open('equations.json', 'r', encoding='utf-8') as f:
    equations = json.load(f)

# Pick a random equation for the day
daily_equation = random.choice(equations)

# Prepare the Markdown/LaTeX block to inject
latex_block = f"""
### {daily_equation['name']} ({daily_equation['year']})
*{daily_equation['author']}* - [Read more]({daily_equation['url']})

> {daily_equation['description']}

$$
{daily_equation['latex']}
$$
"""

# 2. Read the template
with open('README.template.md', 'r', encoding='utf-8') as f:
    template = f.read()

# 3. Replace the placeholder with the generated block
final_readme = template.replace('{{DAILY_EQUATION}}', latex_block)

# 4. Save the final README.md
with open('README.md', 'w', encoding='utf-8') as f:
    f.write(final_readme)