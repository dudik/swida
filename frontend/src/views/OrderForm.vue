<template>
  <div>
    <h2>Create Transport Order</h2>
    <form @submit.prevent="submitForm">
      <div>
        <label>Order Number</label>
        <input v-model="order.order_number" type="text" required />
      </div>
      <div>
        <label>Customer Name</label>
        <input v-model="order.customer_name" type="text" required />
      </div>
      <div>
        <label>Order Date</label>
        <input v-model="order.order_date" type="datetime-local" required />
      </div>

      <div v-for="(waypoint, index) in order.waypoints" :key="index">
        <label>Waypoint Location</label>
        <input v-model="waypoint.location_name" type="text" required />
        <label>Waypoint Type</label>
        <select v-model="waypoint.waypoint_type">
          <option value="pickup">Pickup</option>
          <option value="delivery">Delivery</option>
        </select>
        <button @click="removeWaypoint(index)">Remove Waypoint</button>
      </div>

      <button @click="addWaypoint">Add Waypoint</button>
      <button type="submit">Submit</button>
    </form>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import axios from 'axios';

export default defineComponent({
  data() {
    return {
      order: {
        order_number: '',
        customer_name: '',
        order_date: '',
        waypoints: [
          {
            location_name: '',
            waypoint_type: 'pickup',
          },
        ],
      },
    };
  },
  methods: {
    addWaypoint() {
      this.order.waypoints.push({
        location_name: '',
        waypoint_type: 'pickup',
      });
    },
    removeWaypoint(index: number) {
      this.order.waypoints.splice(index, 1);
    },
    async submitForm() {
      try {
        const response = await axios.post('http://localhost:8000/api/orders/', this.order);
        alert('Order created successfully!');
      } catch (error) {
        console.error(error);
        alert('Error creating order.');
      }
    },
  },
});
</script>

