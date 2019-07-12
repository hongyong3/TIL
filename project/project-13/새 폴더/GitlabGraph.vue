<template>

<div>




    <div id="chart" class="hide_xs">

    </div>

    <h2 class="headline mt-2 text-xs-center">
      <a href="//lab.ssafy.com/DaeJeon4ban_JeongPyoYong/webmobile-sub2">GitlabRepogitory 방문</a>
    </h2>


</div>

</template>

<script>

export default {
  name: 'GitlabGraph',

  data() {
    return {
      repo: [],
      date: [],
      commits: [],

    }
  },
  components: {

  },
  mounted() {
    this.getRepo()
    const data = {
      labels: this.date,
      datasets: [
         {
             name: "Commit count", type: "bar",
             values: this.commits
         },
      ]
    }

   const chart = new frappe.Chart("#chart", {  // or a DOM element,
                                               // new Chart() in case of ES6 module with above usage
       title: "Gitlab Commit log",
       data: data,
       type: 'axis-mixed', // or 'bar', 'line', 'scatter', 'pie', 'percentage'
       height: 250,
       colors: ['#7cd6fd']
      })
  },

  methods: {
    getRepo: function () {
        axios.get('https://lab.ssafy.com/api/v4/projects/6078/events?private_token=NB7dVHnZ4-xzjAgQawUy')
        .then(response => {
            this.repo = response.data
        })
        .then(()=> {
            this.getDate()
        })
    },

    getDate: function () {

        for (var i = 0; i < this.repo.length; i++) {
            var flag = 0;

            var tempdate = this.repo[i]["created_at"].slice(0, 10)

        for (var j = 0; j < this.date.length; j++) {

            if (tempdate === this.date[j]) {
                flag = 1;
                this.commits[j] += this.repo[i]["push_data"]["commit_count"];

            }
        }
        if (flag ===0){
            this.date.push(tempdate);
            this.commits.push(this.repo[i]["push_data"]["commit_count"]);

        }
    }
}
  },
}

</script>

<style>
@media only screen and (max-width : 450px) {
  .hide_xs {
    display:none;
  }
}
</style>
