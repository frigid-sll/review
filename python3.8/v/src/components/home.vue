<template>
  <div id="two">
    <button @click="set">配置</button>
    <br>
    <button @click="py">python</button>
    <br>
  </div>
</template>
<script>
import Qs from 'qs'
import Router from '@/router/index'
export default {
  name:'#two',
  data(){
    return{
      name:'',
      password:''
    }
  },
  methods:{
      set:function(){
          Router.push({path: '/set/first'})
      },
      py:function(){
          Router.push({path: '/python/one'})
      }
   }
}
</script>