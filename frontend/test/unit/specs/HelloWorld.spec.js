import Vue from 'vue'
import LogIn from '@/components/LogIn'

describe('LogIn.vue', () => {
  it('should render correct contents', () => {
    const Constructor = Vue.extend(LogIn)
    const vm = new Constructor().$mount()
    expect(vm.$el.querySelector('.login h1').textContent)
      .toEqual('Welcome to Your Vue.js App')
  })
})
