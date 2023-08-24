arr = [1,2,3,4,5]
n = 4
valor = -1 //indice

for(let i = arr.length - 1; i != -1 ; i--){
     if(arr[i] === n ){
        valor = i
        break
     } 
}

console.log(valor);