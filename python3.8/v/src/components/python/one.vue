<template>
  <div id="two">
    <button @click="a">基础语法</button>
  </div>
</template>
<script>
import Qs from 'qs'
import Router from '@/router/index'
export default {
  name:'#two',
  data(){
    return{
    }
  },
  methods:{
    a:function(){
      Router.push({path: '/python/a'})
    }
   }
}
</script>