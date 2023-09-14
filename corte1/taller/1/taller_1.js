let A = [1,2,3,4,5,6,7]
let B = [7,6,5,4,3,2,1]

/*Ejercicio 1
Cree un programa que implemente funciones recursivas y funciones iterativas que reciban
    como parámetro dos arreglos 𝑎𝑟𝑟𝑎𝑦1 𝑦 𝑎𝑟𝑟𝑎𝑦2 no vacíos de números enteros naturales y
    realicen las siguientes operaciones:
   
    a. Función que retorne un nuevo arreglo 𝑎𝑟𝑟𝑎𝑦3 con la suma de los elementos de ambos
       arreglos 𝑎𝑟𝑟𝑎𝑦1[𝑖] + 𝑎𝑟𝑟𝑎𝑦2[𝑖]

    b. Función para sumar los datos del arreglo 𝑎𝑟𝑟𝑎𝑦1, la función debe retorna el resultado
       de la suma de los datos impares.
*/

// 1-a
function SumArrays(arrA,arrB){

    let arrC = []

    function sumByIndex(i){

        arrC.unshift(arrA[i] + arrB[i])
        if(i === 0) return arrC
        sumByIndex(i - 1)
    }

    sumByIndex(arrA.length - 1)

    return arrC
}
let C = SumArrays(A,B)
console.log("\n\n----------Ejercicio 1-a----------")
console.log( C );

//1-b

function isEven(n){
    return n % 2 === 1
}

function SumArraysElementosImpares(A, i = A.length-1){
    if(i === 0) return 0
    if(isEven(A[i])) return A[i] + SumArraysElementosImpares(A,i-1)
    else return SumArraysElementosImpares(A,i-1)
}


console.log("\n\n----------Ejercicio 1-b----------")
console.log(A);
console.log(SumArraysElementosImpares(A));

