<template>
  <div id="two">
    <b>vue的配置：</b>
    <p>
        因为vue是没有axis的  导入axios插件 就可以用axis了
        <br>

        cnpm install --save axios
        <br>

        然后在vue文件夹（myproject）里的config里的index.js里改
        <br>
        proxyTable: {
    <br>        '/api':{
    <br>        target:'http://127.0.0.1:8000/',  #这里是你要跨域的网址 django是8000，flask是5000
    <br>        changeOrigin:true,
    <br>        pathRewrite:{
    <br>            '^/api':''
    <br>            }
    <br>        }
    <br>    },
        <br>

        然后在src里的main.js里加这两行代码：
        <br>
        import axios from 'axios'
        <br>
        Vue.prototype.axios=axios
        <br>
        导入axios使vue可以用axis

    </p>
    <br>
    <b>django的配置:</b>
    <br>
    1、需要pip3 install django-cors-headers
    <br>
    2、在settings.py里做这些修改
        <br>
        a、在INSTALLED_APPS中加入'corsheaders',
        <br>
        b、在MIDDLEWARE中将
        django.middleware.csrf.CsrfViewMiddleware',
        注释掉
        <br>
        c、在MIDDLEWARE中将
        'corsheaders.middleware.CorsMiddleware'添加在 'django.middleware.common.CommonMiddleware',上面
        <br>
        d、在最后加上如下代码
        <br>
        STATIC_URL = '/static/'
        <br>
        STATICFILES_DIRS=(
            <br>
            os.path.join(BASE_DIR,'static'),
            <br>
        )
        <br>

        # 跨域增加忽略
        <br>
        CORS_ALLOW_CREDENTIALS = True
        <br>
        CORS_ORIGIN_ALLOW_ALL = True
        <br>

        CORS_ORIGIN_WHITELIST = (
            <br>
            'http://127.0.0.1:8000',
            <br>
        )
        <br>

        CORS_ALLOW_METHODS = (
            <br>
            'DELETE',
            <br>
            'GET',
            <br>
            'OPTIONS',
            <br>
            'PATCH',
            <br>
            'POST',
            <br>
            'PUT',
            <br>
            'VIEW',
            <br>
        )
        <br>

        CORS_ALLOW_HEADERS = (
            <br>
            'XMLHttpRequest',
            <br>
            'X_FILENAME',
            <br>
            'accept-encoding',
            <br>
            'authorization',
            <br>
            'content-type',
            <br>
            'dnt',
            <br>
            'origin',
            <br>
            'user-agent',
            <br>
            'x-csrftoken',
            <br>
            'x-requested-with',
            <br>
            'Pragma',
            <br>
        )
  </div>
</template>
<script>
import Qs from 'qs'
export default {
  name:'#two',
  data(){
    return{
    }
  },
  methods:{
    
   }
}
</script>