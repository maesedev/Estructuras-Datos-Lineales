let A = [1,2,3,4,5,6,7]
let B = [7,6,5,4,3,2,1]


function search(arr,n){

    let i = arr.length - 1
    const iterate= i =>{
        if(i == -1) return -1

        if(arr[i ] == n) return i 

        else return iterate(i-1)
    
    }
    return iterate(i)
}

console.log("The index is: ",search([1,2,3,4,5] , 3));