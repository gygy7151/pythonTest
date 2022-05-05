// you can write to stdout for debugging purposes, e.g.
// console.log('this is a debug message');

function solution(S) {
  const ans = "";
  const target = S[0];
  const cnt = 0;
  for (var x in S) {
    if (x == target && cnt < 3) {
      ans += x;
      cnt += 1;
    } else if (x !== target && cnt < 3) {
      ans += x;
      cnt = 1;
      target = x;
    }
  }
  document.write(ans);

  // write your code in JavaScript (Node.js 8.9.4)
}
