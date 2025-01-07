//Team TopherAcademy1 :: Anastasia Lee, Mark Ma
//SoftDev pd4
//K27 - Basic functions in JavaScript
//2025-01-06m

//JavaScript implementations of Day0 recursive Scheme functions

//factorial:

var fact = function(n) {
    if (n == 1) {
      return n;
    }
    return n*fact(n-1);
}

//TEST CALLS
// (writing here can facilitate EZer copy/pasting into dev console now and later...)
fact(1) // should be 1
fact(5) // should be 120

//-----------------------------------------------------------------


//fib:

var fib = function(n) {
    if (n < 2) {
      return n;
    }
    return fib(n-1) + fib(n-2);
}

//TEST CALLS
// (writing here can facilitate EZer copy/pasting into dev console now and later...)
fib(0) //should be 0
fib(10) //should be 55
//=================================================================

