<template>
  <div id="FineDust">
    <span>{{ fineDustData['response']['body'] }}</span>
  </div>
</template>

<script>

  export default {
    name: 'FineDust',
    data () {
      return {
        fineDustData: [],
        fineDustDong: [],
      }
    },
    components: {

    },

    mounted () {
      this.fineDust()
    },

    methods: {
        fineDust: function () {
            axios.get('http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey=ZsOezhZXck%2FuuGJFlggeC2c0DGP2%2B8SPvc4r4wrLi8LQ5ST0RIfJ6GLkyG2FKMZOJjVRvEyEV%2FevatgTC1Xemg%3D%3D&numOfRows=10&pageNo=1&sidoName=%EB%8C%80%EC%A0%84&ver=1.3')
                .then((response) => {
                    this.fineDustData = response.data.response.body
                    // console.log(fineDustData.length)
                })
                // .then(() => {
                //   this.getData()
                // })
        },
      //   getData: function () {
      //     for (var i = 0; i < this.fineDustData.length; i++){
      //
      //     }
      //     .then((pm10) => {
      //       this.pm10
      //       alert('data')
      //       conosole.log(pm10)
      //       // this.dusts.push
      //     })
      // }
    },
  }

</script>
