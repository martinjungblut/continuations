let with_cc = (capture_continuation, continuation) => {
  capture_continuation(continuation);
  return continuation;
};

let add1 = (n, k) => k(n + 1);
let mul5 = (n, k) => k(n * 5);

var captured_continuation = undefined;

with_cc(cont => {
  captured_continuation = cont;
}, a => {
  add1(a, b => {
    mul5(b, c => {
      console.log(c);
    });
  });
})(10);

captured_continuation(3);
captured_continuation(4);
