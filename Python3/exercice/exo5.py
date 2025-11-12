On a mesuré la différence de potentiel en fonction du courant dans une cellule photovoltaïque. Les 14 points de mesure se trouvent ci-dessous. On aimerait connaître la valeur du courant pour laquelle la puissance est maximale et la valeur de cette puissance maximale. Comme nous n'avons que 14 mesures, il est judicieux d'interpoler les données afin d'estimer au mieux ces valeurs. 

|I(mA)|0.00|0.07|0.73|1.43|3.41|6.01|7.32|7.59|7.68|7.77|7.81|7.88|7.91|7.92|
|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|
|V(mV)|745|744|736|729|696|615|460|331|258|187|151|98.6|67.6|46.4|

<ol>
<li>Faites le graphe de la puissance en fonction du courant pour ces 14 points de données afin d'avoir une idée grossière de la courbe continue sous-jacente (rappel : $P=VI$).</li>
<li>Testez les méthodes d'interpolation suivantes: linéaire et spline.</li>
<li>Sur chacune de vos courbes interpolées, localisez le maximum via fmin (de scipy.optimize) et reportez ce point sur votre graphe de la puissance en fonction du courant (le point doit être bien visible).</li>
</ol>
# Courants
I=np.array([0.00,0.07,0.73,1.43,3.41,6.01,7.32,7.59,7.68,7.77,7.81,7.88,7.91,7.92])
# Tensions
U=np.array([745,744,736,729,696,615,460,331,258,187,151,98.6,67.6,46.4])