import os
import re

articles = [
    {
        "title": "Comment atteindre l'indépendance financière",
        "image": "https://images.unsplash.com/photo-1554224155-6726b3ff858f?auto=format&fit=crop&w=1200&q=80",
        "intro": "L'indépendance financière consiste à construire une situation où vos revenus et vos investissements vous donnent plus de liberté.",
        "sections": [
            ("Comprendre l'indépendance financière","L'objectif n'est pas de devenir riche rapidement mais de mieux contrôler son argent."),
            ("Épargner régulièrement","Mettre de côté chaque mois permet de construire une base financière solide."),
            ("Investir avec patience","Les investissements progressifs permettent souvent de construire un patrimoine sur le long terme.")
        ]
    },
    {
        "title": "Comment économiser 1000 euros par an",
        "image": "https://images.unsplash.com/photo-1579621970795-87facc2f976d?auto=format&fit=crop&w=1200&q=80",
        "intro": "Économiser 1000 euros par an est un objectif réaliste si l'on agit sur plusieurs petites dépenses.",
        "sections": [
            ("Analyser ses dépenses","Identifier les dépenses inutiles permet souvent d'économiser rapidement."),
            ("Créer un budget simple","Un budget mensuel aide à mieux contrôler ses dépenses."),
            ("Automatiser son épargne","Programmer un virement automatique aide à épargner sans y penser.")
        ]
    },
    {
        "title": "Comment investir avec un petit budget",
        "image": "https://images.unsplash.com/photo-1565514020179-026b92b84bb6?auto=format&fit=crop&w=1200&q=80",
        "intro": "Il est possible de commencer à investir même avec un petit budget.",
        "sections": [
            ("Commencer progressivement","Investir chaque mois permet de construire un capital."),
            ("Limiter les risques","Il est important de comprendre les investissements avant d'agir."),
            ("Penser long terme","La patience est souvent la clé des investissements réussis.")
        ]
    }
]

def slugify(text):

    text = text.lower()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"\s+", "-", text)

    return text


os.makedirs("articles", exist_ok=True)

for article in articles:

    slug = slugify(article["title"])

    filename = f"articles/{slug}.html"

    sections_html = ""

    for title, text in article["sections"]:
        sections_html += f"<h2>{title}</h2><p>{text}</p>"

    html = f"""
<!DOCTYPE html>
<html lang="fr">

<head>

<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>{article["title"]} | FinanceSimple</title>

<meta name="description" content="{article["intro"]}">

<style>

body {{
font-family: Arial;
margin:0;
background:#f4f6f9;
}}

header {{
background:#0a2540;
color:white;
padding:40px;
text-align:center;
}}

nav {{
background:#082033;
padding:15px;
text-align:center;
}}

nav a {{
color:white;
margin:15px;
text-decoration:none;
font-weight:bold;
}}

.container {{
max-width:900px;
margin:auto;
background:white;
padding:40px;
}}

.container img {{
width:100%;
border-radius:10px;
margin-bottom:20px;
}}

footer {{
background:#0a2540;
color:white;
text-align:center;
padding:20px;
margin-top:40px;
}}

</style>

</head>

<body>

<header>

<h1>FinanceSimple</h1>
<p>Apprendre à gérer et investir son argent</p>

</header>

<nav>

<a href="../index.html">Accueil</a>
<a href="../gagner-argent-internet.html">Gagner de l'argent</a>
<a href="../investir-bourse.html">Investir</a>
<a href="../budget.html">Budget</a>
<a href="../revenu-passif.html">Revenus passifs</a>
<a href="../contact.html">Contact</a>

</nav>

<div class="container">

<h1>{article["title"]}</h1>

<img src="{article["image"]}">

<p>{article["intro"]}</p>

{sections_html}

<p><strong>Source :</strong> https://www.service-public.fr</p>

</div>

<footer>

© 2026 FinanceSimple

</footer>

</body>
</html>
"""

    with open(filename, "w", encoding="utf-8") as f:
        f.write(html)

print("Articles générés avec succès.")
