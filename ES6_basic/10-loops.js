export default function appendToEachArrayValue(array, appendString) {
    let index = 0;
    for (const value of array) {
        /* eslint-disable no-param-reassign */
        array[index] = appendString + value;
        index += 1;
    }

    return array;
}