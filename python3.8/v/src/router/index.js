import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import home from '@/components/home'
import first from '@/components/set/first'
import dj_v from '@/components/set/dj_v'
import one from '@/components/python/one'
import a from '@/components/python/a'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'HelloWorld',
      component: HelloWorld
    },
    {
      path: '/home',
      name: 'home',
      component: home
    },
    {
      path: '/set/first',
      name: 'first',
      component: first
    },
    {
      path: '/set/dj_v',
      name: 'dj_v',
      component: dj_v
    },
    {
      path: '/python/one',
      name: 'one',
      component: one
    },
    {
      path: '/python/a',
      name: 'a',
      component: a
    },
  ]
})
