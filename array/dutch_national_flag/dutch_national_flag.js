function dutchNationalFlag(arr) {
    let low = 0, mid = 0, high = arr.length - 1;

    while (mid <= high) {
        if (arr[mid] === 0) {
            [arr[low], arr[mid]] = [arr[mid], arr[low]];
            low++;
            mid++;
        } else if (arr[mid] === 1) {
            mid++;
        } else {  // arr[mid] === 2
            [arr[high], arr[mid]] = [arr[mid], arr[high]];
            high--;
        }
    }
}

const arr = [2, 0, 1, 2, 1, 0];
dutchNationalFlag(arr);
console.log(arr);  // Should print: [0, 0, 1, 1, 2, 2]
