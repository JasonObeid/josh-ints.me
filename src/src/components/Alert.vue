<template>
  <div>
    <b-alert variant="success" v-show="elementVisible">{{ message }}</b-alert>
  </div>
</template>

<script>
export default {
  data() {
    return {
      elementVisible: true,
    };
  },
  props: ['message'],
  created() {
    // eslint-disable-next-line no-return-assign
    setTimeout(() => this.elementVisible = false, 2000);
  },
};

</script>
