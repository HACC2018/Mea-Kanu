import firebase from "nativescript-plugin-firebase";
import config from "./shared/firebase-config";

import Vue from "nativescript-vue";

import RadListView from "nativescript-ui-listview/vue";

Vue.use(RadListView);

Vue.config.silent = (TNS_ENV === 'production');

import cars from "./shared/cars/car-service";

import PlantList from "./components/PlantList";
import PlantDetails from "./components/PlantDetails";
import CarDetails from "./components/CarDetails";
import CarDetailsEdit from "./components/CarDetailsEdit";

new Vue({

    render: h => h('frame', [h(PlantList)])
}).$start()
//     template: `
//         <Frame>
//             <PlantList/>
//         </Frame>`,
//
//     components: {
//         PlantList,
//         CarDetails,
//         CarDetailsEdit
//     },
//
//     data: {
//         cars: []
//     },
//
//     created() {
//         firebase.init(config).then(
//             instance => {
//                 console.log("firebase.init done");
//
//                 cars.load().then((data) => {
//                     this.cars = Object.values(data);
//                 })
//             },
//             error => {
//                 console.log(`firebase.init error: ${error}`);
//             }
//         );
//     }
// }).$start();
