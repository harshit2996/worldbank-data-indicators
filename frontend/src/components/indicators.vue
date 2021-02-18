<template>
  <v-row class="indicators">
    <v-col align-self="center" class="indicators-header fill-height container ">Indicators</v-col>
    <v-hover v-for="(item,i) in indicators" :key="i">
      <v-col 
        slot-scope="{ hover }"  
        :class="(hover?'lighten-2 ':'') +(selectedIndicator.Indicators==item.Indicators?' active ':' ') +'indicator-values container fill-height'" 
        @click="indicatorSelect(item)"
        >
        {{item.Indicators}}
      </v-col>
    </v-hover>
  </v-row>
            
</template>

<script>
import axios from 'axios'
export default {
  data:()=>({
    indicators:[],
  }),

  props:['currentIndicator'],

  computed:{
    selectedIndicator:{
      get(){
        return this.currentIndicator
      },
      set(v){
        this.$emit('update:currentIndicator', v)
      }
    }

  },
  
  mounted(){
    this.selectedIndicator = this.currentIndicator
    axios.get('http://localhost:8000/display_data/')
    .then(res=>{
      this.indicators = res.data
    })
    .catch(err=>{
      console.log(err.response.data)
    })
  },

  methods:{
    indicatorSelect(item){
      this.selectedIndicator = item
    }
  }
}
</script>

<style lang="scss">
.indicators{
  text-align: center;
  border-radius: 10px;
  .indicators-header{
    border: 1px solid black;
    border-top-left-radius: 10px;
    border-bottom-left-radius: 10px;
    background-color: orange;
    justify-content: center;
  }
  .indicator-values{
    border: 1px solid black;
    background-color: rgba($color: #000000, $alpha: 0.3);
    border-left: none;
    justify-content: center;
    &:last-child{
      border-top-right-radius: 10px;
      border-bottom-right-radius: 10px;
    }
    &:hover{
      cursor: pointer;
      background-color: rgba($color: #000000, $alpha: 0.2);
    }
    &.active{
      background-color: orangered ;
    }
  }
}
</style>