# Tests d’hypothèses
*Fiche de révision — Licence Économétrie S5 | Cours (65 pages, dont 54 planches initialement numérisées) et TD 1 (2 pages)*

## Plan des supports étudiés
Le cours introduit d'abord les bases de statistique descriptive et d'inférence, puis le raisonnement de Neyman–Pearson : hypothèses H₀/H₁, règles de décision, erreurs α et β, puissance. Ses diapositives présentent ensuite le programme des tests d'un échantillon et de deux échantillons. Le TD porte surtout sur les **tests de moyenne**.

**Limite importante :** le chapitre 2 (tests détaillés sur moyenne, proportion et variance) et le chapitre 3 (comparaison entre deux échantillons) sont **annoncés dans le plan**, mais ne figurent pas comme cours théoriques complets dans le PDF reçu. Les formules ci-dessous viennent des planches et TD effectivement présents.

## 1. Rappels statistiques avant le test
Le parcours du cours suit : **Population → Échantillon → Observation → Description → Estimation → Test → Décision**.

- **Population :** ensemble des individus ou unités étudiés (clients, entreprises, produits, ménages).
- **Échantillon :** sous-ensemble de n observations, tiré selon un plan adapté.
- **Paramètre :** grandeur fixe mais généralement inconnue dans la population : moyenne μ, proportion p, variance σ².
- **Statistique / estimateur :** quantité calculée avec l'échantillon : moyenne x̄, fréquence p̂, variance corrigée s².
- **Variables quantitatives :** discrètes ou continues ; **qualitatives :** nominales ou ordinales.

### Statistiques essentielles
- **Moyenne :** x̄ = (Σ xi) / n.
- **Variance corrigée :** s² = Σ(xi - x̄)² / (n - 1).
- **Écart-type :** s = √s².
- **Erreur standard de la moyenne :** σ/√n si σ est connu ; sinon l'estimation utilise s/√n.
- **Coefficient de variation :** CV = s / x̄ (interprétation prudente si x̄ est proche de zéro).

Le cours rappelle le théorème central limite (TCL) : avec des observations indépendantes et des conditions adaptées, la distribution de x̄ peut être approximativement normale quand n est suffisamment grand. La règle n ≥ 30 n'est qu'un repère pédagogique, pas une garantie universelle.

**Échantillonnages abordés :** aléatoire simple, stratifié, en grappes et systématique. Un grand échantillon ne corrige pas, à lui seul, un tirage biaisé.

## 2. Estimer ou tester ?
**Estimation ponctuelle :** calculer une valeur plausible d'un paramètre (x̄ pour μ).  
**Intervalle de confiance :** fournir, par une procédure définie, un intervalle qui couvre le paramètre selon une fréquence nominale sur des échantillons répétés.  
**Test d'hypothèses :** formuler une affirmation sur le paramètre, confronter les données à cette affirmation et décider selon une règle fixée avant de voir les résultats.

Un test ne donne pas une certitude : c'est une décision contrôlant un risque d'erreur.

## 3. Hypothèse nulle H₀ et hypothèse alternative H₁
- **H₀ (hypothèse nulle) :** référence/statut quo que l'on cherche éventuellement à rejeter.
- **H₁ (alternative) :** changement ou effet que l'on veut détecter.
- **Bilatéral :** H₁ : μ ≠ μ₀ (on cherche un changement dans les deux sens).
- **Unilatéral à droite :** H₁ : μ > μ₀ (augmentation).
- **Unilatéral à gauche :** H₁ : μ < μ₀ (diminution).

Exemples repris du cours :
- « Le délai moyen dépasse 48 h » : alternative unilatérale à droite.
- « L'inflation est différente de 2 % » : bilatéral.
- « Le taux de chômage est inférieur à 9 % » : unilatéral à gauche.

**Vocabulaire rigoureux :** dire « on rejette H₀ » ou « on ne rejette pas H₀ », plutôt que « on a prouvé H₀ vraie ».

## 4. Décision, région critique et p-valeur
Un test choisit une **statistique** (par exemple Z), sa distribution sous H₀ et une **région critique** qui entraîne le rejet. Le seuil α est fixé à l'avance (souvent 5 %).

**Test Z bilatéral à α = 5 % :** rejeter H₀ si |Z| > 1,96.  
**Test Z unilatéral à droite à α = 5 % :** rejeter H₀ si Z > 1,645.  
**Test Z unilatéral à gauche à α = 5 % :** rejeter H₀ si Z < -1,645.

La **p-valeur** représente, sous H₀, la probabilité d'obtenir une statistique au moins aussi extrême que celle observée selon le test choisi. Si p-valeur ≤ α, rejeter H₀. Une petite p-valeur n'est **pas** la probabilité que H₀ soit fausse.

## 5. Erreurs et puissance
| Situation | Décision | Type |
|---|---|---|
| H₀ est vraie | On rejette H₀ | **Erreur de 1re espèce**, probabilité α |
| H₀ est fausse | On ne rejette pas H₀ | **Erreur de 2e espèce**, probabilité β |
| H₀ est vraie | On ne rejette pas | Bonne décision, probabilité 1 - α |
| H₀ est fausse | On rejette | Bonne détection, **puissance = 1 - β** |

La **puissance** est la capacité à détecter un effet réel. Selon le cours, elle augmente généralement quand :
- l'**échantillon n** est plus grand ;
- la **variance σ²** est plus faible (mesure plus précise) ;
- l'effet réel est plus grand ;
- on accepte un α plus élevé, **au prix** de davantage de fausses alertes.

Il existe un arbitrage entre α et β ; tous deux ne peuvent pas être rendus arbitrairement petits sans conditions ou augmentation d'information.

## 6. Test Z sur une moyenne (σ connu)
Hypothèse du cours : population normale ou approximation valide pour x̄ ; écart-type **de population σ connu**.

**Statistique :** Z = (x̄ - μ₀) / (σ/√n).

### Exemple 1 — dépenses moyennes (TD de cours)
Une enseigne annonce μ₀ = 200 DH. On suspecte une hausse. Échantillon : n = 25, x̄ = 208 DH, σ = 20 DH.

H₀ : μ ≤ 200 (frontière testée μ = 200) ; H₁ : μ > 200.  
Z = (208 - 200)/(20/√25) = 8/4 = **2,00**.  
À 5 % à droite, la valeur critique est 1,645 : **2,00 > 1,645**, donc rejet de H₀. Les données sont compatibles avec une hausse de la dépense moyenne.

### Exemple 2 — poids d'un produit (diapositive corrigée)
H₀ : μ = 500 g, H₁ : μ ≠ 500 g ; n = 36, x̄ = 495 g, σ = 12 g.  
Z = (495 - 500)/(12/√36) = **-2,5**.  
Au seuil bilatéral de 5 %, |-2,5| > 1,96 : **rejet de H₀**.

### Exemple 3 — temps de fabrication (TD 1)
Ancienne moyenne 6 h, variance 0,36 h² (σ = 0,6 h), n = 125. Le TD fixe une règle : conclure à une amélioration si x̄ < 5,9 h.

- Hypothèses : H₀ : μ ≥ 6 h ; H₁ : μ < 6 h.
- Statistique sous la frontière de H₀ : Z = (x̄ - 6)/(0,6/√125).
- Région de rejet : x̄ < 5,9, soit Z < (5,9 - 6)/(0,6/√125) ≈ **-1,86**.
- Risque α correspondant : P(Z < -1,86) ≈ **3,13 %** (calcul approximatif). Le TD demande de le calculer, il n'impose pas ici d'emblée α = 5 %.
- Si la vraie moyenne est 5,85 h, β = P(x̄ ≥ 5,9 | μ = 5,85) ≈ P(Z ≥ 0,932) ≈ **17,6 %**, puissance ≈ **82,4 %** (calcul approximatif à partir des données du TD).

## 7. Quand utiliser Z, Student t ou Chi-deux ?
Selon les planches finales du cours :
- **Moyenne μ :** Z lorsque l'écart-type population σ est connu et les conditions sont réunies ; Student t pour une moyenne avec σ inconnu sous les hypothèses adéquates.
- **Proportion p :** approximation normale lorsque ses conditions d'application sont satisfaites.
- **Variance σ² :** Chi-deux (χ²) lorsque l'échantillon provient d'une population normale.
- **Ajustement et indépendance :** le plan annonce des tests du Chi-deux.
- **Deux échantillons :** le plan annonce comparaison de moyennes, proportions, variances et corrélations, mais la théorie de ces chapitres n'est pas développée dans les documents disponibles.

Ne choisissez pas un test parce que le logiciel l'affiche : choisissez-le après identification du paramètre, du sens de H₁, de l'échantillonnage et des hypothèses.

## 8. Méthode de résolution en six étapes
1. Identifier **le paramètre** (μ, p, σ²...) et la population.
2. Écrire **H₀ et H₁**.
3. Déterminer **unilatéral droit, gauche ou bilatéral**.
4. Fixer **α** avant le calcul.
5. Choisir, calculer puis comparer **Z, t, χ²** ou une p-valeur, selon le cas.
6. **Conclure en contexte** économique ou de gestion (« au seuil de 5 %, les données ... »).

## 9. Exercices à préparer
Le TD 1 comprend quatre problèmes :
- effet d'une réorganisation industrielle sur le temps de fabrication (α, β, puissance) ;
- évolution de l'âge moyen de clients (test bilatéral) ;
- contenu moyen en viande d'une sauce (échantillon de 40 bocaux, σ inconnu) ;
- durée de vie moyenne d'ampoules (n = 12, moyenne de référence 2 250 h).

Les dernières diapositives incluent aussi des questions de formulation H₀/H₁, décision à partir de Z = 1,40 ou Z = -2,20, et puissance selon n, σ et α.

## 10. Quiz express
1. **Que signifie α ?** Rejeter H₀ alors qu'elle est vraie.
2. **Que signifie β ?** Ne pas rejeter H₀ alors qu'elle est fausse.
3. **Que vaut la puissance ?** 1 - β.
4. **Si l'alternative contient « différent », quel test ?** Bilatéral.
5. **Si Z = -2,20 et |Zcrit| = 1,96, au seuil bilatéral 5 % ?** Rejeter H₀.
6. **Une p-valeur de 0,03 à α = 5 % ?** Rejet de H₀ sous les hypothèses du test.
7. **Pourquoi augmenter n ?** Pour réduire l'erreur standard et en général améliorer la puissance.

## Sources étudiées et limites
- « Tests d’hypothèses S5 — Chapitre 1 », 65 pages : diapositives introductives et rappels numérisés (OCR vérifié) ; partie finale texte p. 55–64.
- « Tests sur la moyenne — TD 1 », 2 pages.
- Les nombres de l'exemple industriel et ses probabilités complémentaires ont été calculés à partir du TD, qui les présente sous forme de questions.
- Certaines formules des diapositives OCR ont pu être mal reconnues : vérifier dans le PDF original les notations et les figures.

*Cette fiche synthétise les chapitres réellement disponibles : elle ne constitue pas une synthèse de cours détaillés des chapitres 2 et 3 non transmis.*
