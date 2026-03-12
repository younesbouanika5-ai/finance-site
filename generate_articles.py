import os
import re

articles = [
    {
        "title": "Comment atteindre l'indépendance financière",
        "image": "https://images.unsplash.com/photo-1554224155-6726b3ff858f?auto=format&fit=crop&w=1200&q=80",
        "intro": "L'indépendance financière consiste à construire une situation où vos revenus, votre épargne et vos investissements vous donnent plus de liberté.",
        "sections": [
            ("Comprendre l'indépendance financière", "L'objectif n'est pas forcément de devenir riche rapidement, mais plutôt de mieux contrôler son argent, ses dépenses et ses choix de vie."),
            ("Épargner régulièrement", "Mettre de côté une somme chaque mois est une base essentielle pour se créer une sécurité financière sur le long terme."),
            ("Investir avec patience", "L'investissement progressif sur plusieurs années peut aider à développer son patrimoine et à rapprocher de ses objectifs.")
        ]
    },
    {
        "title": "Comment économiser 1000 euros par an",
        "image": "https://images.unsplash.com/photo-1579621970795-87facc2f976d?auto=format&fit=crop&w=1200&q=80",
        "intro": "Économiser 1000 euros par an est un objectif réaliste si l'on agit sur plusieurs petites dépenses du quotidien.",
        "sections": [
            ("Analyser ses dépenses", "Commencez par identifier les abonnements inutiles, les achats impulsifs et les frais répétitifs qui pèsent sur votre budget."),
            ("Mettre en place un budget simple", "Prévoir une enveloppe pour chaque catégorie de dépense permet souvent de mieux contrôler son argent."),
            ("Automatiser son épargne", "Programmer un virement mensuel vers un compte épargne aide à économiser sans avoir à y penser.")
        ]
    },
    {
        "title": "Comment construire un patrimoine",
        "image": "https://images.unsplash.com/photo-1556740749-887f6717d7e4?auto=format&fit=crop&w=1200&q=80",
        "intro": "Construire un patrimoine demande du temps, de la régularité et des décisions cohérentes sur plusieurs années.",
        "sections": [
            ("Poser des bases solides", "Avant d'investir, il est utile d'avoir un budget clair, une épargne de sécurité et une vision de ses objectifs."),
            ("Diversifier progressivement", "Un patrimoine peut être composé d'épargne, d'investissements financiers, voire d'immobilier selon votre profil."),
            ("Penser long terme", "Les meilleurs résultats viennent souvent d'une stratégie stable et patiente plutôt que de décisions prises dans l'urgence.")
        ]
    },
    {
        "title": "Comment créer plusieurs sources de revenus",
        "image": "https://images.unsplash.com/photo-1526304640581-d334cdbbf45e?auto=format&fit=crop&w=1200&q=80",
        "intro": "Multiplier ses sources de revenus permet de réduire sa dépendance à un seul salaire et d'améliorer sa sécurité financière.",
        "sections": [
            ("Commencer par une compétence simple", "Freelance, revente de services, création de contenu ou missions ponctuelles peuvent constituer une première source complémentaire."),
            ("Créer une source évolutive", "Certaines activités comme un site web, un produit numérique ou l'affiliation peuvent évoluer avec le temps."),
            ("Rester organisé", "Il vaut mieux développer une source de revenu à la fois plutôt que d'essayer trop de projets en même temps.")
        ]
    },
    {
        "title": "Comment développer ses revenus passifs",
        "image": "https://images.unsplash.com/photo-1518186233392-c232efbf2373?auto=format&fit=crop&w=1200&q=80",
        "intro": "Les revenus passifs ne sont pas magiques : ils demandent souvent du travail au départ, puis deviennent plus automatiques avec le temps.",
        "sections": [
            ("Comprendre le principe", "Un revenu passif est un revenu qui continue à exister même lorsque vous n'êtes pas constamment en train de travailler dessus."),
            ("Choisir un modèle réaliste", "Un site de contenu, un investissement régulier ou un produit numérique peuvent être des pistes intéressantes."),
            ("Construire dans la durée", "Les revenus passifs deviennent souvent intéressants après plusieurs mois de régularité.")
        ]
    },
    {
        "title": "Comment gagner de l'argent en freelance",
        "image": "https://images.unsplash.com/photo-1520607162513-77705c0f0d4a?auto=format&fit=crop&w=1200&q=80",
        "intro": "Le freelance consiste à vendre une compétence précise à des clients sur internet ou en direct.",
        "sections": [
            ("Choisir une compétence vendable", "Rédaction, montage vidéo, design, traduction ou assistance virtuelle sont des services souvent demandés."),
            ("Créer une offre claire", "Une offre simple, avec un prix de départ et un résultat précis, rassure les premiers clients."),
            ("Améliorer sa réputation", "Les avis, la qualité du travail et la régularité permettent de progresser plus vite.")
        ]
    },
    {
        "title": "Comment investir avec un petit budget",
        "image": "https://images.unsplash.com/photo-1565514020179-026b92b84bb6?auto=format&fit=crop&w=1200&q=80",
        "intro": "Il est possible de commencer à investir avec de petites sommes, à condition de rester prudent et cohérent.",
        "sections": [
            ("Commencer progressivement", "Investir une petite somme chaque mois peut être plus simple et plus réaliste que vouloir investir un gros montant d'un coup."),
            ("Limiter les risques inutiles", "Quand on débute, il vaut mieux comprendre les produits avant de chercher des gains rapides."),
            ("Penser long terme", "Même un petit budget peut produire des résultats intéressants sur plusieurs années.")
        ]
    },
    {
        "title": "Comment investir en actions",
        "image": "https://images.unsplash.com/photo-1642790106117-e829e14a795f?auto=format&fit=crop&w=1200&q=80",
        "intro": "Investir en actions consiste à acheter une part d'entreprise dans l'objectif de faire croître son capital à long terme.",
        "sections": [
            ("Comprendre ce qu'est une action", "Une action représente une petite partie d'une entreprise cotée en bourse."),
            ("Analyser avant d'acheter", "Il faut s'intéresser au secteur, aux risques et à l'horizon de placement avant toute décision."),
            ("Rester discipliné", "La patience et la diversification sont souvent plus importantes que la recherche du coup parfait.")
        ]
    },
    {
        "title": "Comment investir en ETF pour débutant",
        "image": "https://images.unsplash.com/photo-1642543492481-44e81e3914a7?auto=format&fit=crop&w=1200&q=80",
        "intro": "Les ETF sont souvent utilisés par les débutants car ils permettent d'investir sur plusieurs entreprises avec un seul produit.",
        "sections": [
            ("Pourquoi les ETF sont populaires", "Ils permettent de diversifier plus facilement qu'en choisissant une seule action."),
            ("Comprendre les frais", "Même des frais faibles peuvent avoir un impact à long terme, il faut donc les comparer."),
            ("Investir avec méthode", "Une stratégie régulière et simple est souvent suffisante pour débuter correctement.")
        ]
    },
    {
        "title": "Comment investir sur le long terme",
        "image": "https://images.unsplash.com/photo-1460925895917-afdab827c52f?auto=format&fit=crop&w=1200&q=80",
        "intro": "Investir sur le long terme repose surtout sur la patience, la régularité et une bonne compréhension de ses objectifs.",
        "sections": [
            ("Définir un horizon", "Plus votre horizon est long, plus vous pouvez lisser certaines fluctuations du marché."),
            ("Éviter les réactions émotionnelles", "Changer de stratégie à chaque baisse ou chaque hausse peut nuire aux résultats."),
            ("Rester cohérent", "Une méthode simple, répétée pendant plusieurs années, peut être très efficace.")
        ]
    },
    {
        "title": "Comment préparer sa retraite",
        "image": "https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?auto=format&fit=crop&w=1200&q=80",
        "intro": "Préparer sa retraite revient à anticiper ses besoins futurs et à construire une base financière progressive.",
        "sections": [
            ("Commencer tôt", "Même de petites sommes investies tôt peuvent avoir un effet significatif avec le temps."),
            ("Diversifier ses solutions", "Épargne, investissements et bonnes habitudes budgétaires peuvent se compléter."),
            ("Réévaluer régulièrement", "Vos besoins évoluent, votre stratégie de préparation aussi.")
        ]
    },
    {
        "title": "Comment réduire ses dépenses",
        "image": "https://images.unsplash.com/photo-1554224154-26032ffc0d07?auto=format&fit=crop&w=1200&q=80",
        "intro": "Réduire ses dépenses n'implique pas forcément de se priver, mais plutôt d'optimiser ce qui peut l'être.",
        "sections": [
            ("Identifier les fuites
