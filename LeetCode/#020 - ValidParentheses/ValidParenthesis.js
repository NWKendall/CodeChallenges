var isValid = function (str) {
  let stack = [];
  let bracket = {
    "(": ")",
    "{": "}",
    "[": "]",
  };

  for (let char of str) {
    if (bracket[char]) {
      stack.push(bracket[char]);
    } else {
      if (stack.pop() !== char) return false;
    }
  }
  if (stack.length != 0) return false;

  return true;
};
