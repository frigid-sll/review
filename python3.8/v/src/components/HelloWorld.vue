<template>
  <div id="two">
    请输入用户名：<input type="text" v-model="name"><br>
    请输入密码：<input type="text" v-model="password"><br>
    <button @click="start()">登陆</button>
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
      start:function(){
            this.axios.post('/api/login/',
                            Qs.stringify({  
                                name:this.name,
                                password:this.password
                            }),
                            ).then((res)=>{
                                if(res.data.code==200){
                                    alert('登录成功')
                                    Router.push({path: '/home'})
                                }else{
                                    alert('登陆失败')
                                }
                            })
        }
   }
}
</script>