let A = [1,2,3,4,5,6,7]
let B = [7,6,5,4,3,2,1]

/*
Ejercicio 2
    Cree un programa que implemente una función recursiva y función iterativa que reciba como
    parámetros dos arreglos 𝑎𝑟𝑟𝑎𝑦 𝑦 𝑎𝑟𝑟𝑎𝑦2 no vacíos de números enteros y retorne un booleano
    indicando si los arreglos son iguales, es decir, si tienen los mismos valores en las mismas
    posiciones.
*/


function equals(arr1,arr2, i = arr1.length - 1){
    if(arr1.length !== arr2.length)return false
    if(i == 0) return true
    if(arr1[i] === arr2[i]) return  true && equals(arr1, arr2, i -1)
    else return false

}

function equals2(arr1,arr2){

    const recursive=(i)=>{
        if(arr1.length !== arr2.length)return false
        if(i == 0) return true
        if(arr1[i] === arr2[i]) return  true && recursive(i -1)
        else return false
    }

    return recursive(arr1.length)

}


//console.log("\n\nRecursive: ",equals2([1,2,3],[1,2,3]));






