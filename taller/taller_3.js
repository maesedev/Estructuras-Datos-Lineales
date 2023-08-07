let A = [1,2,3,4,5,6,7]
let B = [7,6,5,4,3,2,1]

/*
Ejercicio 3
    Cree un programa que implemente una función recursiva y función iterativa que reciba como
    parámetros dos arreglos 𝑎𝑟𝑟𝑎𝑦1 𝑎𝑟𝑟𝑎𝑦2 no vacíos de números enteros positivos o negativos y
    retorne un nuevo arreglo 𝑎𝑟𝑟𝑎𝑦3 con los elementos de ambos arreglos.
    Ejemplo:
        Entrada f([2, 10, 99], [-1, 8, 200])
        Salida [-1,2,8.10,99,200]
*/






function juntarElementos(arrA,arrB){
    let i = arrA.length - 1
    let arrC = []
    const sumByIndex = (i)=>{


        arrC.unshift(...order( arrA[i] , arrB[i] ) );
        if(i === 0) return arrC
        return sumByIndex(i - 1)
    }
    const order = (a,b) => a < b ? [a,b] :[b,a]  

    return sumByIndex(i)
}

console.log("\n\n----------Ejercicio 3 ----------")

console.log(juntarElementos(
    [2, 10, 99],
    [-1, 8, 200]));