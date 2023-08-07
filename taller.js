

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

        if(i === 0){
            arrC[0] = arrA[0] + arrB[0]
            return arrC
        }else {
            arrC[i] = arrA[i] + arrB[i]
            sumByIndex(i - 1)
        } 
    }
    sumByIndex(arrA.length - 1)
    return arrC
}
let A = [1,2,15,4,5,6,7]
let B = [1,2,33,-20,5,6,7]

console.log(SumArrays(A, B , A.length - 1));