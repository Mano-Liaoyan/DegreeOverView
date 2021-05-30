<template>
  <a-select mode="multiple" placeholder="Select Cilos" :value="selectedItems"
            style="width: 100%" @change="handleChange">
    <a-select-option v-for="item in filteredOptions" :key="item" :value="item">
      {{ item }}
    </a-select-option>
  </a-select>
</template>
<script>
export default {
  name: "AutoHiddenSelector",
  props: {
    ids: 0
  },
  data() {
    return {
      selectedItems: [],
    };
  },
  computed: {
    filteredOptions() {
      console.log('state: ', this.$store.state.new_related_cilos)
      return this.$store.state.new_related_cilos.filter(o => !this.selectedItems.includes(o));
    },
  },
  methods: {
    handleChange(selectedItems) {
      this.selectedItems = selectedItems;
      console.log('select items', this.selectedItems)
      this.$emit("update", this.selectedItems, this.ids);
    },
  },
};
</script>
