The protein alphabet is a series of protein structure views that look like letters compiled by Mark Howarth. This can be found [here](http://www.bioch.ox.ac.uk/howarth/alphabet.htm).
This css/js library makes use of it to make dropcaps. [Here is a demo](https://rawgit.com/matteoferla/protein_alphabet_dropcaps/master/demo.html).

## Use
To use it the js simply add `Alphabet_ray folder` and `protein_dropcaps.js` in your website directory and add `<script src="image_dropcaps.js"></script>` (or wherever you put it) somewhere (preferably bottommost of body).
The protein_dropcaps.js script is written lazily so uses a relative path that assumes `Alphabet_ray` is in the root directory. Therefore if you add the pngs to somewhere else change the path accordingly within the js file.
In the code, it will make a dropcap at the first letter of a paragraph element (`<p>`), either the first in a page or of a paragraph after a level one header (`<h1>`).

## Implementation
Annoyingly, the `p:first-child:first-letter` CSS pseudoelement is really cool, but when it comes to graphical dropcaps it does not discern between the letters.
Therefore, here a JS script finds the first letter and alters it (e.g. `<span class=drop-X`>X</span>) and loads only the needed figure.
The JS can be circumvented by doing it manually and adding a span with the class drop-A or whatever letter and using the whole of the `dropcaps.css` style sheet or only the required parts.

## Figure generations
The figures were generated with a series of commands make with the `make_png_script.py` python3 script.

## Coming up
I think a bunch of protein complexes throbbers (spinning things, like circle of balls or marble, that appear when you wait) would be fun...
Similarly to this: [github.com/matteoferla/Spinning-Python](https://github.com/matteoferla/Spinning-Python).