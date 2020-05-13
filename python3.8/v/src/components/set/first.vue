<template>
  <div id="two">
    配置首页<br>
    <button @click="dj_v">vue与django结合</button>
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
    dj_v:function(){
      Router.push({path: '/set/dj_v'})
    }
   }
}
</script>