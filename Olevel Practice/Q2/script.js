const calc = function () {
  let num1 = Number(document.getElementById("num1").value);
  let num2 = Number(document.getElementById("num2").value);
  let showAddition = document.getElementById("add");
  let showSubtraction = document.getElementById("sub");
  let showProduct = document.getElementById("multi");
  let showDivision = document.getElementById("div");
  if (num1 && num2) {
    document.getElementById("output").style = "display:block";
    document.getElementById("error-message").style = "display:none;color: red;";
    showAddition.value = num1 + num2;
    showSubtraction.value = num1 - num2;
    showProduct.value = num1 * num2;
    showDivision.value = num1 / num2;
  } else {
    document.getElementById("error-message").style =
      "display:block;color: red;";
  }
};
