```jsx

/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
    let arr = [];
    
    for (let i = 0; i < s.length; i++) {
        if (['(', '[', '{'].includes(s[i])) { 
            if (s[i] == '(') {
                arr.push(')');
            }
            else if (s[i] == '{') {
                arr.push('}');
            }
            else {
                arr.push(']');
            }      
        }
        else { 
            if (arr.length && arr[arr.length - 1] === s[i]) {
                arr.pop();
            } else {
                return false;
            }
        }
    }
    if(arr.length === 0) {
        return true;
       } else {
           return false;
       }
 
};
```;
