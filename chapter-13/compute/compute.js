function range(m, n) {
  return [...Array(n - m).keys()]
    .map(x => x + m);
}

function isEven(n) {
  return n % 2 === 0;
}

function repeat(n, times) {
  return Array(times).fill(n);
}

// JS has a flatMap() that combines mapping with flattening. Flattening is what
// reduce + this concat function would do, so we don't really need this
// function in JS.
function concat(list_a, list_b) {
  return [...list_a, ...list_b]
}

function computed() {
  return range(1, 8)
    .filter(isEven)
    .flatMap(n => repeat(n, n));
}

console.log(computed())
