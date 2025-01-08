// Team TopherAcademy1 :: Anastasia Lee, Mark Ma
// SoftDev pd4
// K28 -- Getting more comfortable with the dev console and the DOM
// 2025-01-07t
// --------------------------------------------------


//send diagnostic output to console
//(Ctrl-Shift-K in Firefox to reveal console)
console.log("AYO");

var i = "hello";
var j = 20;


//assign an anonymous fxn to a var
var f = function(x) 
{
    var j=30;
    return j+x;
};


//instantiate an object
var o = { 'name' : 'Thluffy',
          age : 1024,
          items : [10, 20, 30, 40],
          morestuff : {a : 1, b : 'ayo'},
          func : function(x) {
              return x+30;
          }
        };

//create a new node in the tree
var addItem = function(text)
{
    var list = document.getElementById("thelist");
    var newitem = document.createElement("li");
    newitem.innerHTML = text;
    list.appendChild(newitem);
};

//prune a node from the tree
var removeItem = function(n)
{
    var listitems = document.getElementsByTagName('li');
    listitems[n].remove();
};

//color selected elements red
var red = function()
{
    //original:
    // var items = document.getElementsByTagName("li");
    // for(var i = 0; i < items.length; i++) {
    //     items[i].classList.add('red');
    // }

    //mine:
    var items = document.getElementsByTagName("li");
    for(var i = 0; i < items.length; i++) {
        var cl = items[i].classList;
        for (var k = 0; k < cl.length; k++) {
            cl.remove(cl[0]);
        }
	    cl.add('red');
    }
    for(var i = 0; i < items.length; i++) {
        var cl = items[i].classList;
        for (var k = 0; k < cl.length; k++) {
            cl.remove(cl[0]);
        }
	    cl.add('red');
    }
};

//color a collection in alternating colors
var stripe = function()
{
    var items = document.getElementsByTagName("li");
    for(var i = 0; i < items.length; i++) {
        if (i%2==0) {
            items[i].classList.add('red');
        } else {
            items[i].classList.add('blue');
        }
    }
};


//insert your implementations here for...
// FIB
var fib = function(n) {
    if (n < 2) {
      return n;
    }
    return fib(n-1) + fib(n-2);
}
//send diagnostic output to console
console.log(fib(10));

// FAC
var fact = function(n) {
    if (n == 1) {
      return n;
    }
    return n*fact(n-1);
}
//send diagnostic output to console
console.log(fact(5));

// GCD
var gcd = function(a, b) {
    if (b == 0) {
        return a;
    }
    return gcd(b, (a % b));
}
//send diagnostic output to console
console.log(gcd(120, 256));

// In addition to the style shown above,
//  you are encouraged to test drive the "arrow function syntax" as shown below.
//  Note anything notable.
const myFxn = (param1, param2) => {
    // body
    return retVal;
};


