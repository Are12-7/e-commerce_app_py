$(".plus-cart").click(function () {
  var id = $(this).attr("pid").toString();
  var eml = this.parentNode.children[2];
  console.log("pid = ", id);
  $.ajax({
    type: "GET",
    url: "/plus-cart",
    data: {
      prod_id: id,
    },
    success: function (data) {
      eml.innerText = data.quantity;
      document.getElementById("subtotal").innerText = data.subtotal;
      document.getElementById("tax").innerText = data.tax;
      document.getElementById("final_price").innerText = data.final_price;
    },
  });
});

$(".minus-cart").click(function () {
  var id = $(this).attr("pid").toString();
  var eml = this.parentNode.children[2];
  $.ajax({
    type: "GET",
    url: "/minus-cart",
    data: {
      prod_id: id,
    },
    success: function (data) {
      eml.innerText = data.quantity;
      document.getElementById("subtotal").innerText = data.subtotal;
      document.getElementById("tax").innerText = data.tax;
      document.getElementById("final_price").innerText = data.final_price;
    },
  });
});

$(".remove-cart").click(function () {
  var id = $(this).attr("pid").toString();
  var eml = this;
  $.ajax({
    type: "GET",
    url: "/remove-cart",
    data: {
      prod_id: id,
    },
    success: function (data) {
      document.getElementById("subtotal").innerText = data.subtotal;
      document.getElementById("tax").innerText = data.tax;
      document.getElementById("final_price").innerText = data.final_price;
      eml.parentNode.parentNode.parentNode.parentNode.remove();
    },
  });
});

$(".plus-wishlist").click(function () {
  var id = $(this).attr("pid").toString();
  $.ajax({
    type: "GET",
    url: "/pluswishlist",
    data: {
      prod_id: id,
    },
    success: function (data) {
      //alert(data.message)
      window.location.href = `http://localhost:8000/product-detail/${id}`;
    },
  });
});

$(".minus-wishlist").click(function () {
  var id = $(this).attr("pid").toString();
  $.ajax({
    type: "GET",
    url: "/minuswishlist",
    data: {
      prod_id: id,
    },
    success: function (data) {
      window.location.href = `http://localhost:8000/product-detail/${id}`;
    },
  });
});
