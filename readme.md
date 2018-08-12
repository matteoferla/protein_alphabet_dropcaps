The protein alphabet is a series of protein structure views that look like letters compiled by Mark Howarth. This can be found [here](http://www.bioch.ox.ac.uk/howarth/alphabet.htm).

This css/js library makes use of it to make dropcaps. [Here is a demo](https://rawgit.com/matteoferla/protein_alphabet_dropcaps/master/demo.html).

## Use
### Option A: CDN
Add the line: `<script src="https://cdn.rawgit.com/matteoferla/protein_alphabet_dropcaps/master/protein_dropcaps-CDN.js" type="text/javascript"></script>` somewhere (preferably bottommost of body).
This will fetch it magically from the internet...
### Option B: serverside
Add the `Alphabet_ray folder` and `protein_dropcaps.js` in your website directory and add `<script src="image_dropcaps.js" type="text/javascript"></script>` (or wherever you put it).
The `protein_dropcaps.js` script is written lazily so uses a relative path that assumes `Alphabet_ray` is in the root directory. Therefore if you add the pngs to somewhere else change the path accordingly within the js file.
### Option C: full manual
If you are on Google's blogger, you cannot have `<p>` elements and JS script cannot be loaded from outside, or writing a HTML email, you most likely want to make a dropcap manually... in which case add an element like this (with the two As replaced with your letter:

    <span style="float: left; font-size: .1px; background: url('https://cdn.rawgit.com/matteoferla/protein_alphabet_dropcaps/master/Alphabet_ray/A.png') no-repeat; background-size: 40px;padding: 40px 0 0 40px; margin-right: 9px;">A</span>

### where to expect dropcaps to automatically appear
In the code, the script will automatically make a dropcap at the first letter of a paragraph element (`<p>`), either the first in a page or of a paragraph after a level one header (`<h1>`).
NB. I have not coded it to check whether there is extra markup inside the html of the p-element.

## Implementation
Annoyingly, the `p:first-child:first-letter` CSS pseudoelement is really cool, but when it comes to graphical dropcaps it does not discern between the letters.
Therefore, here a JS script finds the first letter and alters it (e.g. `<span class=drop-X`>X</span>) and loads only the needed figure.

The JS can be circumvented by doing it manually and adding a span with the class drop-A or whatever letter and using the whole of the `dropcaps.css` style sheet or only the required parts.

Soon SVG fonts, aka. color fonts, will hit the web fully. This is great and it means that the p:first-child:first-letter pseudoelement could work with a custom SVG font of protein alphabet. But the pretty major catch is that a PyMol view cannot be exported as SVG and illustrator does not do a clean job of vectorising the images.

## Figure generations
The figures were generated with a series of commands make with the `make_png_script.py` python3 script.

## Coming up
I think a bunch of protein complexes throbbers (spinning things, like circle of balls or marble, that appear when you wait) would be fun...
Similarly to this: [github.com/matteoferla/Spinning-Python](https://github.com/matteoferla/Spinning-Python).