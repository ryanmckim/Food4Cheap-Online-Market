const openCartButtons = document.querySelectorAll("[data-cart-target]");
const closeCartButtons = document.querySelectorAll("[data-close-button]");
const overlay = document.getElementById("overlay");

openCartButtons.forEach((button) => {
  button.addEventListener("click", () => {
    const cart = document.querySelector(button.dataset.cartTarget);
    openCart(cart);
  });
});

overlay.addEventListener("click", () => {
  const carts = document.querySelectorAll(".cart__details.active");
  carts.forEach((cart) => {
    closeCart(cart);
  });
});

closeCartButtons.forEach((button) => {
  button.addEventListener("click", () => {
    const cart = button.closest(".cart__details");
    closeCart(cart);
  });
});

function openCart(cart) {
  if (cart == null) {
    return;
  }

  cart.classList.add("active");
  overlay.classList.add("active");
}

function closeCart(cart) {
  if (cart == null) {
    return;
  }

  cart.classList.remove("active");
  overlay.classList.remove("active");
}

function purchase() {
  alert("purchase complete");
}