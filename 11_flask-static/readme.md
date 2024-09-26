Anastasia Lee\
peaches & mangoes\
SoftDev\
K11 -- serving static pages in flask\
2024-09-25\
time spent: 0.5 hours

Predictions:
- The home page will be the same as in previous assignments; that part of the code has not been modified
- The pages in the static folder are not dynamic; they will not change if you reload them
- If you go to http://localhost:5000/static/foo.html, you will see "Is this plaintext, though?" in the default html font (Times New Roman), which I believe qualifies as formatting, so it is not plaintext
- If you go to http://localhost:5000/static/foo, you will see plaintext, and I think it will be a different font than Times New Roman
- If you uncomment the code block in app.py, the function h() will be run:
  - the name of the module is \_\_main__, and this will be printed to the terminal
  - a random number between 0 and 1 will be generated and printed to http://localhost:5000/static/foo.html
  - the random number will not change if you reload the webpage because it is static

DISCO:
- If you go to http://localhost:5000/static/foo, a file 'foo' is downloaded, and the file contains plaintext
- The URLs work similarly to navigating the terminal; appending `/static/` takes you to the `static` folder, etc.
- If you uncomment the code block in app.py, reloading http://localhost:5000/static/foo.html does change the random number

QCC:
- What is the difference between a static page and a dynamic page if return statement for the dynamic page doesn't change?
- Is the text printed to the webpage in html considered plaintext?
- What is a static webpage if not a webpage that doesn't change when you reload it? Does the debugger have priority over the static-ness of a webpage?

INVESTIGATIVE APPROACH:
- copy foo.html -> fixie.html and change contents to requirements for fixie
- head to http://localhost:5000/static/fixie.html instead of http://localhost:5000/static/foo.html