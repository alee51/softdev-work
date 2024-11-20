# K22: Testing On-Ramps + Other FEFs
lilyPigs: Anastasia Lee, Andy Shyklo
## DISCO
- Dropdown menu doesn't work without JS
- In body, insert `background-image: url('path/to/image')` to change the website background to an image of your choosing
- `background-repeat` determines whether the background image repeats after it ends
- Use `img` element to insert images
- `overflow: hidden` disables scrolling

- You have to add the script within the head for tailwind using `<script src="https://cdn.tailwindcss.com"></script>`
- You can add styling within tailwind using another script, an within it using tailwind.config to configure elements like theme, font, and colors

## QCC
- Not all images work well as a background; it's best to choose one that has a seamless transition between the bottom to the top of its repetitions
- Foundation and bootstrap are both similar to normal HTML and CSS
- What is the purpose of the z-index in the overlay formatting?
- How can I put two overlay images side-by-side?
- When is one FEF better suited for a project than another?
- How can we use animations better, like with integrating them directly into our website rather than using presets for things like the loading animation?
- Styling is defined through class="" instead of style="", and is generally a lot more streamlined and clearer to use, and also has more features. 
- It somewhat resembles a more accessible and feature-full CSS. 
- Most importantly, you can set fonts with font-(font that you defined), margins (m-1, mt-2), and text size (text-xl). 
- A lot of elements use span html elements and include many classes from tailwind in their designs. 
- Generally, Tailwind just allows you to have a more interactive and responsive website, like with the loading button.
## Q0: Did you have to consult resources beyond your Devo-generated on-ramp?
1
## Q0b: If answer to preceding question is 1, cite all resources consulted -- including verbal consultations and/or neighbouring team's readme. 1citation/line.
Asked Jady whether she used any JS, and which line in the app.css file disables scrolling\
Tailwind documentation for the cursor loading effect on the buttons: https://tailwindcss.com/docs/cursor\
More information on margins, and some smaller features: https://tailwindcss.com/docs/margin
## Q1: At this point, which FEF do you prefer, and why?
Anastasia: I think I prefer Bootstrap, because it is quite versatile and does not depend on CSS and JS as much as the other FEFs do.\
Andy: I think I prefer Bootstrap the most, since most of its details are a lot more immersive and I think it is genenerally a lot more developed, although it is slightly more confusing than Tailwind. Basically, if I was making a simple website, I would use Tailwind, but for more robust websites, I would use Bootstrap.