# Estimating Exponent for Pythagorean Method of Expected Win Percentage in Various Leagues

## Background
Bill James defined the ["Pythagorean Theory of Baseball,"](https://www.baseball-reference.com/bullpen/Pythagorean_Theorem_of_Baseball) so named because of superficial similarity to the Pythagorean Theorum for finding the length of the hypatenuse c of a right triangle abc: ````a^2 + b^2 = c^2````. [Other statisticians](http://www.rawbw.com/~deano/helpscrn/pyth.html) have since adapted the method for other sports, with different exponents to account for different scoring systems. For example, in basketball, [ESPN uses ^16.5](http://www.espn.com/nba/stats/rpi). 

How closely do these numbers work for recent seasons? What numbers should be used for other sports? How have the numbers changed over time, and are they actually any good for other sports?

I start here with the NHL.

## Collection
I requested points scored for and against and comparing that to win% for each franchise in the history of the NHL using the official API. 

## Visualization
![A scatterplot with trend line, showing a fairly cloudy distribution.](plot_NHL_exponents.png)

## Interpretation
[Kevin Dayaratna and Steven J. Miller](https://web.williams.edu/Mathematics/sjmiller/public_html/math/papers/DayaratnaMiller_HockeyFinal.pdf) estimated an exponent slightly greater than 2 for hockey, though the above chart suggests an exponent slightly lower than 2 would be better.
