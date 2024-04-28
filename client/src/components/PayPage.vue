<template>
    <div class="page">
        <h1>Betalning</h1>
        <p>Du kommer nu att skickas vidare för att slutföra betalning för att publicera din annons. 
            <br>När betalningen har gått igenom kommer din annons att publiceras. 
        </p>
        <h4>10 kr</h4>
        <button id="checkout-button" @click="handlePayment">Gå vidare till betalning</button>
    </div>
</template>
  
<script>
import{ loadStripe } from '@stripe/stripe-js';

export default {
  methods: {
    async handlePayment() {
      // Skapa en instans av Stripe med din offentliga nyckel
      const stripeI = await loadStripe('pk_test_51P2BEGRxv3wNoBa56OkuHUm7ujXysUE7MdJad53O4K8wPu34dfaa9rZ4pK6ufYFuR9MAoyudKqeLMGluAa2R8kyn00cRii90ll');

      // Initiera betalningen med Stripe Checkout
      const { error } = await stripeI.redirectToCheckout({
        lineItems: [{ price: 'price_1P2BtYRxv3wNoBa5KtgSnE4g', quantity: 1 }],
        mode: 'payment',
        successUrl: 'http://localhost:8080/#/ad-confirm',
        cancelUrl: 'http://localhost:8080/#/home',
      });

      if (error) {
        console.error('Betalningsfel:', error);
      }
    }
  }
}
</script>

<style scoped>
.page {
    padding: 50px;
    min-height: 80vh;
    margin: 0 auto;
  }

  h1 {
    font-weight: bold;
    font-size: 50px;
    color: #0c264d;
    padding-bottom: 30px;
  }

  h4 {
    color: #0c264d
  }

  button {
    margin-top: 20px;
  }
</style>


