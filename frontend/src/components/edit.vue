<template>
  <v-dialog
    v-model="open"
    width="500"
  >

    <v-card>
      <v-card-title class="headline grey">
        Edit Values
      </v-card-title>
      <v-divider></v-divider>

      <v-form>
        <v-card-text>
          <v-col class="fill-height">
              <v-text-field v-for="(value, name) in rowData" v-model="formData[name]" :key="name" :label="name"></v-text-field>
          </v-col>
        </v-card-text>

        <v-divider></v-divider>

        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn
            color="primary"
            text
            @click="submit"
          >
            Submit
          </v-btn>
        </v-card-actions>
      </v-form>
    </v-card>
  </v-dialog>
</template>

<script>
  import axios from 'axios'
  export default {
    name: 'EditItem',

    props:['dialog', 'rowData', 'indicator'],

    computed:{
      open:{
        get(){
          return this.dialog
        },
        set(v){
          this.$emit('update:dialog',v)
        }
      },

      formData:{
        get(){
          let temp = {}
          for(const property in this.rowData){
            temp[property] = this.rowData[property]
          }
          return temp
        },
        set(){
        }
      }

    },

    methods:{
      submit(){
        axios.patch('http://localhost:8000/display_data/'+this.indicator, this.formData )
        .then(()=>{
          for(const property in this.formData){
            this.rowData[property] = this.formData[property]
          }
          this.open = !this.open
        })
        .catch(err=>{
          console.log(err.response.data)
          this.open = !this.open
        })
      }
    }

  }
</script>
