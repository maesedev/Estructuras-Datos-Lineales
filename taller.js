array1 = [1,2,3,4,5,6,7]
array2 = [1,2,3,4,5,6,7,8]
array3 = [1,2,3,100,5,6,7]


function equals(arr1,arr2, i = arr1.length - 1){
    if(arr1.length !== arr2.length)return false
    if(i == 0) return true
    if(arr1[i] === arr2[i]) return  true && equals(arr1, arr2, i -1)
    else return false

}

console.log(equals(array1, array2));
console.log(equals(array1, array3));


function sumarArr(){
}

console.log(equals(array1, array2));
console.log(equals(array1, array3));



function findIndex(Arr, n, i = Arr.length){
    if( i = -1) return -1
    if( Arr[i] == n ) return i
    else return findIndex(Arr, n, i - 1)
}

console.log(findIndex(array1,5))

