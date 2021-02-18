<template>
  <v-snackbar
      v-model="snackbar"
      multi-line
    >
      <ul>
        <li v-for="(value,name) in message" :key="name">{{name}} : {{value}}</li>
      </ul>

      <template v-slot:action="{ attrs }">
        <v-btn
          color="red"
          text
          v-bind="attrs"
          @click="snackbar = false"
        >
          Close
        </v-btn>
      </template>
    </v-snackbar>
</template>

<script>
export default {
  name:"ErrorComponent",

  props:['message', 'trigger'],

  computed:{
    snackbar:{
      get(){
        return this.trigger
      },
      set(v){
        this.$emit('update:trigger',v)
      }

    }
  }
}
</script>

<style>

</style>