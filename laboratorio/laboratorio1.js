/*
Escribir una función recursiva que devuelva la suma de los valores almacenados en un 
arreglo unidimensional.
 Entrada. [20,10,45,39,80]
 Salida. 194

*/

function suma(arr,i){
    if(i === 0) return arr[0]
    return arr[i] + suma(arr, i - 1 )
}

console.log("\n\n----Ejercicio 1");
array = [20,10,45,39,80]
console.log("La suma de [" + array + "] es: " + suma(array ,  array.length - 1));



/*
Escribir una función recursiva que calcule y retorne el cuadrado de un numero entero n, 
n ≥ 1, mediante el siguiente método: el cuadrado de n es igual a la suma de los n primeros 
números impares. 
    Entrada. 4 
    Salida. 16 
El cuadrado de 4 es, 1 + 3 + 5 + 7 = 16.
*/

function cuad(n){
    return n === 1 ? 1 :  ( n * 2) - 1 + cuad( n - 1 )
}


console.log("\n\n----Ejercicio 2");
console.log("El cuadrado de 4 es: " + cuad(4));
console.log("El cuadrado de 5 es: " + cuad(5));
console.log("El cuadrado de 10 es: " + cuad(10));


/*

Escribir una función recursiva que, dado un numero entero positivo, devuelva la suma de 
sus dígitos pares. 
Entrada. 16582234
    Salida. 22
    Ya que, 6 + 8 + 2 + 2 + 4 = 22.
    Entrada. 13553
    Salida. 0
    Ya que ningún dígito del número es par.
    */
   
   
   
   
   
   
   
   /*
   
   Escribir una función recursiva que calcule la suma de los divisores pares de un numero
   entero positivo. 
   Entrada. 20 
   Salida. 36
   Ya que, 2 + 4 + 10 + 20 = 36
   */
  
console.log("\n\n----Ejercicio 4");


function isPar(n){
    if (n == 0) return false 
    return !( n % 2)
}

function SumaDivisoresPares(x=0,i=x){

    if(i==0) return 0
    if( !(x % i) && isPar(i) ) {
        return SumaDivisoresPares(x, i - 1) + i
    }
    
    return SumaDivisoresPares(x,i-1) 
}


console.log("La suma de los divisores pares del numero 20 es: " + SumaDivisoresPares(20));
console.log("La suma de los divisores pares del numero 14 es: " + SumaDivisoresPares(14));