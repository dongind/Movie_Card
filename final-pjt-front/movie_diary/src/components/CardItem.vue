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
    card: Object,
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
        url: `http://127.0.0.1:8000/api/v1/cards/${this.card.id}/`,
        // headers: {'Authorization': `Token ${this.$store.state.token}`}
      })
        .then((response) => {
          this.userId = response.data.user
          this.content = response.data.content
          // console.log('됨ㅋ ')
          const cardInfo = {
            'userId': this.userId,
            'content': response.data.content,
          }
          this.$emit('get-card-item', cardInfo)
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