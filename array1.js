"1. Create an array and print its elements."
let arr = [10,20,30]
arr.forEach(Element=>console.log(Element));

"2. Find the sum of all elements in an array."
let arr2 = [10,20,30]
let summation = 0
for (let num of arr2){
   summation += num
}
console.log(`2. Sum of elements ${summation}`)

"3.Reverse an array without using built-in functions"
let arr3 = [1,2,3,4,5,6]
let left = 0,right = arr3.length-1
while (left<right){
    let swapper = arr3[left]
    arr3[left] = arr3[right]
    arr3[right] = swapper
    left++,right--
}
console.log(`Reversed. ${arr3}`);

"4.Finding max value"
let arr4 = [1,2,3,4]
console.log(`maxvalue`,Math.max(...arr4))
"or"
let k = [1,2,3,4,5]
let max = k[0]
for (let num of arr4){
    if(num > max){
        max = num
    }
}
console.log(`Max value: ${max}`)

"5. value and index"
let myList = [10, 20, 30, 40];

myList.forEach((value, index) => {
    console.log(`Index: ${index}, Value: ${value}`)
})
"counting occurences"
function countingoccurences(arr5){
    let dic = {}
    for (let i of arr5){
        if (dic[i]) {
            dic[i] += 1;
        } else {
            dic[i] = 1;
        }
    }
    return dic
}
let arr5 = [1,2,3,3,2,2,1,1]
console.log(countingoccurences(arr5))

"Remove duplicate elements from an array"