// /** @odoo-module **/

import { registry } from "@web/core/registry";
import { getDefaultConfig } from "@web/views/view";
import { useService } from "@web/core/utils/hooks";
import { Component, useSubEnv, useState, useRef, onWillStart } from "@odoo/owl";
import { EasyOrderProducts } from "../product/product_component";
import { EasyOrderProductsShoppingCart } from "../cart/cart_component";

export class EasyOrder extends Component {
  setup() {
    useSubEnv({
      config: {
        ...getDefaultConfig(),
        ...(this.env.config || {}),
      },
    });
    this.notificationService = useService("notification");
    // this.notificationService.add("Hello, Welcome to Easy Order!");
    this.state = useState({
      amount_total: 0,
      products: [],
      shoppingCart: [],
    });
    // this.state.products = useService("easyOrder.getProducts");

    this.productModel = "product.product";
    this.orm = useService("orm");
    this.searchInput = useRef("search-input");

    onWillStart(async () => {
      await this.getAllProducts();
    });
  }

  // async getAllProducts() {
  //   this.state.products = await this.orm.searchRead(
  //     this.productModel,
  //     [["detailed_type", "!=", "service"]],
  //     ["name", "list_price",'default_code', "standard_price", "image_128"]
  //   );

  async getAllProducts() {
    // Step 1: Fetch products
    const products = await this.orm.searchRead(
      this.productModel,
      [["detailed_type", "!=", "service"]],
      [
        "id",
        "name",
        "list_price",
        "default_code",
        "standard_price",
        "image_128",
      ]
    );

    if (products.length === 0) {
      this.state.products = []; // No products found
      return;
    }

    // Step 2: Fetch stock quantities
    const productIds = products.map((p) => p.id);
    const stockQuants = await this.orm.searchRead(
      "stock.quant",
      [["product_id", "in", productIds]],
      ["product_id", "quantity"]
    );

    console.log("Stock quantities fetched:", stockQuants);
    // console.log(typeof default_code);

    // Step 3: Create stock mapping
    // const stockMap = stockQuants.reduce((acc, stock) => {
    //   const prodId = stock.product_id[0];
    //   acc[prodId] = (acc[prodId] || 0) + stock.quantity; // Sum quantities
    //   return acc;
    // }, {});

    // Step 4: Attach on-hand quantity to products
    // const updatedProducts = products.map((product) => ({
    //   ...product,
    //   onHandQty: stockMap[product.id] ?? 0,
    // }));

    // const updatedProducts = products.map(product => {
    //   console.log("Processing product:", product.id, "Stock:", stockMap[product.id] || 0);
    //   return {
    //     ...product,
    //     onHandQty: stockMap[product.id]  ?? 0, // Use `||` instead of `??` for undefined cases
    //   };
    // });
    // const updatedProducts = products.map(product => ({
    //   ...product,
    //   onHandQty: stockMap[product.id] || 0, // Default to 0 if not found
    // }));
    const updatedProducts = products.map((product) => {
      const stockEntry = stockQuants.find(
        (sq) => sq.product_id[0] === product.id
      );
      return { ...product, onHandQty: stockEntry ? stockEntry.quantity : 0 };
    });

    // Step 5: Update state
    this.state.products = updatedProducts;
  }

  async searchProducts() {
    const textProduct = this.searchInput.el.value;
    this.state.products = await this.orm.searchRead(
      this.productModel,
      [["name", "ilike", textProduct]],
      ["name", "list_price", "standard_price", "image_128"]
    );
  }
  addToCard(productId) {
    // this.state.shoppingCart.push(productId);
    const productIndex = this.state.products.findIndex(
      (product) => product.id === productId
    );
    const productcartIndex = this.state.shoppingCart.findIndex(
      (product) => product.id === productId
    );
    if (productcartIndex === -1) {
      this.state.shoppingCart.push({
        id: productId,
        name: this.state.products[productIndex].name,
        list_price: this.state.products[productIndex].list_price,
        standard_price: this.state.products[productIndex].standard_price,
        quantity: 1,
        price_subtotal: this.state.products[productIndex].list_price * 1,
      });
    } else {
      this.state.shoppingCart[productcartIndex].quantity += 1;
      this.state.shoppingCart[productcartIndex].price_subtotal =
        this.state.products[productIndex].list_price *
        this.state.shoppingCart[productcartIndex].quantity;
    }

    this.state.amount_total = this.state.shoppingCart.reduce(
      (total, product) => {
        return total + product.price_subtotal;
      },
      0
    );

    // this.notificationService.add(
    //   `Product "${this.state.products[productIndex].name}" is added to the cart.`
    // );

    // this.state.amount_total=this.state.shoppingCart.reduce((total,product)=>
    //   total+(product.price_subtotal).toFixed(2),2);
  }

  removeFromCard(productId) {
    const productIndex = this.state.products.findIndex(
      (product) => product.id === productId
    );
    //const productcartIndex=this.state.shoppingCart.findIndex(product=> product.id === productId)
    if (productIndex !== -1) {
      if (this.state.shoppingCart[productIndex].quantity > 1) {
          this.state.shoppingCart[productIndex].quantity -= 1;
          this.state.shoppingCart[productIndex].price_subtotal =
          this.state.shoppingCart[productIndex].list_price *
          this.state.shoppingCart[productIndex].quantity;
      } else {
        this.state.shoppingCart[productIndex].quantity = 0;
        this.state.shoppingCart[productIndex].price_subtotal = 0;
        this.state.shoppingCart.splice(productIndex, 1);
      }
    } else {
      // this.notificationService.add("Product Not Found In Card");
    }
    this.state.amount_total = this.state.shoppingCart.reduce(
      (total, product) => {
        return total + product.price_subtotal;
      },
      0
    );

    // Define an async function to handle the RPC call

    // this.notificationService.add(
    //   `Product "${this.state.products[productIndex].name}" is removed from the cart.`
    // );
  }

  // removeFromCard(productId) {
  //   const productIndex = this.state.products.findIndex(
  //     (product) => product.id === productId
  //   );
  //   // Find the product in shoppingCart
  //   const productCartIndex = this.state.shoppingCart.findIndex(
  //     (product) => product.id === productId
  //   );
  //   if (productCartIndex === -1) {
  //     console.warn(`Product ID ${productId} not found in shopping cart.`);
  //     return; // Stop execution if product is not found
  //   }
  
  //   let updatedCart = [...this.state.shoppingCart]; // Create a copy
  
  //   if (updatedCart[productCartIndex].quantity > 1) {
  //       updatedCart[productCartIndex].quantity -= 1;
  //       updatedCart[productCartIndex].price_subtotal =
  //       updatedCart[productCartIndex].list_price * updatedCart[productCartIndex].quantity;
  //   } else {
  //     // updatedCart[productCartIndex].name = "";
  //     updatedCart[productCartIndex].quantity = 0;
  //     updatedCart[productCartIndex].price_subtotal = 0;
  //     updatedCart.splice(productCartIndex, 1);
  //   }
  
  //   // Recalculate total
  //   this.state.amount_total = updatedCart.reduce((total, product) => total + product.price_subtotal, 0);
  
  //   // Update state
  //   // this.setState({
  //   //   shoppingCart: updatedCart,
  //   //   amount_total: newTotal
  //   // });
  
  //   // Show notification (optional)
  //   // this.notificationService.add(`Product "${updatedCart[productCartIndex]?.name || ''}" removed from the cart.`);
  // }
  
 
  
  
}

EasyOrder.template = "easyorder.EasyOrder";
EasyOrder.components = { EasyOrderProducts, EasyOrderProductsShoppingCart };
// Ensure this is properly registered
registry.category("actions").add("easyorder.basecomponent", EasyOrder);

// console.log("EasyOrder registered successfully!");
