# pj-django_vue_post_init
```js
  <script>
        var vm = new Vue({
                     el:'#box',
                     data:{
                             myData:[],
                     },
                     methods:{
                             post:function(){
                                     this.$http.post('url').then(function(res){
                                             this.myData=res.data;
                                             console.log(this.myData);
                                     });
                                 }
                     }
             });
        vm.post();
  </script>    

```
