<template>
  <div>
    <h2>Transport Orders</h2>
    <table>
      <thead>
        <tr>
          <th>Order Number</th>
          <th>Customer Name</th>
          <th>Order Date</th>
          <th>Waypoints</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="order in orders" :key="order.id">
          <td>{{ order.order_number }}</td>
          <td>{{ order.customer_name }}</td>
          <td>{{ order.order_date }}</td>
          <td>
            <ul>
              <li v-for="waypoint in order.waypoints" :key="waypoint.id">
                {{ waypoint.waypoint_type }} - {{ waypoint.location_name }}
              </li>
            </ul>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import axios from 'axios';

export default defineComponent({
  data() {
    return {
      orders: [],
    };
  },
  mounted() {
    this.fetchOrders();
  },
  methods: {
    async fetchOrders() {
      try {
        const response = await axios.get('http://localhost:8000/api/orders/');
        this.orders = response.data;
      } catch (error) {
        console.error(error);
      }
    },
  },
});
</script>

