# IA et RO — Recherche opérationnelle
*Fiche de révision — Licence Économétrie S5 | 6 PDF du module de recherche opérationnelle*

## Périmètre du support disponible
Les six documents transmis portent sur la **recherche opérationnelle (RO)** : programmation linéaire, résolution graphique, algorithme du simplexe et TD de dualité. **Aucun cours autonome d'intelligence artificielle (IA) n'est présent** parmi ces documents ; cette fiche ne prétend donc pas résumer une partie IA non fournie.

## 1. Pourquoi la programmation linéaire ?
La programmation linéaire (PL) sert à choisir la meilleure affectation de ressources limitées : quantité à produire, plan publicitaire, mélange d'aliments, temps machine ou coût minimum. Le modèle comporte :
- des **variables de décision** x1, x2, ..., qui traduisent les choix ;
- une **fonction objectif** linéaire Z à maximiser (profit, couverture) ou minimiser (coût) ;
- des **contraintes** linéaires (capacités, besoins minimum, budgets, demandes) ;
- des contraintes de **non-négativité** xi ≥ 0 si les quantités ne peuvent être négatives.

**Procédure de modélisation :** (1) identifier les inconnues et leurs unités ; (2) traduire l'objectif ; (3) écrire une inégalité ou égalité par ressource ; (4) ajouter xi ≥ 0 ; (5) vérifier la cohérence des unités.

### Exemple du cours — deux produits
Une entreprise fabrique A et B. Chaque unité A rapporte 50 DH, chaque B 60 DH. Les consommations des trois ressources donnent :
- Max Z = 50x1 + 60x2 ;
- x1 + 2x2 ≤ 8 (machine) ;
- 2x1 + 2x2 ≤ 10 (matière p) ;
- 9x1 + 4x2 ≤ 36 (matière q) ;
- x1, x2 ≥ 0.

Pour un problème à **besoins minimaux**, les signes peuvent être inversés. Exemple de ration alimentaire :
Min Z = 20x1 + 40x2, avec 2x1 + x2 ≥ 16, x1 + x2 ≥ 12, x1 + 3x2 ≥ 18 et xi ≥ 0.

## 2. Forme canonique et forme standard
Le cours distingue la forme **canonique** (contraintes exprimées par inégalités) et la forme **standard** (contraintes exprimées par égalités avec variables non négatives).

Pour une contrainte du type x1 + 2x2 ≤ 8, ajouter une variable d'écart e1 ≥ 0 :
**x1 + 2x2 + e1 = 8.**
Elle mesure la capacité non utilisée.

Pour une contrainte du type 2x1 + x2 ≥ 16, soustraire une variable de surplus e1 ≥ 0 :
**2x1 + x2 - e1 = 16.**

Une contrainte est dite **saturée** à l'optimum si son écart est nul ; si l'écart est non nul, le support parle de contrainte « marginale ». Attention : la transformation en égalité n'autorise pas à oublier la non-négativité.

## 3. Résolution graphique (deux variables)
La méthode graphique convient aux problèmes avec deux variables de décision :
1. Placer x1 sur l'axe horizontal et x2 sur l'axe vertical.
2. Tracer la droite correspondant à chaque contrainte (remplacer ≤ ou ≥ par =).
3. Conserver le demi-plan qui satisfait l'inégalité ; l'intersection de tous les demi-plans forme la **région admissible**.
4. Trouver ses **sommets** par intersections de droites.
5. Calculer Z à chacun de ces sommets et retenir le meilleur point (max ou min).
6. Vérifier les contraintes, l'objectif et les éventuels écarts.

### Exemple corrigé dans le support
Max Z = 300x1 + 200x2, sous contraintes :
x1 + 2x2 ≤ 20 ; 2x1 + x2 ≤ 22 ; x1 + x2 ≤ 12 ; xi ≥ 0.

Sommets étudiés : (0,10) donne Z = 2 000 ; (4,8) donne Z = 2 800 ; (10,2) donne Z = 3 400 ; (11,0) donne Z = 3 300. **Optimum : x1 = 10, x2 = 2, Zmax = 3 400.**

À ce point, la première contrainte conserve 6 unités libres, les deuxième et troisième sont saturées.

Un autre exemple du cours est Max Z = 300x1 + 500x2, avec x1 ≤ 4, 2x2 ≤ 12 et 3x1 + 2x2 ≤ 18. Son optimum est (x1,x2) = (2,6), pour Z = 3 600.

**Cas particuliers figurant dans les diapositives :** ensemble admissible vide (pas de solution), objectif non borné (pas d'optimum fini), ou plusieurs optima sur un segment. La simple forme de la région ne suffit pas : il faut examiner la direction de l'objectif.

## 4. Méthode du simplexe
Le simplexe est un algorithme itératif qui passe d'une solution de base admissible à une solution voisine améliorant l'objectif, jusqu'à atteindre l'optimum. Il permet de traiter davantage de variables que la méthode graphique.

**Étapes pour une maximisation :**
1. Mettre le programme sous forme standard ; ajouter les variables d'écart.
2. Construire la base de départ et le **tableau initial** avec coefficients Ci et CB, seconds membres b et coefficients des contraintes.
3. Calculer **Zj = Σ(CB × aij)** puis **Ci - Zi**.
4. Choisir comme variable **entrante** celle dont Ci - Zi est le plus grand et strictement positif.
5. Choisir la variable **sortante** par le plus petit rapport positif b_i / a_i,colonne-pivot, pour les dénominateurs strictement positifs.
6. Diviser la ligne pivot par l'élément pivot et annuler les autres coefficients de la colonne.
7. Recalculer les coûts réduits et recommencer si nécessaire.
8. **Arrêt (max) :** tous les Ci - Zi sont ≤ 0.

**Minimisation :** d'après la convention du tableau du cours, on choisit le coût réduit Ci - Zi le plus négatif ; l'arrêt intervient lorsque tous les Ci - Zi sont ≥ 0.

### Exemple du simplexe
Pour Max Z = 300x1 + 500x2, sous x1 ≤ 4, 2x2 ≤ 12 et 3x1 + 2x2 ≤ 18, le tableau commence avec les variables d'écart. Après les pivots, le support obtient x1 = 2, x2 = 6 et **Zmax = 3 600**.

## 5. Contraintes ≥, égalités et méthode du Grand M
Lorsque les variables d'écart ne permettent pas de construire une **base réalisable de départ** (contraintes ≥ ou =), le cours introduit des **variables artificielles**, qui doivent sortir de la base avant la solution finale.

- En maximisation, on pénalise ces variables avec un coefficient très négatif **-M**.
- En minimisation, on leur affecte un coût très positif **+M**.
- On construit le tableau avec ces pénalités, puis on pivote pour éliminer les variables artificielles.

L'exemple de minimisation du support est :
Min Z = 24x1 + 20x2, sous x1 + x2 ≥ 30, x1 + 2x2 ≥ 40 et xi ≥ 0. On soustrait des variables de surplus et ajoute les artificielles pour former la base. Le cours indique une solution **x1 = 0, x2 = 30, Zmin = 600**.

## 6. Dualité : ce que couvrent les documents
Le **TD 2 — Simplexe et dualité** demande de former le dual de programmes P1 à P4, puis de résoudre un dual et d'en déduire l'optimum primal. Le plan du cours annonce un chapitre 3 « Dualité », mais **le cours théorique correspondant n'a pas été fourni**. Réviser les exercices et demander le chapitre complet pour les règles formelles détaillées.

## 7. Méthode de travail pour les TD
- **TD de formulation :** transformer les données d'une usine, d'un plan de publicité, d'un assortiment ou d'un mélange en variables, fonction objectif et contraintes. Ne pas commencer par résoudre avant d'avoir écrit le modèle.
- **TD graphique :** tracer proprement chaque droite et calculer ses intersections ; comparer les valeurs de Z aux sommets.
- **TD simplexe :** soigner le signe des coefficients Ci - Zi, le calcul du ratio et la normalisation de la ligne pivot.
- **TD dualité :** identifier précisément la fonction objectif et le sens de chaque contrainte avant d'écrire le dual.

## 8. Questions flash
1. **Qu'est-ce qu'une variable de décision ?** Une inconnue qui représente une quantité ou un choix contrôlé par le décideur.
2. **Pourquoi ajouter une variable d'écart ?** Transformer une contrainte ≤ en égalité et suivre la ressource non utilisée.
3. **Pourquoi tester les sommets ?** Un programme linéaire, lorsqu'il possède un optimum fini sur un polyèdre, possède une solution optimale à au moins un sommet.
4. **Comment choisir la variable sortante ?** Avec le plus petit ratio positif b/a, si a > 0.
5. **Quand s'arrêter en maximisation selon le tableau du cours ?** Quand tous les Ci - Zi ≤ 0.
6. **Pourquoi le Grand M ?** Pour disposer d'une base initiale et forcer le retrait des variables artificielles.

## Supports d'origine étudiés
- « RO — Chapitre 1 — Programmation linéaire » (51 pages).
- « RO — Chapitre 2 — Méthode simplexe — Économétrie S5 2026-2027 » (42 pages).
- « RO — Chapitre 2 — Méthode simplexe — CCAS 2025-2026 » (44 pages), version de comparaison.
- « RO — TD1 — Formulation programmation linéaire » (2 pages).
- « RO — TD1 — Résolution graphique » (2 pages).
- « RO — TD2 — Simplexe et dualité » (2 pages).

*Périmètre limité aux supports réellement déposés : programmation linéaire et RO, sans chapitre théorique IA.*
