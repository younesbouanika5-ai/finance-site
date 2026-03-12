import os
import re

# titres déjà utilisés
existing_titles = [
"Comment gagner de l'argent sur internet",
"Comment investir en bourse",
"Comment gérer son budget",
"Applications pour gagner de l'argent",
"10 idées de revenus passifs"
]

# nouveaux titres SEO
titles = [
"Comment investir en ETF pour débutant",
"Comment économiser 1000 euros par an",
"Les meilleures applications pour gérer son argent",
"Comment créer plusieurs sources de revenus",
"Les bases de l'éducation financière",
"Comment éviter les arnaques financières",
"Les meilleures stratégies pour épargner",
"Comment atteindre l'indépendance financière",
"Comment investir avec un petit budget",
"Les erreurs financières les plus courantes",
"Comment investir sur le long terme",
"Les habitudes des personnes riches",
"Comment construire un patrimoine",
"Comment préparer sa retraite",
"Comment investir en actions",
"Les meilleurs livres de finance personnelle",
"Comment réduire ses dépenses",
"Comment gagner de l'argent en freelance",
"Les meilleurs sites pour gagner de l'argent",
"Comment développer ses revenus passifs"
]

content = """
<p>Comprendre la finance personnelle permet d'améliorer sa situation financière et de mieux préparer son avenir.</p>

<h2>Pourquoi apprendre la finance</h2>
<p>La finance personnelle permet de mieux gérer son budget, d'épargner et d'investir intelligemment.</p>

<h2>Investir sur le long terme</h2>
<p>Investir régulièrement sur plusieurs années peut permettre de faire croître son capital.</p>

<h2>Créer des revenus passifs</h2>
<p>Les revenus passifs permettent de gagner de l'argent sans travailler activement chaque jour.</p>

<p>Source : https://www.service-public.fr</p>
"""

template = """
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>{title}</title>
</head>

<body>

<h1>{title}</h1>

{content}

</body>
</html>
"""

os.makedirs("articles", exist_ok=True)

for title in titles:

    if title in existing_titles:
        continue

    filename = re.sub(r"[^a-z0-9]+", "-", title.lower()) + ".html"
    filepath = os.path.join("articles", filename)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(template.format(title=title, content=content))

print("Articles SEO générés sans doublons.")
