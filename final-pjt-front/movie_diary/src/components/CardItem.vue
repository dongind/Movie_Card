<template>
  <div>
    {{ userId }} : {{ content }}
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'CardItem',
  props: {
    cardId: Number,
  },
  data() {
    return {
      userId: null,
      content: null,
    }
  },
  computed: {
    
  },
  methods: {
    getCardItem() {
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/api/v1/cards/${this.cardId}`,
        headers: {'Authorization': `Token ${this.$store.state.token}`}
      })
        .then((response) => {
          this.userId = response.data.user
          this.content = response.data.content
        })
    }
  },
  created() {
    this.getCardItem()
  }
}
</script>

<style>

</style>