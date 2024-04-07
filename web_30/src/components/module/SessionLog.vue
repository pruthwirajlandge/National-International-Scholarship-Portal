<template>
    <div id="chart">
        <apexchart type="pie" width="390" :options="chartOptions" :series="series"></apexchart>
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
            labels: [],
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
                    console.log(this.chartOptions['labels']);
                    for (const iterator of res.data['session_report']) {
                        this.series.push(
                            iterator["session_count"],
                        );
                        this.chartOptions['labels'].push(
                            iterator["user"],
                        );
                    }

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