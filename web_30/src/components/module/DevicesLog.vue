<template>
    <div id="chart">
        <apexchart type="pie" width="380" :options="chartOptions" :series="series"></apexchart>
    </div>
</template>

<script>
import Vue from "vue";
import axios from "axios";

export default {
    data: () => ({
        token: Vue.$cookies.get("token"),
        loaded: false,
        data: null,
        series: [],
        chartOptions: {
            chart: {
                width: 380,
                type: 'pie',
            },
            labels: ['Pc','Router','Switch','Other'],
            responsive: [{
                breakpoint: 480,
                options: {
                    chart: {
                        width: 200
                    },
                    legend: {
                        position: 'bottom'
                    }
                }
            }]
        },
    }),
    mounted() {
        this.Get();
    },

    methods: {
        Get() {
            axios({
                method: "GET",
                url: "http://127.0.0.1:8000/get-analysis/",
                data: JSON.stringify({}),
                headers: {
                    "Content-Type": "application/json; charset=UTF-8",
                    Authorization: `token ${this.token}`,
                },
            })
                .then((res) => {
                    this.data = res.data;
                    this.series.push(
                        res.data['report']["pc"],
                        res.data['report']["router"],
                        res.data['report']["switch"],
                        res.data['report']["other"],
                    );
                    this.loaded = true;
                })
                .catch((error) => {
                    console.log(error);
                    this.errored = true;
                });
        },
    },
};
</script>

<style></style>