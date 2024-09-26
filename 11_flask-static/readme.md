Anastasia Lee\
peaches & mangoes\
SoftDev\
K11 -- serving static pages in flask\
2024-09-25\
time spent: 0.5 hours

Predictions:
- The pages in the static folder are not dynamic; they will not change if you reload them
- If you go to http://localhost:5000/static/foo.html, you will see "Is this plaintext, though?" in the default html font (Times New Roman), which I believe qualifies as formatting, so it is not plaintext
- If you go to http://localhost:5000/static/foo, you will see plaintext, and I think it will be a different font

DISCO:
- If you go to http://localhost:5000/static/foo, a file 'foo' is downloaded, and the file contains plaintext
- The URLs work similarly to navigating the terminal; appending `/static/` takes you to the `static` folder, etc.

QCC:
- What is the difference between a static page and a dynamic page if return statement for the dynamic page doesn't change?
- Is the text printed to the webpage in html considered plaintext?

INVESTIGATIVE APPROACH:
- copy foo.html -> fixie.html and change contents to requirements for fixie
- head to http://localhost:5000/static/fixie.html instead of http://localhost:5000/static/foo.html